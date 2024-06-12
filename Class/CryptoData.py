import pandas as pd
import requests
from datetime import datetime, timezone

import calendar
from binance.spot import Spot as Client

class CryptoData:
    def __init__(self, symbol, timeinterval):
        self.symbol = symbol
        self.timeinterval = timeinterval
    
    async def get_live_data(self):
        now = datetime.now(timezone.utc)
        unixtime = calendar.timegm(now.utctimetuple())
        since = unixtime
        start = str(since - 60*60*10)
        
        url = 'https://fapi.binance.com/fapi/v1/klines?symbol='+self.symbol+'&interval='+str(self.timeinterval)+'&limit=100'
        data = requests.get(url).json()        
        
        D = pd.DataFrame(data)
        D.columns = ['open_time', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'qav', 'num_trades',
                     'taker_base_vol', 'taker_quote_vol', 'is_best_match']
    
        return D

    @staticmethod
    def get_historical_price(symbol, timeinterval):
        # URL para acceder a la API de Binance
        base_url = "https://api.binance.com"
        
        # Crear cliente para acceder a la API
        spot_client = Client(base_url=base_url)
        
        # Acceder a los datos históricos del símbolo
        history = spot_client.klines(symbol, timeinterval, limit=2000)
        
        # Convertir los datos a DataFrame
        columns = ['time', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 
                   'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore']
        df = pd.DataFrame(history, columns=columns)
        df['time'] = pd.to_datetime(df['time'], unit='ms')
        
        # Devolver el DataFrame con los datos históricos
        return df
