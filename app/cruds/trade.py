import os
import pandas as pd
from typing import List, Tuple, Optional

from sqlalchemy import select, func
from sqlalchemy.orm import Session, sessionmaker
import app.models.trade as trade_model
import app.schemas.trade as trade_schema
from sqlalchemy.engine import Result
from sqlalchemy.dialects import sqlite

from mongodb.src.mongo_handler import *

from util.config import ConfigManager
from util.exceptions import *
from util import daylib
from util import utils
dl = daylib.daylib()

import logging

def get_trades(db:Session, symbol:str, since_date:int, until_date:int) -> List[Tuple[int, str, str, str, str]]:
    """ Lookup trade by sym and date

    Returns:
        trade_model.Trade
    """


    until_date = dl.add_day(until_date,1)
    
    cm = ConfigManager(os.environ["KULOKO_INI"])
    mongo_ini = cm.load_ini_config(path=None, config_name="mongo", mode=None)
    
    #TODO: set dynamic
    mongo_config_mode = "DOCKER"
    mongodb = MongoHandler(mongo_ini[mongo_config_mode], 'trade')
    db_accesser = MongoUtil(mongodb, logging)
    
    ls_date = dl.get_between_date(since_date, until_date)

    trades = []
    sorted(ls_date)
    results = db_accesser.find_between_dates(table='trade',symbol=symbol, sd = min(ls_date), ed= max(ls_date))
    for result in results:      
        trades.append(result)

    # TODO: TOO heavy. So ma
    return trades[:10]


def get_ohlcv(db:Session, symbol:str,  since_date:int, until_date:int) -> List[Tuple[int, str, str, str, str]]:
    #TODO: Add interval string. 
    logger = logging.getLogger('uvicorn')  
    trades = get_trades(db, symbol, since_date, until_date)
    trades = [ _trade for _trade in trades ]
    df = pd.DataFrame(trades)
    df['time'] = df['time'].apply( lambda x : dl.strYMDHMSF_to_dt(x))
    df.set_index('time',inplace=True)
    df_ohlc = df['price'].resample('T').ohlc()
    df_ohlc.loc[:,['open','high','low','close']] = df_ohlc.loc[:,['open','high','low','close']].fillna(method='ffill')
    df_v = df['size'].resample('T').sum()
    df_ohlcv = pd.concat([df_ohlc, df_v],axis=1).reset_index()
    df_ohlcv['time'] = df_ohlcv['time'].apply( lambda x : dl.dt_to_strYMDHMSF(x))
    df_ohlcv['symbol'] = symbol

    return df_ohlcv.to_dict(orient='records')