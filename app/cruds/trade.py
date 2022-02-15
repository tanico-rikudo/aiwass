
from typing import List, Tuple, Optional

from sqlalchemy import select, func
from sqlalchemy.orm import Session, sessionmaker
import app.models.trade as trade_model
import app.schemas.trade as trade_schema
from sqlalchemy.engine import Result
from sqlalchemy.dialects import sqlite


from util.exceptions import *
from util import daylib
from util import utils
dl = daylib.daylib()

import logging

def get_trades(db:Session, symbol:str, since_date:int, until_date:int) -> List[Tuple[int, str, str, str, str]]:
    """ Lookup trade by id

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

