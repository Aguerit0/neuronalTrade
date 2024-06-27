import asyncio
import requests
import plotly.graph_objects as go
import time
import pandas as pd
from datetime import datetime, date
import json

if __name__ == "__main__":
    time = pd.DataFrame()

    # print('Indicators: \n1- RSI \n2- Stochastic RSI \n3- MACD \n4- Bollinger Bands \n5- EMA 200 \n6- MM \n')
    # indicator = input('Option: ')

    # response = requests.get(f"http://127.0.0.1:8000/alerts/{indicator}")
    # print(response.json())

    def fetch_live_data():
        response = requests.get(" ")
        data = response.json()
        # Convert JSON to DataFrame
        if "data" in data and isinstance(data["data"], list):
            data = pd.json_normalize(data["data"])
        else:
            raise ValueError("Unexpected JSON format")

        # Add the 'time' column
        data["time_now"] = datetime.now()

        return data

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[], y=[], mode="lines"))
    fig.show()
    while True:
        df = pd.DataFrame(fetch_live_data())
        df = df.iloc[:, [4, 12]]
        print(df.iloc[-1])
        # Add new data to the graph
        fig.add_trace(go.Scatter(x=df["time_now"], y=df["close"], mode="lines"))

        # Update the graph
        fig.show()

        # Wait 60s / before getting new data
        # time.sleep(60)
