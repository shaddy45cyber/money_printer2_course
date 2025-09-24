import ccxt
import pandas as pd
import numpy as np
from datetime import datetime  as dt, timedelta
import pytz
import time
import warnings
import tulipy as ti

# public instance 
exchange = ccxt.binance()

#private instance
Apikey = "your apikey"
Secretkey = "your secretkey"
Exchange = ccxt.binance({
    'apikey':Apikey,
    'secret':Secretkey,
    'enableRateLimit':True,
    'options':{
    'defaultType':'future'
    }
})

exchange.load_markets()
symbol = 'DOGEUSDT'



