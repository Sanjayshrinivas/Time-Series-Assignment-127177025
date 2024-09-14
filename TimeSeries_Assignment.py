import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

def load_data(csv_file):
    df = pd.read_csv(csv_file, parse_dates=['Year'], index_col='Year')
    return df

def decompose_time_series(df, column, model='multiplicative', freq=None):
    decomposition = seasonal_decompose(df[column], model=model, period=freq)
    return decomposition

def plot_decomposition(decomposition):
    plt.figure(figsize=(10, 6))

    plt.subplot(311)
    plt.plot(decomposition.observed, label='Observed')
    plt.legend(loc='upper left')

    plt.subplot(312)
    plt.plot(decomposition.trend, label='Trend', color='orange')
    plt.legend(loc='upper left')

    plt.subplot(313)
    plt.plot(decomposition.seasonal, label='Seasonality', color='green')
    plt.legend(loc='upper left')

    plt.tight_layout()
    plt.show()

def analyze_trend_seasonality(csv_file, column, model='multiplicative', freq=None):
    df = load_data(csv_file)
    decomposition = decompose_time_series(df, column, model, freq)
    plot_decomposition(decomposition)


csv_file = "D:\Time Series Analysis\Amazon.csv"
column = 'Billion USD'
analyze_trend_seasonality(csv_file, column, model='multiplicative', freq=12)
