import pandas as pd
from CryptoData import CryptoData


def export_to_csv(data):
    data.to_csv("data.csv", index=False)


# test
data = CryptoData("BTCUSDT", "1h")
historical_data = data.get_historical_price()
export_to_csv(historical_data)
