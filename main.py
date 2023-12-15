import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy.optimize as spop

stocks = np.array(['BTC-USD', 'ETH-USD', 'BNB-USD','XRP-USD', 'SOL-USD', 'ADA-USD', 'STETH-USD', 'AVAX-USD', 'DOGE-USD'])
start = '2021-09-01'
end = '2023-12-15'
fee = 0.05
window = 365
t_threshold = -3
data = pd.DataFrame()
for stock in stocks:
    prices = yf.download(stock, start, end) #берем прайсы с апи яху
    data[stock] = prices['Close'] #take only Close prise column
    data['r' + stock] = np.append(data[stock][1:].reset_index(drop=True)/data[stock][:-1].reset_index(drop=True) - 1, 0) #вычисляем доходность от 2 до предпоследнего дня



print(data)