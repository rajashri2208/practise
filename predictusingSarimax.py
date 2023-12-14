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
