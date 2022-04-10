from fastapi import APIRouter, Depends
from typing import List, Optional
import app.schemas.prediction as prediction_schema
import app.cruds.trade as prediction_crud
from sqlalchemy.orm import Session
from db.db import get_db

import app.models.trade as trade_model
from sqlalchemy import select

router = APIRouter()

from util import daylib

dl = daylib.daylib()


@router.get("/prediction", response_model=List[prediction_schema.PredictionResponseBase])
async def list_predictions(db: Session = Depends(get_db), symbol: str = None, date: int = None,
                      time: int = None):
    if symbol is None:
        raise HTTPException(status_code=500, detail="Symbol must be set")
    if date is None:
        raise HTTPException(status_code=500, detail="date must be set")
    if time is None:
        raise HTTPException(status_code=500, detail="time must be set")
    return prediction_crud.get_trades(db, symbol, date, time)
