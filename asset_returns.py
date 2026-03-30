import yfinance as yf
import pandas as pd

class AssetReturns:
    def __init__(self, ticker, start_date):
        self.ticker = ticker
        self.start_date = start_date
        self.prices = None
        self.get_data()


    def get_data(self):
        data = yf.download(self.ticker, start = self.start_date)
        self.prices = data['Close'].squeeze()

    def returns(self): #Returns the daily, weekly, monthly, and yearly returns as a pandas dataframe
        returns_df = pd.Series({
            "daily": self.prices.pct_change().mean(),
            "weekly": self.prices.resample('W').ffill().pct_change().mean(),
            "monthly": self.prices.resample('ME').ffill().pct_change().mean(),
            "yearly": self.prices.resample('YE').ffill().pct_change().mean()
        })
        return returns_df

    def calculate_roi(self,init_investment): #Returns the dollar return given an initial investment
        start_price = float(self.prices.iloc[0])
        end_price = float(self.prices.iloc[-1])
        percent_return = (end_price - start_price) / start_price
        total_return = init_investment * (1 + percent_return)
        return total_return