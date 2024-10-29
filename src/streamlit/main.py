import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Carregar dados do arquivo CSV
df = pd.read_csv("../src/transfer/resultado_consulta.csv")
df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
df.set_index('data', inplace=True)

# Garantir que a coluna 'valor' seja numérica
df['valor'] = df['valor'].astype(float)

# ----------------------------  ARIMA  -----------------------------------
arima_model = ARIMA(df['valor'], order=(5, 1, 0))
arima_model_fit = arima_model.fit()
arima_forecast = arima_model_fit.forecast(steps=60)

# ----------------------------  SARIMA  ----------------------------------
sarima_model = SARIMAX(df['valor'], order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
sarima_model_fit = sarima_model.fit()
sarima_forecast = sarima_model_fit.get_forecast(steps=60).predicted_mean

# ----------------------------  Random Forest  ----------------------------
df['data_ordinal'] = df.index.map(pd.Timestamp.toordinal)
X = df[['data_ordinal']]
y = df['valor']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

rf_model = RandomForestRegressor(n_estimators=100)
rf_model.fit(X_train, y_train)

future_dates = pd.date_range(df.index[-1], periods=60, freq='M')
future_ordinal = future_dates.map(pd.Timestamp.toordinal).values.reshape(-1, 1)
rf_forecast = rf_model.predict(future_ordinal)

# ----------------------------  Regressão Linear  ----------------------------
linear_model_reg = LinearRegression()
linear_model_reg.fit(X_train, y_train)
linear_forecast = linear_model_reg.predict(future_ordinal)

# ----------------------------  Gráfico Combinado  ----------------------------
plt.figure(figsize=(15, 8))

plt.plot(df.index, df['valor'], label='Histórico', color='green')
plt.plot(future_dates, rf_forecast, label='Previsão Random Forest', color='purple', linestyle='--')
plt.plot(future_dates, linear_forecast, label='Previsão Regressão Linear', color='brown', linestyle='--')
plt.plot(future_dates, arima_forecast, label='Previsão ARIMA', color='red', linestyle='--')
plt.plot(future_dates, sarima_forecast, label='Previsão SARIMA', color='orange', linestyle='--')

plt.xlabel('Ano')
plt.ylabel('Valor')
plt.legend(loc='lower left')
plt.grid(True)
plt.title('Previsão com ARIMA, SARIMA, Random Forest e Regressão Linear')

plt.show()