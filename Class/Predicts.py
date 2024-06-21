import seaborn
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from CryptoData import CryptoData

# Models: Redes neurales recurrentes, Modelos de suavizado exponencial, gradient boosting machine, modelos de series de temporales autoregresivos, redes neuronales convolucionales 1d


def decission_tree(data_time, data_x, data_y):
    data_time = data_time
    x_train, x_test, y_train, y_test = train_test_split(data_x, data_y, test_size=0.2)
    model = DecisionTreeRegressor()
    model.fit(x_train, y_train)
    predict = model.predict(x_test)
    score = model.score(x_test, y_test)
    return score, predict


data = CryptoData.get_historical_price("BTCUSDT", "1h")
data_time = data["time"]
data_x = data[["open", "high", "low", "volume"]]  # variables predictorias
data_y = data["close"]  # variable objetivo

print(decission_tree(data_time, data_x, data_y))
