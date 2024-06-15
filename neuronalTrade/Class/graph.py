import plotly.graph_objects as go
import requests
import time

def fetch_live_data():
    response = requests.get("http://localhost:8000/api/live-data")
    data = response.json()
    return data["data"]

# Configura el gráfico inicial
fig = go.Figure()
fig.add_trace(go.Scatter(x=[], y=[], mode='lines+markers'))

# Muestra el gráfico vacío inicialmente
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
