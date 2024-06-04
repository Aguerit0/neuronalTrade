import pandas as pd
import requests
from datetime import datetime
import calendar
from datetime import datetime, timezone
import asyncio
from Indicators import Indicators
from CryptoData import CryptoData

async def main():
    while True:
        # Symnols list
        symbols = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "ADAUSDT", "XRPUSDT", 
                   "SOLUSDT", "DOTUSDT", "DOGEUSDT", "LINKUSDT", "LTCUSDT"]

        # Time interval
        timeinterval = 1
        temporalidad = f'{timeinterval}m'

        # Configure timezone
        now = datetime.now(timezone.utc)
        unixtime = calendar.timegm(now.utctimetuple())
        since = unixtime
        start = str(since - 60*60*10)    
        
        indicator = input('Indicators: \n1- RSI \n2- MACD \n3- Bollinger \n4- EMA \n5- MM \n6- Stochastic RSI \n')
        if indicator == '1':
                idc = Indicators.rsi(D)
        elif indicator == '2':
                idc = Indicators.macd(D)
        elif indicator == '3':
                idc = Indicators.bollinger_bands(D)
        elif indicator == '4':
                idc = Indicators.ema_200(D)
        elif indicator == '5':
                idc = Indicators.MM(D)
        elif indicator == '6':
                idc = Indicators.stochastic_rsi(D)


        for symbol in symbols:
                # Get data live from binance
                df_live_data = CryptoData(symbol, temporalidad)
                D = pd.DataFrame(await df_live_data.get_live_data())
                # Get indiicator
                idc = await idc(D)
                rsi = await Indicators.rsi(D) 
                if rsi <= 25 or rsi >= 75:
                        signal = 'COMPRA' if rsi <= 25 else 'VENTA'
                        text = f'Binance Futures {symbol} RSI ({temporalidad}): {rsi} - {signal}'
                        print(text)
          
        await asyncio.sleep(5)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()
