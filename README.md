# Time-Series-Assignment-127177025
Explanation of the code:
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

• import pandas as pd: This imports the pandas library, which is used for data 
manipulation and analysis. It allows for reading and working with structured data 
(like CSV files).
• import matplotlib.pyplot as plt: This imports matplotlib.pyplot and assigns it 
the alias plt. It's used for creating visualizations, such as plots and graphs.
• from statsmodels.tsa.seasonal import seasonal_decompose: This imports 
the seasonal_decompose function from the statsmodels library. This function 
decomposes a time series into three parts: trend, seasonality, and residuals.

def load_data(csv_file):
 df = pd.read_csv(csv_file, parse_dates=['Year'], index_col='Year')
 return df
• def load_data(csv_file): Defines a function called load_data that takes a file path 
(csv_file) as an argument.
• df = pd.read_csv(csv_file, parse_dates=['Year'], index_col='Year'): Reads the CSV 
file into a DataFrame (df) using pandas.
• parse_dates=['Year']: This converts the 'Year' column into datetime objects.
• index_col='Year': This sets the 'Year' column as the index of the DataFrame, 
making it easier to handle time-series data.
• return df: Returns the DataFrame df containing the loaded data.
def decompose_time_series(df, column, model='multiplicative', freq=None):
 decomposition = seasonal_decompose(df[column], model=model, period=freq)
 return decomposition
• def decompose_time_series(df, column, model='multiplicative', freq=None):
Defines a function to decompose the time series.
• df: The DataFrame containing the time series data.
• column: The specific column (in the DataFrame) containing the time-series 
values.
• model='multiplicative': This specifies the type of decomposition model to use 
(either 'multiplicative' or 'additive'). Multiplicative assumes that variations 
increase over time, while additive assumes a constant variation.
• freq=None: This parameter represents the frequency of the data, e.g., how often 
it repeats (yearly, monthly, etc.). It's set to None by default, but can be passed in.
• decomposition = seasonal_decompose(df[column], model=model, 
period=freq):
• Uses the seasonal_decompose function to break the time series in df[column]
into its observed, trend, seasonality, and residual components.
• The decomposition model (additive or multiplicative) and frequency (period) are 
defined by the parameters.
• return decomposition: Returns the decomposition object containing the trend, 
seasonality, and observed data.
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
• def plot_decomposition(decomposition): Defines a function to plot the time 
series decomposition (observed, trend, and seasonality).
• plt.figure(figsize=(10, 6)): Creates a new figure for plotting with a specified size 
(10 inches wide by 6 inches tall).
First subplot:
• plt.subplot(311): Creates the first subplot (out of three rows). The 311 means: 3 
rows, 1 column, and this is the 1st plot.
• plt.plot(decomposition.observed, label='Observed'): Plots the observed timeseries data.
• plt.legend(loc='upper left'): Adds a legend to the plot in the upper left corner.
Second subplot:
• plt.subplot(312): Creates the second subplot (in the middle row).
• plt.plot(decomposition.trend, label='Trend', color='orange'): Plots the trend data 
in orange.
• plt.legend(loc='upper left'): Adds a legend to the plot.
Third subplot:
• plt.subplot(313): Creates the third and last subplot (in the bottom row).
• plt.plot(decomposition.seasonal, label='Seasonality', color='green'): Plots the 
seasonality data in green.
• plt.legend(loc='upper left'): Adds a legend to the plot.
>plt.tight_layout(): Automatically adjusts the layout of the plots to prevent overlap.
> plt.show(): Displays the plot.
def analyze_trend_seasonality(csv_file, column, model='multiplicative', 
freq=None):
 df = load_data(csv_file)
 decomposition = decompose_time_series(df, column, model, freq)
 plot_decomposition(decomposition)
• def analyze_trend_seasonality(csv_file, column, model='multiplicative', 
freq=None):: This is the main function that orchestrates the entire analysis 
process.
• It takes the path to the CSV file (csv_file), the name of the column containing 
time-series data (column), the type of decomposition model (model), and the 
frequency (freq).
• df = load_data(csv_file): Calls the load_data function to load the CSV data into a 
DataFrame.
• decomposition = decompose_time_series(df, column, model, freq): 
Decomposes the time series using the specified model and frequency.
• plot_decomposition(decomposition): Plots the observed data, trend, and 
seasonality.
csv_file = '/content/Amazon.csv' 
column = 'Billion USD' 
analyze_trend_seasonality(csv_file, column, model='multiplicative', freq=12)
• csv_file = '/content/Amazon.csv': Specifies the path to the CSV file to be 
analyzed.
• column = 'Billion USD': Specifies the name of the column in the CSV that 
contains the time-series data for analysis.
• analyze_trend_seasonality(csv_file, column, model='multiplicative', freq=12): 
Calls the analyze_trend_seasonality function to load the data, decompose the 
time series, and plot the results. Here, the freq=12 assumes monthly data with a 
yearly seasonality
