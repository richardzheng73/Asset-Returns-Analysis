import yfinance as yf
import pandas as pd
from datetime import datetime
class Data:
    def __init__(self, ticker, start_date, end_date):
        self.ticker = ticker if isinstance(ticker, list) else [ticker]
        self.start_date = start_date
        self.end_date = end_date
        self.price_series = None
        self.get_data()

    def get_years(self):
        start_date = datetime.strptime(self.start_date, '%Y-%m-%d').date()
        end_date = datetime.strptime(self.end_date, '%Y-%m-%d').date()
        delta = end_date - start_date
        days = delta.days
        years = days/ 365.25
        return years
    def get_data(self):
        data = yf.download(self.ticker, start=self.start_date, end=self.end_date, auto_adjust=True, multi_level_index=False)
        close = data['Close']
        if isinstance(close, pd.Series):
            close = close.to_frame(name = self.ticker[0])
        self.price_series = close

    def returns(self): #Returns the daily returns
        returns = self.price_series.pct_change().dropna()
        return returns
