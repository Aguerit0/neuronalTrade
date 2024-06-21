"""Mock data to populate the dashboard charts and tables."""

import reflex as rx
from neuronalTrade.graphs import Area, Line, line_chart
import asyncio
from neuronalTrade.Class.CryptoData import CryptoData
import pandas as pd

# Instance of CryptoData class
symbol = "BTCUSDT"
time_interval = "1m"
crypto_data = CryptoData(symbol, time_interval)

# Function to get data from the API
async def get_live_data():
    data = await crypto_data.get_live_data()
    # Convert JSON to DataFrame
    live_data = data[['open_time', 'close']].rename(columns={'open_time': 'name', 'close': 'uv'})
    live_data['name'] = pd.to_datetime(live_data['name'], unit='ms').astype(str)  # Convert to string
    live_data_dict = live_data.to_dict('records')
    return live_data_dict

# Function to update chart data
async def update_chart_data():
    live_data_dict = await get_live_data()
    return live_data_dict

# Placeholder for line chart data
line_chart_data = []  # This will be updated asynchronously later

stat_card_data = [
    [
        "Today's Money",
        "$53,000",
        "+2%",
    ],
    [
        "Today's Users",
        "2,300",
        "+5%",
    ],
    [
        "Today's Orders",
        "1,400",
        "-3%",
    ],
    [
        "Today's Sales",
        "$23,000",
        "+2%",
    ],
]

lines_data_live = [
    Line(data_key="uv", stroke="#8884d8"),
    Line(data_key="pv", stroke="var(--accent-8)"),
]

pie_chart_data = [
    {"name": "Group A", "value": 400, "fill": "var(--red-7)"},
    {"name": "Group B", "value": 300, "fill": "var(--green-7)"},
    {"name": "Group C", "value": 300, "fill": "var(--purple-7)"},
    {"name": "Group D", "value": 200, "fill": "var(--blue-7)"},
    {"name": "Group E", "value": 278, "fill": "var(--yellow-7)"},
    {"name": "Group F", "value": 189, "fill": "var(--pink-7)"},
]

area_chart_data = line_chart_data

areas = [
    Area(data_key="pv", stroke="#8884d8", fill="#8884d8"),
    Area(data_key="uv", stroke="var(--accent-8)", fill="var(--accent-8)"),
]

tabular_data = [
    ["Full name", "Email", "Group"],
    ["Danilo Sousa", "danilo@example.com", rx.badge("Developer")],
    ["Zahra Ambessa", "zahra@example.com", rx.badge("Admin", variant="surface")],
    ["Jasper Eriksson", "jasper@example.com", rx.badge("Developer")],
]


# Inicializa el componente line_chart con una lista vacía por defecto
line_chart_component = line_chart(data=[], data_key="name", lines=lines_data_live)

# Función para inicializar y actualizar los datos del gráfico
async def initialize_chart_data():
    global line_chart_component
    line_chart_data = await update_chart_data()
    # Re-renderiza el componente del gráfico con los nuevos datos
    line_chart_component = line_chart(data=line_chart_data, data_key="name", lines=lines_data_live)

# Función de arranque para el módulo
def start_data_initialization():
    loop = asyncio.get_event_loop()
    if loop.is_running():
        loop.create_task(initialize_chart_data())
    else:
        loop.run_until_complete(initialize_chart_data())

# Llama a la función de arranque
start_data_initialization()