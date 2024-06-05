import asyncio
import pandas as pd
import requests
from datetime import datetime
import calendar
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mdates
from CryptoData import CryptoData

class Indicators:
    def __init__(self, symbol, timeinterval):
        self.symbol = symbol
        self.timeinterval = timeinterval
    
    # RSI
    async def rsi(data):
        period = 14
        df = data
        df['close'] = df['close'].astype(float)
        df2 = df['close'].to_numpy()

        df2 = pd.DataFrame(df2, columns = ['close'])
        delta = df2.diff()

        up, down = delta.copy(), delta.copy()
        up[up < 0] = 0
        down[down > 0] = 0

        _gain = up.ewm(com=(period - 1), min_periods=period).mean()
        _loss = down.abs().ewm(com=(period - 1), min_periods=period).mean()

        RS = _gain / _loss

        rsi = 100 - (100 / (1 + RS))  
        rsi = rsi['close'].iloc[-1]
        rsi = round(rsi, 1)

        return rsi
    
    # RSI stochastic
    async def stochastic_rsi(data, period=14, smooth_k=3, smooth_d=3):
        # RSI standard 
        # Convert data to numeric
        data[['open', 'high', 'low', 'close']] = data[['open', 'high', 'low', 'close']].apply(pd.to_numeric)

        delta = data['close'].diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)

        avg_gain = gain.rolling(window=period, min_periods=1).mean()
        avg_loss = loss.rolling(window=period, min_periods=1).mean()

        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        
        # Calculate %K of stochastic RSI
        rsi_min = rsi.rolling(window=period, center=False).min()
        rsi_max = rsi.rolling(window=period, center=False).max()
        stoch = ((rsi - rsi_min) / (rsi_max - rsi_min)) * 100
        
        # Smoothing %K
        k = stoch.rolling(window=smooth_k, center=False).mean()
        
        # Calculate %D of stochastic RSI
        d = k.rolling(window=smooth_d, center=False).mean()
        
        return k, d
    
    # MACD: receive a DataFrame with the 'close' column
    async def macd(data, short_period=12, long_period=26, signal_period=9):
        # Calculate Short EMA
        short_ema = data['close'].ewm(span=short_period, min_periods=1, adjust=False).mean()

        # Calculate Long EMA
        long_ema = data['close'].ewm(span=long_period, min_periods=1, adjust=False).mean()

        # Calculate MACD line
        macd_line = short_ema - long_ema

        # Calculate Signal line
        signal_line = macd_line.ewm(span=signal_period, min_periods=1, adjust=False).mean()

        # Calculate MACD histogram
        histogram = macd_line - signal_line

        return macd_line, signal_line, histogram
        
    # Bands of Bollinger
    async def bollinger_bands(data):
        # SMA 21
        sma_21 = data['close'].rolling(window=21).mean()
        
        # Calculate lower and upper bands
        lower = sma_21 - 2 * data['close'].rolling(window=20).std()
        upper = sma_21 + 2 * data['close'].rolling(window=20).std()

        return sma_21, lower, upper
    
    # Calculate EMA of 200 periods
    async def ema_200(data):
        ema = data['close'].ewm(span=200, adjust=False).mean()
        return ema


    # (function for test) -> Moving Average
    def meanmoving(data):
            
        # Calculate MMS 30 periods
        MV30 = pd.DataFrame()
        MV30['Close'] = data['Close'].rolling(window=30).mean()# Calculate mean of 30 periods
        print("Media movil simple de 30 periodos: ", MV30.index==29)
        # Calculate MMS 100 periods
        MV100 = pd.DataFrame()
        MV100['Close'] = data['Close'].rolling(window=100).mean()# Calculate mean of 100 periods
        print("Media movil simple de 100 periodos: ", MV100==29)
        
        # Price of crossover of MMS 30 and MMS 100
        data = pd.DataFrame()
        data['BTC-USD'] = data['Close']
        data['MV30'] = MV30['Close']
        data['MV100'] = MV100['Close']
        return data
        
