import matplotlib.pyplot as plt

class Plots:
    def __init__(self, daily_returns):
        self.daily_returns = daily_returns


    def cumulative_returns(self):
        cumulative = (1 + self.daily_returns).cumprod() * 100
        fig, ax = plt.subplots(figsize=(12,5))

        for ticker in cumulative.columns:
            ax.plot(cumulative.index, cumulative[ticker], label = ticker, linewidth = 1.5)
        ax.set_title('Cumulative Returns')
        ax.set_ylabel('Cumulative Value (% of Initial Principle)')
        ax.set_yscale('log')
        ax.set_xlabel('Year')
        ax.legend()
        ax.grid(True, alpha = 0.3)
        plt.tight_layout()
        plt.show()