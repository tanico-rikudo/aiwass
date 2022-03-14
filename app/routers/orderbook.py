from fastapi import APIRouter, Depends
from typing import List, Optional
import app.schemas.orderbook as orderbook_schema
import app.cruds.orderbook as orderbook_crud
from sqlalchemy.orm import Session
from db.db import get_db

# import app.models.trade as trade_model
from sqlalchemy import select

router = APIRouter()

from util import daylib
dl = daylib.daylib()


@router.get("/orderbooks",response_model=List[orderbook_schema.OrderBookResponseBase])
async def list_orderbooks(db: Session = Depends(get_db), symbol:str = None, since_date:int = None, until_date:int = None):
    if symbol is None:
         raise HTTPException(status_code=404, detail="Symbol must be set")
    if since_date is None:
         raise HTTPException(status_code=404, detail="since_date must be set")
    if until_date is None: 
        until_date = since_date
    return orderbook_crud.get_orderbook(db, symbol, since_date, until_date)