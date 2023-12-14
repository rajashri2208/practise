from statsmodels.tsa.statespace.sarimax import SARIMAX
import matplotlib.pyplot as plt

# Assuming 'time_series_data' contains both time series and calendar covariates as previously described

# Create a time series index
time_series_data = time_series_data.set_index('Date')

# Fit SARIMA model
model = SARIMAX(time_series_data['Count'], order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
results = model.fit()

# Forecast next 10 days
forecast = results.get_forecast(steps=10)

# Extract forecasted values
forecast_values = forecast.predicted_mean
forecast_index = pd.date_range(start=time_series_data.index.max() + pd.Timedelta(days=1), periods=10)

# Create a DataFrame for the forecasted values
forecast_df_sarima = pd.DataFrame({
    'Date': forecast_index,
    'Forecast': forecast_values.values
})






#-------------------------------------


from statsmodels.tsa.statespace.sarimax import SARIMAX
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generating time series data
start_date = '2022-01-01'
end_date = '2023-12-31'
date_range = pd.date_range(start=start_date, end=end_date)
count_data = np.random.randint(1, 100, size=len(date_range))

time_series_data = pd.DataFrame({
    'Date': date_range,
    'Count': count_data
})

# Generating calendar covariate data
calendar_data = pd.DataFrame({
    'Date': date_range,
    'Day_of_Week': date_range.dayofweek,
    'Month': date_range.month,
    'Year': date_range.year,
    'Day_of_Month': date_range.day,
    'Day_of_Year': date_range.dayofyear
})

# Merge time series data with calendar covariates
merged_data = pd.merge(time_series_data, calendar_data, on='Date')

# Create a time series index
merged_data = merged_data.set_index('Date')

# Fit SARIMAX model with calendar covariates
model = SARIMAX(merged_data['Count'], exog=merged_data[['Day_of_Week', 'Month', 'Year', 'Day_of_Month', 'Day_of_Year']],
                order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
results = model.fit()

# Forecast next 10 days
future_dates = pd.date_range(start=time_series_data['Date'].max() + pd.Timedelta(days=1), periods=10)

exog_future = pd.DataFrame({
    'Day_of_Week': future_dates.dayofweek,
    'Month': future_dates.month,
    'Year': future_dates.year,
    'Day_of_Month': future_dates.day,
    'Day_of_Year': future_dates.dayofyear
}, index=future_dates)

forecast = results.get_forecast(steps=10, exog=exog_future)

# Extract forecasted values
forecast_values = forecast.predicted_mean
forecast_index = pd.date_range(start=merged_data.index.max() + pd.Timedelta(days=1), periods=10)

# Create a DataFrame for the forecasted values
forecast_df_sarimax = pd.DataFrame({
    'Date': forecast_index,
    'Forecast': forecast_values.values
})

# Print forecast for the next 10 days
print(forecast_df_sarimax)

# Plot the forecast
plt.figure(figsize=(10, 6))
plt.plot(merged_data.index, merged_data['Count'], label='Original data')
plt.plot(forecast_index, forecast_values, label='Forecast', color='red')
plt.xlabel('Date')
plt.ylabel('Count')
plt.title('SARIMAX Forecast for Next 10 Days with Calendar Covariates')
plt.legend()
plt.show()

# Print forecast for the next 10 days
print(forecast_df_sarima)

# Plot the forecast
plt.figure(figsize=(10, 6))
plt.plot(time_series_data.index, time_series_data['Count'], label='Original data')
plt.plot(forecast_index, forecast_values, label='Forecast', color='red')
plt.xlabel('Date')
plt.ylabel('Count')
plt.title('SARIMA Forecast for Next 10 Days')
plt.legend()
plt.show()
