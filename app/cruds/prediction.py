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
from postgres.src.postgres_handler import *

dl = daylib.daylib()

import logging


def get_predictions(db: Session, symbol: str, date: int, time: int) -> List[Tuple[int, str, str, str, str]]:
    """ Lookup trade by sym and date

    Returns:
        trade_model.Trade
    """

    cm = ConfigManager(os.environ["KULOKO_INI"])
    mongo_ini = cm.load_ini_config(path=None, config_name="mongo", mode=None)

    # TODO: set dynamic
    postgresHandler = PostgresHandler()
    db_accesser = PostgresUtil(postgresHandler, logging)
    results = db_accesser.get_realtime_prediction()

    return results

