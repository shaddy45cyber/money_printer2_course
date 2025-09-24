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


#fetch OHLCV data for as far back as we want
def create_since(days,mins):
    timezone=pytz.utc
    Now=dt.now(timezone)
    since=Now-timedelta(days=1*days,minutes=1*mins)
    starttime=int(since.timestamp()*1000)
    return starttime

def create_endtime():
    timezone=pytz.utc
    Now=dt.now(timezone)
    end=Now
    endtime=int(end.timestamp()*1000)
    return endtime

def calculate_mins(timeframe,periods):
   units=timeframe[-1]
   value=float(timeframe[:-1])
   if units == 'm':
      return value * periods
   elif units == 'h':
      return value * periods* 60
   elif units == 'd':
      return value * periods *60 * 24

def fetch_data(symbol,timeframe,days,mins):
    since=create_since(days,mins)
    endtime=create_endtime()
    all_candles=[]
    while since < endtime:
        try:
            candles = exchange.fetch_ohlcv(symbol,timeframe,since)
            if not candles:
                break
            all_candles.extend(candles)
            since=int(candles[-1][0]+1)
            if since >= endtime:
                break
        except ccxt.NetworkError as e:
            return []
    df=pd.DataFrame(all_candles,columns=['timestamp','open','high','low','close','volume'])
    data = np.array(df)
    return data

#for example fetch data for the past one day and 15m
candles = fetch_data(symbol,'1m',1,15)

#function for telling the candle color 
def candle_color(close,open):
   if close > open:
      return  1 # green
   elif open > close:
      return 0 # red
   else:
      return []
close = candles[:,4] # is an array 
open = candles[:,1]
low = candles[:,3]
high = candles[:,2]
timestamp = candles[:,0]
Volume = candles[:,5]
#Time first then OHLCV
Color_of_candle = candle_color(close[-1],open[-1]) # color of the last candle
if Color_of_candle == 1:
    print('Green')
else:
    print('Red')