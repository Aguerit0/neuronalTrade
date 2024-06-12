import asyncio
import requests
import plotly.graph_objects as go
import time

if __name__ == "__main__":
    #print('Indicators: \n1- RSI \n2- Stochastic RSI \n3- MACD \n4- Bollinger Bands \n5- EMA 200 \n6- MM \n')
    #indicator = input('Option: ')
    
    #response = requests.get(f"http://127.0.0.1:8000/alerts/{indicator}")
    #print(response.json())
    
    def fetch_live_data():
        response = requests.get("http://localhost:8000/api/live_data")
        data = response.json()
        return data["data"]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[], y=[], mode='lines+markers'))
    fig.show()
    
    while True:
        new_data = fetch_live_data()
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        
        # Agrega nuevos datos al gráfico
        fig.add_trace(go.Scatter(x=[current_time], y=[new_data], mode='lines+markers'))
        
        # Actualiza el gráfico
        fig.show()
        
        # Espera 60 segundos antes de obtener nuevos datos
        time.sleep(60)