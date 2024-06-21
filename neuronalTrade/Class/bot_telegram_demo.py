import asyncio
import pandas as pd
import requests
import telegram
from datetime import datetime
import calendar
from datetime import datetime, timezone

# Reemplaza 'your_token' con el token de tu bot
chat_id = '-4192881719'
bot = telegram.Bot(token='7088629547:AAFOim8jVRZ2HUmnWRiHOtU9LNDz12-_ZJo')

async def send_message(chat_id, text):
    await bot.send_message(chat_id=chat_id, text=text)

async def main():
    while True:
        # Lista de símbolos para monitorear
        symbols = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "ADAUSDT", "XRPUSDT", 
                   "SOLUSDT", "DOTUSDT", "DOGEUSDT", "LINKUSDT", "LTCUSDT"]

        # Configuración de intervalo de tiempo y consulta de datos
        timeinterval = 1
        temporalidad = f'{timeinterval} minutos'

        now = datetime.now(timezone.utc)
        unixtime = calendar.timegm(now.utctimetuple())
        since = unixtime
        start = str(since - 60*60*10)    

        for symbol in symbols:
            url = 'https://fapi.binance.com/fapi/v1/klines?symbol='+symbol+'&interval='+str(timeinterval)+'m'+'&limit=100'
            data = requests.get(url).json()        

            D = pd.DataFrame(data)
            D.columns = ['open_time', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'qav', 'num_trades',
                         'taker_base_vol', 'taker_quote_vol', 'is_best_match']

            # Cálculo del RSI
            period = 14
            df = D
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

            if rsi <= 25 or rsi >= 75:
                signal = 'COMPRA' if rsi <= 25 else 'VENTA'
                text = f'Binance Futures {symbol} RSI ({temporalidad}): {rsi} - {signal}'
                await send_message(chat_id=chat_id, text=text)
          
        await asyncio.sleep(5)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()
