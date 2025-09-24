import MetaTrader5 as mt5

import pandas as pd
import numpy as np
import time
from datetime import datetime as dt , timedelta
import pytz

symbol = "XAUUSD"
magic_no = 123456

mt5.initialize()
#your trading bots 
mt5.shutdown

