from fastapi import APIRouter, Depends
from typing import List, Optional
import app.schemas.trade as trade_schema
import app.cruds.trade as trade_crud
from sqlalchemy.orm import Session
from db.db import get_db

import app.models.trade as trade_model
from sqlalchemy import select

router = APIRouter()

from util import daylib
dl = daylib.daylib()


@router.get("/trades",response_model=List[trade_schema.TradeResponseBase])
async def list_trades(db: Session = Depends(get_db), symbol:str = None, since_date:int = None, until_date:int = None):
    if symbol is None:
         raise HTTPException(status_code=404, detail="Symbol must be set")
    if since_date is None:
         raise HTTPException(status_code=404, detail="since_date must be set")
    if until_date is None: 
        until_date = since_date
    return trade_crud.get_trades(db, symbol, since_date, until_date)

@router.get("/trades/bulk",response_model=List[trade_schema.TradeResponseBase])
async def bulk_import_trades(db: Session = Depends(get_db), symbol:str = None, since_date:int = None, until_date:int = None):
    if symbol is None:
         raise HTTPException(status_code=404, detail="Symbol must be set")
    if since_date is None:
         raise HTTPException(status_code=404, detail="since_date must be set")
    if until_date is None: 
        until_date = since_date
    return trade_crud.import_trade(db, symbol, since_date, until_date)

@router.post("/trades", response_model=trade_schema.TradeCreateResponse)
async def create_trade(trade_body: trade_schema.TradeCreate, db:Session = Depends(get_db)):
    trade_body.event_datetime = dl.strYMDHMSF_to_dt(str(trade_body.event_datetime))
    return trade_crud.create_trade(db, trade_body)