import pandas_datareader as pdr
import datetime as dt


def get_close_price(ticker_list):
    end = dt.date.today()
    start = end - dt.timedelta(days=1)

    df = pdr.get_data_yahoo(ticker_list, start, end)
    df_close = df['Close'].tail(1).unstack().reset_index()
    df_close.columns = ['Ticker', 'Date', 'Close']

    return df_close
