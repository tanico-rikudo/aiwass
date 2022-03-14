import os
from typing import List, Tuple, Optional

from sqlalchemy import select, func
from sqlalchemy.orm import Session, sessionmaker
import app.models.orderbook as orderbook_model
# import app.schemas.trade as trade_schema
from sqlalchemy.engine import Result
from sqlalchemy.dialects import sqlite

from mongodb.src.mongo_handler import *
from util.exceptions import *
from util.config import ConfigManager
from util import daylib
from util import utils
dl = daylib.daylib()

import logging

def get_orderbook(db:Session, symbol:str, since_date:int, until_date:int) -> List[Tuple[str, int, float, float, float, float]]:
    """ Lookup orderbook by sym and date

    Returns:
       List[Tuple[str, int, float, float, float, float]
    """

    until_date = dl.add_day(until_date,1)
    
    cm = ConfigManager(os.environ["KULOKO_INI"])
    mongo_ini = cm.load_ini_config(path=None, config_name="mongo", mode=None)
    
    #TODO: set dynamic
    mongo_config_mode = "DOCKER"
    mongo_db = MongoHandler(mongo_ini[mongo_config_mode], 'orderbook')
    db_accesser = MongoUtil(mongo_db, logging)
    
    ls_date = dl.get_between_date(since_date, until_date)

    orderbooks = []
    sorted(ls_date)
    results = db_accesser.find_between_dates(table='orderbook',symbol=symbol, sd = min(ls_date), ed= max(ls_date))
    for result in results:      
        orderbooks.append(result)

    # TODO: TOO heavy. So ma
    return orderbooks[:10]