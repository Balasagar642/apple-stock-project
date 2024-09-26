import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import seaborn as sns
stock_data = yf.Ticker('AAPL')
hist = stock_data.history(period='1d', interval='1m')  # Real-time data for today with 1-minute intervals
print(hist.head())
stock_prices = hist[['Close']].reset_index()
stock_prices['Datetime'] = pd.to_datetime(stock_prices['Datetime'])
fig, ax = plt.subplots()
x_vals = []
y_vals = []

def animate(i):
    latest_data = yf.Ticker('AAPL').history(period='1d', interval='1m')
    x_vals.append(latest_data.index[-1])
    y_vals.append(latest_data['Close'].values[-1])

    ax.clear()
    ax.plot(x_vals, y_vals, color='green')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.title('Real-Time Apple Stock Price')

    ani = FuncAnimation(plt.gcf(), animate, interval=60000,cache_frame_data=False)  # Update every 1 minute
plt.tight_layout()
plt.show()

sns.set_style('darkgrid')


plt.figure(figsize=(10, 6))
sns.lineplot(x=stock_prices['Datetime'], y=stock_prices['Close'])
plt.title('Stock Price Trend')
plt.show()
