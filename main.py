from data import Data
from metrics import Metrics
from plots import Plots
ticker_input = input("Enter ticker(s) Separated by a space: ").upper().split()
start_date = input("Enter a start date (yyyy-mm-dd): ")
end_date = input("Enter a end date (yyyy-mm-dd): ")
initial_investment = float(input("Enter an initial investment: "))

# Initialize classes
data_obj = Data(ticker_input, start_date, end_date)
daily_returns = data_obj.returns()

plots = Plots(daily_returns)
temp_metrics = Metrics(daily_returns.iloc[0], data_obj.get_years())
risk_free = temp_metrics.risk_free_rate(start_date, end_date)

for ticker in daily_returns.columns:
    col = daily_returns[ticker]
    metrics = Metrics(col, data_obj.get_years())
    risk_free = metrics.risk_free_rate(start_date, end_date)
    print("-"*30)
    print(f"Ticker: {ticker}")
    print("-"*30)
    print(f"Annualized Returns: {metrics.annualized_return():.2%}")
    print(f"Annualized Volatility: {metrics.stand_dev():.2%}")
    print(f"Sharpe Ratio: {metrics.sharpe_ratio(risk_free):.2f}")
plots.cumulative_returns()

# print("-" * 30)
# print(f"Daily returns mean: {daily_returns.mean():.4%}")
# print(f"Weekly returns mean: {weekly.mean():.4%}")
# print(f"Monthly returns mean: {monthly.mean():.4%}")
# print(f"Yearly returns mean: {yearly.mean():.4%}")
# print("-" * 30)
#
# dollar_roi, percent_roi = metrics.roi(initial_investment)
# print(f"Cumulative % returns: {percent_roi:.2%}")
# print(f"Cumulative $ returns: ${dollar_roi:.2f}")
# print(f"Annualized Returns: {metrics.annualized_return():.2%}")
# print(f"Annualized Volatility: {metrics.stand_dev():.2%}")
# print(f"Sharpe Ratio: {sharpe_ratio:.2f}")