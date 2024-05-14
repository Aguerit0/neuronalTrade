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
    
    # RSI estocastico
    def stochastic_rsi(data, period=14, smooth_k=3, smooth_d=3):
        # Calcula el RSI estándar
        # Convertir las columnas 'open', 'high', 'low' y 'close' a tipo numérico
        data[['open', 'high', 'low', 'close']] = data[['open', 'high', 'low', 'close']].apply(pd.to_numeric)

        delta = data['close'].diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)

        avg_gain = gain.rolling(window=period, min_periods=1).mean()
        avg_loss = loss.rolling(window=period, min_periods=1).mean()

        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        
        # Calcula el %K del RSI estocástico
        rsi_min = rsi.rolling(window=period).min()
        rsi_max = rsi.rolling(window=period).max()
        stoch_k = ((rsi - rsi_min) / (rsi_max - rsi_min)) * 100
        
        # Aplica suavizado a %K
        stoch_k_smooth = stoch_k.rolling(window=smooth_k).mean()
        
        # Calcula %D del RSI estocástico
        stoch_d = stoch_k_smooth.rolling(window=smooth_d).mean()
        
        return stoch_k_smooth, stoch_d
    
    # MACD: recibe un DataFrame con la columna 'close'
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

        # Datos de la estrategia
        print("MACD: ", macd_line.iloc[-1], " | Signal: ", signal_line.iloc[-1], " | Histogram: ", histogram.iloc[-1])
        
    # Bandas de Bollinger
    async def bollinger_bands(data):
        # SMA 21
        sma_21 = data['close'].rolling(window=21).mean()
        
        # Banda inferior y superior
        lower = sma_21 - 2 * data['close'].rolling(window=20).std()
        upper = sma_21 + 2 * data['close'].rolling(window=20).std()

        return sma_21, lower, upper
    
    # Función para calcular la EMA de 200 períodos
    async def ema_200(data):
        # Calcular la media móvil exponencial de 200 períodos
        ema = data['close'].ewm(span=200, adjust=False).mean()
        return ema
