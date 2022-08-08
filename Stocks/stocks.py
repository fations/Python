import numpy as np
import pandas as pd
import plotly.io as pio
pio.renderers.default = "png"
import yfinance as yf
import plotly.graph_objs as go

class Candle:
    def __init__(self, open, high, low, close):
        self._open = open
        self._high = high
        self._low = low
        self._close = close

    def open(self):
        return self._open
    def high(self):
        return self._high
    def low(self):
        return self._low
    def close(self):
        return self._close
    def print(self):
        print("Open:{} High:{} Low:{} Close:{} \n".format(self._open, self._high, self._low, self._close))
        return()

tickerStrings = ['MSFT', 'AAPL']
df_list = list()
chart_data = list()
for ticker in tickerStrings:
    data = yf.download(ticker, group_by="Ticker", period='3mo', interval='1d')
    data['Ticker'] = ticker
    df_list.append(data)

    #for i in data.index:
    chart_data.append(Candle(data['Open'], data['High'], data['Low'], data['Close']))

    #declare figure
    fig = go.Figure()

    #Create candlestick
    fig.add_trace(go.Candlestick(x=data.index,
                    open=data['Open'],
                    high=data['High'],
                    low=data['Low'],
                    close=data['Close'], name = 'market data'))

    # Add titles
    fig.update_layout(
        title=ticker,
        yaxis_title='Stock Price (USD)')

    #Show
    fig.show()
    #for x in range(len(chart_data)):
    #    chart_data[x].print()

# combine all dataframes into one
df = pd.concat(df_list)

# save to csv
df.to_csv('tickers.csv')



