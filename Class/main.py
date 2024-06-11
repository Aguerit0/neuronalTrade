import asyncio
import requests

if __name__ == "__main__":
    print('Indicators: \n1- RSI \n2- Stochastic RSI \n3- MACD \n4- Bollinger Bands \n5- EMA 200 \n6- MM \n')
    indicator = input('Option: ')
    
    response = requests.get(f"http://127.0.0.1:8000/alerts/{indicator}")
    print(response.json())