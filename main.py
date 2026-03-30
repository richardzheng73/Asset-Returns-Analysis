from asset_returns import AssetReturns

ticker_input = input("Enter a ticker: \n").upper()
start_date = input("Enter a start date: (In this format: yyyy-mm-dd)\n")

asset_returns = AssetReturns(ticker_input, start_date)
pct_returns = asset_returns.returns()

investment = float(input("How much do you want to invest? $"))
roi = asset_returns.calculate_roi(investment)

print(f"Your total ROI: ${round(roi, 2)}")
print(f"Average Daily Return: {round(pct_returns['daily'] * 100, 2)}%")
print(f"Average Weekly % Return: {round(pct_returns['weekly'] * 100, 2)}%")
print(f"Average Monthly % Return: {round(pct_returns['monthly'] * 100, 2)}%")
print(f"Average Yearly % Return: {round(pct_returns['yearly'] * 100, 2)}%")