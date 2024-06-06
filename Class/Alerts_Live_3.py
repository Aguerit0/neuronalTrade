import pandas as pd
import requests
from datetime import datetime
import calendar
from datetime import datetime, timezone
import asyncio
from Indicators import Indicators
from CryptoData import CryptoData
import numpy as np

class AlertLive:
    def __init__(self):
        self.symbols = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "ADAUSDT", "XRPUSDT", 
               "SOLUSDT", "DOTUSDT", "DOGEUSDT", "LINKUSDT", "LTCUSDT"]
        self.timeinterval = 1
        self.temporalidad = f'{self.timeinterval}m'

    async def fetch_data(self, symbol):
        df_live_data = CryptoData(symbol, self.temporalidad)
        return await df_live_data.get_live_data()

    async def check_rsi(self):
        # loop for each symbol
        for symbol in self.symbols:
            # Get data live from binance
            df_live_data = CryptoData(symbol, self.temporalidad)
            D = pd.DataFrame(await df_live_data.get_live_data())
            # Get indicator
            rsi = await Indicators.rsi(D) 
            last_rsi = rsi.iloc[-1].round(2)
            if last_rsi <= 30 or last_rsi >= 70: 
                    signal = 'COMPRA' if last_rsi <= 30 else 'VENTA'
                    
                    text = f'Binance Futures {symbol} RSI ({self.temporalidad}): {last_rsi} - {signal}'
                    print(text)

    async def check_stochastic_rsi(self):
        for symbol in self.symbols:
            # Get data live from binance
            data = await self.fetch_data(symbol)
            rsi_values = await Indicators.rsi(data)
            k, d = await Indicators.stochastic_rsi(rsi_values)
            # print signals for each symbol
            if (k.iloc[-1]<=15 and k.iloc[-1]>d.iloc[-1] and k.iloc[-2]<d.iloc[-2]):
                signal = f'{symbol}: COMPRA (Stochastiic RSI) - valor: {k.iloc[-1]}'
                print(signal)
            elif (k.iloc[-1]>=85 and k.iloc[-1]<d.iloc[-1] and k.iloc[-2]>d.iloc[-2]):
                signal = f'{symbol}: VENTA (Stochastiic RSI) - valor {k.iloc[-1]}'
                print(signal)
                

    async def check_macd(self):
        for symbol in self.symbols:
            # Obtener datos en vivo de Binance
            data = await self.fetch_data(symbol)
            macd_line, signal_line, histogram = await Indicators.macd(data)
            data_macd = pd.DataFrame()
            data_macd['MACD'] = macd_line
            data_macd['Signal'] = signal_line
            data_macd['Histogram'] = histogram

            signal = self.macd_signal(data_macd)
            if signal == 1:
                print(f'{symbol}: BUY (MACD) - Price: {data["close"].iloc[-1]}')
            elif signal == -1:
                print(f'{symbol}: SELL (MACD) - Price: {data["close"].iloc[-1]}')

    def macd_signal(self, data_macd):
        # Solo revisamos la última señal
        if data_macd['MACD'].iloc[-1] > data_macd['Signal'].iloc[-1]:
            return 1  # buy signal
        elif data_macd['MACD'].iloc[-1] < data_macd['Signal'].iloc[-1]:
            return -1  # sell signal
        else:
            return 0  # no signal   

       
                
    async def check_bollinger_bands(self):
        for symbol in self.symbols:
            # Get data live from binance
            data = await self.fetch_data(symbol)
            sma_21, lower, upper = await Indicators.bollinger_bands(data)
            # Calculate signal
            data['close'] = data['close'].astype(float)
            if data['close'].iloc[-1] > upper.iloc[-1]:
                print(f'{symbol}: SELL (Bollinger Bands) - Price: {data["close"].iloc[-1]}')
                
            elif data['close'].iloc[-1] < lower.iloc[-1]:
                print(f'{symbol}: BUY (Bollinger Bands) - Price: {data["close"].iloc[-1]}')
                


    async def check_ema_200(self):
        for symbol in self.symbols:
            # Get data live from binance
            data = await self.fetch_data(symbol)
            data['close'] = data['close'].astype(float)
            ema200 = await Indicators.ema_200(data)
            #print(ema200.iloc[-1])
            # Calculate signal
            if data['close'].iloc[-1] > ema200.iloc[-1] and data['close'].iloc[-2] < ema200.iloc[-1]:
                print(f'{symbol}: SUPPORT (EMA 200) - Price: {data["close"].iloc[-1]}')
            elif data['close'].iloc[-1] < ema200.iloc[-1] and data['close'].iloc[-2] > ema200.iloc[-1]:
                print(f'{symbol}: RESISTANCE (EMA 200) - Price: {data["close"].iloc[-1]}')

    async def check_moving_averages(self):
        for symbol in self.symbols:
            # Get data live from binance
            data = await self.fetch_data(symbol)
            moving_average = pd.DataFrame()
            moving_average = await Indicators.moving_averages(data)
            # Calculate signal
            if((moving_average['MM_5'].iloc[-2] and moving_average['MM_10'].iloc[-2])<moving_average['MM_20'].iloc[-2] and (moving_average['MM_5'].iloc[-1] and moving_average['MM_10'].iloc[-1])>moving_average['MM_20'].iloc[-1]):
                print(f'{symbol}: BUY (MM) - Price: {data["close"].iloc[-1]}')
            elif((moving_average['MM_5'].iloc[-2] and moving_average['MM_10'].iloc[-2])>moving_average['MM_20'].iloc[-2] and (moving_average['MM_5'].iloc[-1] and moving_average['MM_10'].iloc[-1])<moving_average['MM_20'].iloc[-1]):
                print(f'{symbol}: SELL (MM) - Price: {data["close"].iloc[-1]}')

    async def run(self, indicator):
        # Loop for indicators methods
        while True:
            if indicator == '1':
                await self.check_rsi()
            elif indicator == '2':
                await self.check_stochastic_rsi()
            elif indicator == '3':
                await self.check_macd()
            elif indicator == '4':
                await self.check_bollinger_bands()
            elif indicator == '5':
                await self.check_ema_200()
            elif indicator == '6':
                await self.check_moving_averages()
            await asyncio.sleep(5)
        
if __name__ == "__main__":
    
    print('Indicators: \n1- RSI \n2- Stochastic RSI \n3- MACD \n4- Bollinger Bands \n5- EMA 200 \n6- MM \n')
    indicator = input('Option: ')

    bot = AlertLive()

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(bot.run(indicator))
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()