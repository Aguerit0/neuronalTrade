import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import pandas as pd
import requests
from datetime import datetime, timezone
from CryptoData import CryptoData
from Indicators import Indicators
from plotly.subplots import make_subplots


class GraphicIndicators:
    def __init__(self):
        self.symbols = [
            "BTCUSDT",
            "ETHUSDT",
            "BNBUSDT",
            "ADAUSDT",
            "XRPUSDT",
            "SOLUSDT",
            "DOTUSDT",
            "DOGEUSDT",
            "LINKUSDT",
            "LTCUSDT",
        ]
        self.timeinterval = 1
        self.temporalidad = f"{self.timeinterval}m"

    async def fetch_data(self, symbol):
        df_live_data = CryptoData(symbol, self.temporalidad)
        return await df_live_data.get_live_data()

    async def graphic_rsi(self):
        results = []
        for symbol in self.symbols:
            df_live_data = CryptoData(symbol, self.temporalidad)
            D = pd.DataFrame(await df_live_data.get_live_data())
            rsi = await Indicators.rsi(D)
            last_rsi = rsi.iloc[-1].round(2)
