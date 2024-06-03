import asyncio
import pandas as pd
import requests
import telegram
from datetime import datetime
import calendar
from Indicators import *
from CryptoData import *

# Lista de símbolos para monitorear
symbols = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "ADAUSDT", "XRPUSDT", 
           "SOLUSDT", "DOTUSDT", "DOGEUSDT", "LINKUSDT", "LTCUSDT"]

# Configuración de intervalo de tiempo y consulta de datos
timeinterval = 5
temporalidad = f'{timeinterval} minutos'

now = datetime.utcnow()
unixtime = calendar.timegm(now.utctimetuple())
since = unixtime
start = str(since - 60*60*10)

async def main():
    for symbol in symbols:
        url = 'https://fapi.binance.com/fapi/v1/klines?symbol='+symbol+'&interval='+str(timeinterval)+'m'+'&limit=100'
        data = requests.get(url).json()        

        D = pd.DataFrame(data)
        D.columns = ['open_time', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'qav', 'num_trades',
                             'taker_base_vol', 'taker_quote_vol', 'is_best_match']
        
        # Get Live Data
        live_data = await CryptoData('BTCUSDT', timeinterval).get_live_data()  # Espera el resultado de la corutina
        
        # Get Historical Price
        print(live_data)

# Ejecutar la función principal como una tarea asincrónica
asyncio.run(main())
import asyncio
import pandas as pd
import requests
import telegram
from datetime import datetime
import calendar
from Indicators import *
from CryptoData import *

# Lista de símbolos para monitorear
symbols = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "ADAUSDT", "XRPUSDT", 
           "SOLUSDT", "DOTUSDT", "DOGEUSDT", "LINKUSDT", "LTCUSDT"]

# Configuración de intervalo de tiempo y consulta de datos
timeinterval = 5
temporalidad = f'{timeinterval} minutos'

now = datetime.utcnow()
unixtime = calendar.timegm(now.utctimetuple())
since = unixtime
start = str(since - 60*60*10)

async def main():
    for symbol in symbols:
        url = 'https://fapi.binance.com/fapi/v1/klines?symbol='+symbol+'&interval='+str(timeinterval)+'m'+'&limit=100'
        data = requests.get(url).json()        

        D = pd.DataFrame(data)
        D.columns = ['open_time', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'qav', 'num_trades',
                             'taker_base_vol', 'taker_quote_vol', 'is_best_match']
        
        # Get Live Data
        live_data = pd.DataFrame()
        live_data = await CryptoData('BTCUSDT', timeinterval).get_live_data()  # Espera el resultado de la corutina
        
        # Get Historical Price
        
        print(live_data[0])

# Ejecutar la función principal como una tarea asincrónica
asyncio.run(main())
