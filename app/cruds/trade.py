
from typing import List, Tuple, Optional

from sqlalchemy import select, func
from sqlalchemy.orm import Session, sessionmaker
import app.models.trade as trade_model
import app.schemas.trade as trade_schema
from sqlalchemy.engine import Result
from sqlalchemy.dialects import sqlite

from mongodb.src.mongo_handler import MongoHandler

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
    since_date = dl.intD_to_dt(since_date) 
    until_date = dl.intD_to_dt(dl.add_day(until_date,1))
    result=(
        db.query(
            
                trade_model.Trade.id,
                trade_model.Trade.event_datetime,
                trade_model.Trade.symbol,
                trade_model.Trade.price,
                trade_model.Trade.size,
                trade_model.Trade.ask,
                trade_model.Trade.bid,
                trade_model.Trade.flag01,
                trade_model.Trade.flag02,
                trade_model.Trade.flag03
            ).filter(trade_model.Trade.symbol==symbol) \
    .filter(trade_model.Trade.event_datetime>= since_date) \
    .filter(trade_model.Trade.event_datetime< until_date)
        )
    
    logging.info(result.statement.compile(dialect=sqlite.dialect(),
                                  compile_kwargs={"literal_binds": True}))

    return result.all()

def create_trade(
    db: Session, trade_create: trade_schema.TradeCreate
        )  -> trade_model.Trade:
    """ Create trade
    Returns: 
        trade_model.Trade
    """
    trade = trade_model.Trade(**trade_create.dict())
    db.add(trade)
    db.commit()
    db.refresh(trade)
    return trade


def import_trade(db:Session, symbol:str, since_date:int, until_date:int):
    cm = ConfigManager(os.environ["KULOKO_INI"])
    mongo_ini = cm.load_ini_config(path=None, config_name="mongo", mode=None)
    
    #TODO: set dynamic
    mongo_config_mode = "DOCKER"
    mongo_db = MongoHandler(mongo_ini[mongo_config_mode], self.item_type)
    db_accesser = MongoUtil(mongo_db, logging)
    
    #TODO: Optimize. Fetch multiple days in only one time.
    
    ls_date = dl.get_between_date(since_date, until_date)
    for int_date in ls_date:
        return_data = db_accesser.find_at_date(table='trade',symbol=symbol, date = int_date)
        db.bulk_save_objects(
        [trade_model.Trade(
            symbol=d["symbol"],
                event_datetime=d["time"],
                price=d["price"],
                size = d["size"],
                ask = d["ask"],
                bid = d["bid"])
        for d in return_data], return_defaults=True)
        
        db.commit()

def delete_trade(db: Session, date: int) -> None:
    """ Delte Trade for daily bbatch
    Args:
        db (Session): [description]
    """
    db.query(trade_model.Trade).delete()
    db.commit()
