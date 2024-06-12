# api.py

from fastapi import FastAPI, HTTPException, WebSocketDisconnect
from Alerts_Live import AlertLive
import logging
from fastapi.websockets import WebSocket
import asyncio
from CryptoData import CryptoData
import pandas as pd

# Configurar el registro
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
bot = AlertLive()
symbols = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "ADAUSDT", "XRPUSDT", 
               "SOLUSDT", "DOTUSDT", "DOGEUSDT", "LINKUSDT", "LTCUSDT"]
timeinterval = "1m"
bot_CryptoData = CryptoData("BTCUSDT", timeinterval)


@app.get("/alerts/rsi", summary="Get rsi alerts", description="Get rsi alert crypto for a symbol and time interval")
async def get_rsi_alerts():
    try:
        results = await bot.check_rsi()
        return {"alerts": results}
    except Exception as e:
        logger.error(f"Error RSI alerts: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
   
@app.get("/alerts/stochastic-rsi", summary="Get stochastic rsi alerts", description="Get stochastic rsi alert crypto for a symbol and time interval")
async def get_stochastic_rsi_alerts():
    try:
        results = await bot.check_stochastic_rsi()
        return {"alerts": results}
    except Exception as e:
        logger.error(f"Error Stochastic RSI alerts: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
   
@app.get("/alerts/macd", summary="Get macd alerts", description="Get macd alert crypto for a symbol and time interval")
async def get_macd_alerts():
    try:
        results = await bot.check_macd()
        return {"alerts": results}
    except Exception as e:
        logger.error(f"Error MACD alerts: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
   
@app.get("/alerts/bollinger-bands", summary="Get bollinger bands alerts", description="Get bollinger bands alert crypto for a symbol and time interval")
async def get_bollinger_bands_alerts():
    try:
        results = await bot.check_bollinger_bands()
        return {"alerts": results}
    except Exception as e:
        logger.error(f"Error Bollinger Bands alerts: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/alerts/ema-200", summary="Get ema-200 alerts", description="Get ema-200 alert crypto for a symbol and time interval")
async def get_ema_200_alerts():
    try:
        results = await bot.check_ema_200()
        return {"alerts": results}
    except Exception as e:
        logger.error(f"Error EMA-200 alerts: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/alerts/moving-averages", summary="Get moving averages alerts", description="Get moving averages alert crypto for a symbol and time interval")
async def get_moving_averages_alerts():
        try:
            results = await bot.check_moving_averages()
            return {"alerts": results}
        except Exception as e:
            logger.error(f"Error Moving Averages alerts: {e}")
            raise HTTPException(status_code=500, detail="Internal Server Error")


# Method to get live data from the API
@app.get("/api/live_data", summary="Get live data", description="Get live data for a symbol and time interval")
async def get_live_data():
    try:
        data = await bot_CryptoData.get_live_data()
        data = data.to_dict(orient='records')
        return {"data": data}
    except Exception as e:
        logger.error(f"Error getting live data: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
# Websockets for real-time alerts
@app.websocket("/live_data")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await bot_CryptoData.get_live_data()
            
            await websocket.send_json({"data": data})
            await asyncio.sleep(60)
    except WebSocketDisconnect:
        logger.info("Client disconnected")
    except Exception as e:
        logger.error(f"Error in websocket connection: {e}")
    finally:
        await websocket.close()
# Websockets for real-time alerts
@app.websocket("/ws/alerts/{indicator}")
async def websocket_endpoint(websocket: WebSocket, indicator: str):
    await websocket.accept()
    try:
        while True:
            if indicator == 'rsi':
                alerts = await bot.check_rsi()
            elif indicator == 'stochastic_rsi':
                alerts = await bot.check_stochastic_rsi()
            elif indicator == 'macd':
                alerts = await bot.check_macd()
            elif indicator == 'bollinger_bands':
                alerts = await bot.check_bollinger_bands()
            elif indicator == 'ema_200':
                alerts = await bot.check_ema_200()
            elif indicator == 'moving_averages':
                alerts = await bot.check_moving_averages()
            else:
                await websocket.send_json({"error": "Invalid indicator"})
                break

            await websocket.send_json({"alerts": alerts})
            await asyncio.sleep(5)  # Wait (x) seconds before sending the next alert
    except WebSocketDisconnect:
        logger.info("Client disconnected")
    except Exception as e:
        logger.error(f"Error in websocket connection: {e}")
    finally:
        await websocket.close()