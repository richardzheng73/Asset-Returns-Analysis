import yfinance as yf
import pandas as pd
import numpy as np
class Metrics:
    def __init__(self, d, y):
        self.data = d
        self.years = y

    def time_freq(self):
        weekly = (1 + self.data).resample('W').prod() - 1
        monthly = (1 + self.data).resample('ME').prod() - 1
        yearly = (1 + self.data).resample('YE').prod() - 1
        return weekly, monthly, yearly

    def roi(self,init_investment): #Returns the dollar return given an initial investment
        total_percent_return = (1 + self.data).prod() - 1
        dollar_return = init_investment * total_percent_return
        return dollar_return, total_percent_return

    def annualized_return(self):
        total_growth = (1 + self.data).prod()
        a_r = total_growth**(1/self.years) - 1
        return a_r

    def stand_dev(self):
        annualized_volatility = self.data.std() * np.sqrt(252)
        return annualized_volatility

    def risk_free_rate(self, start_date, end_date):
        rfr = yf.download("^IRX",start = start_date, end = end_date, progress=False, multi_level_index=False)
        return float(rfr['Close'].mean()) / 100

    def sharpe_ratio(self, risk_free):
        annualized_volatility = self.stand_dev()
        annualized_return = self.annualized_return()
        return (annualized_return - risk_free) / annualized_volatility