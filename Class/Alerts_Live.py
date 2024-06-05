import pandas as pd
import requests
from datetime import datetime
import calendar
from datetime import datetime, timezone
import asyncio
from Indicators import Indicators
from CryptoData import CryptoData

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
            if rsi <= 30 or rsi >= 70: 
                    signal = 'COMPRA' if rsi <= 30 else 'VENTA'
                    text = f'Binance Futures {symbol} RSI ({self.temporalidad}): {rsi} - {signal}'
                    print(text)

    async def check_stochastic_rsi(self):
        for symbol in self.symbols:
            # Get data live from binance
            data = await self.fetch_data(symbol)
            k, d = await Indicators.stochastic_rsi(data)
            # print signals for each symbol
            if (k.iloc[-1]<=15 and k.iloc[-1]>d.iloc[-1] and k.iloc[-2]<d.iloc[-2]):
                signal = f'{symbol}: COMPRA (Stochastiic RSI) - valor: {k.iloc[-1]}'
                print(signal)
            elif (k.iloc[-1]>=85 and k.iloc[-1]<d.iloc[-1] and k.iloc[-2]>d.iloc[-2]):
                signal = f'{symbol}: VENTA (Stochastiic RSI) - valor {k.iloc[-1]}'
                print(signal)
                

    async def check_macd(self):
        for symbol in self.symbols:
            # Get data live from binance
            data = await self.fetch_data(symbol)
            stoch_k_smooth, stoch_d = await Indicators.stochastic_rsi(data)
            print(stoch_d, stoch_k_smooth)

    async def check_bollinger_bands(self):
        for symbol in self.symbols:
            # Get data live from binance
            data = await self.fetch_data(symbol)
            sma_21, lower, upper = await Indicators.bollinger_bands(data)
            print(sma_21, lower, upper) 

    async def check_ema_200(self):
        for symbol in self.symbols:
            # Get data live from binance
            data = await self.fetch_data(symbol)
            ema200 = await Indicators.ema_200(data)
            print(ema200)   

    async def check_meanmoving(self):
        for symbol in self.symbols:
            # Get data live from binance
            data = await self.fetch_data(symbol)
            meanmoving = pd.DataFrame()
            meanmoving = await Indicators.meanmoving(data)
            print(meanmoving)

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
                await self.check_mm()
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