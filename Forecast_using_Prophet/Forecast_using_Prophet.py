#prepare time series Data
import pandas as pd

# Sample simulated data
data = {
    'month': pd.date_range(start='2023-01-01', periods=12, freq='ME'),
    'score': [1000, 1050, 1100, 1080, 1150, 1200, 1180, 1250, 1300, 1280, 1350, 1400]
}
ts_df = pd.DataFrame(data)
ts_df.head()

#Forecast using Prophet
from prophet import Prophet

# Prepare data in Prophet format
df_prophet = ts_df.rename(columns={'month':'ds', 'score':'y'})

# Initialize model
model = Prophet(yearly_seasonality=True, daily_seasonality=False)
model.fit(df_prophet)

# Make future dataframe (next 6 months)
future = model.make_future_dataframe(periods=6, freq='ME')
forecast = model.predict(future)

# Show forecast
forecast[['ds','yhat','yhat_lower','yhat_upper']].tail()

#plot forecast
import matplotlib.pyplot as plt

fig1 = model.plot(forecast)
plt.title("Airport Score Forecast")
plt.xlabel("Month")
plt.ylabel("Score")
plt.show()

# Optional: Components plot (trend, seasonality)
fig2 = model.plot_components(forecast)
plt.show()

#Arima Forecast
from pmdarima import auto_arima
from statsmodels.tsa.arima.model import ARIMA

# Fit model
model_arima = ARIMA(ts_df['score'], order=(1,1,1))
model_fit = model_arima.fit()

# Forecast next 6 months
forecast_arima = model_fit.forecast(steps=6)
print(forecast_arima)
