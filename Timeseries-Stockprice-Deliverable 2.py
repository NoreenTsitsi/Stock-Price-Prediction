#!/usr/bin/env python
# coding: utf-8

# In[1266]:


from pydoc import classname
import pandas as pd
import numpy as np
import os
from sklearn.feature_extraction.image import grid_to_graph
from sklearn import tree
from sklearn import metrics
from six import StringIO
from IPython.display import Image, display
import pydotplus
import graphviz
from pydotplus import graphviz
import matplotlib.pyplot as plt
from math import sqrt
from sklearn.metrics import mean_squared_error


# In[1267]:


from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import kpss
from statsmodels.tsa.api import ExponentialSmoothing
from statsmodels.tsa.api import SimpleExpSmoothing
from statsmodels.tsa.api import Holt
from statsmodels.tsa.arima_model import ARIMA
from pmdarima.arima import auto_arima


# In[1268]:


PFE_df= pd.read_csv('PfizerPFE.csv')


# In[1269]:


PFE_df.head()


# In[1270]:


PFE_df['Date'] = pd.to_datetime(PFE_df['Date'])


# In[1271]:


PFE_df.dtypes


# In[1272]:


plt.figure(figsize=(10,6))
plt.grid(True)
plt.xlabel('Date')
plt.ylabel('Close Prices')
plt.plot(PFE_df['Close'])
plt.title('PFE closing price')
plt.show()


# In[1273]:


plt.figure(figsize=(10,6))
plt.grid(True)
plt.xlabel('Date')
plt.ylabel('Volume')
plt.plot(PFE_df['Volume'])
plt.title('PFE Volume')
plt.show()


# In[1274]:


plt.figure(figsize=(10,6))
df_close = PFE_df['Close']
df_close.plot(style='k.',kind='hist')
plt.title('Hisogram of closing price PFE')
plt.show()


# In[1275]:


plt.figure(figsize=(10,6))
df_close = PFE_df['Volume']
df_close.plot(style='k.',kind='hist')
plt.title('Hisogram of Volume PFE')
plt.show()


# In[1276]:


import plotly.graph_objects as go

fig = go.Figure(data=go.Ohlc(x=PFE_df['Date'],
        open=PFE_df['Open'],
        high=PFE_df['High'],
        low=PFE_df['Low'],
        close=PFE_df['Close']))
fig.show()


# In[1277]:


# Checking decomposition of trend, seasonality and residue of the original time series.
decomposition = seasonal_decompose(PFE_df['Close'], model='multiplicative', period=30)
fig = plt.figure()  
fig = decomposition.plot()  
fig.set_size_inches(20, 10)


# In[1278]:


#Testing for stationarity using ADF and KPSS Tests.

def stationarity_test(stock_close_price):
    # Calculating rolling mean and rolling standard deviation:
    rolling_mean = stock_close_price.rolling(30).mean()
    rolling_std_dev = stock_close_price.rolling(30).std()
  
    # Plotting the statistics:
    plt.figure(figsize=(24,6))
    plt.plot(rolling_mean, color='blue', label='Rolling Mean')
    plt.plot(rolling_std_dev, color='green', label = 'Rolling Std Dev')
    plt.plot(stock_close_price, color='red',label='Original Time Series')
    plt.legend(loc='best')
    plt.title('Rolling Mean and Standard Deviation')
    
    print("ADF Test:")
    adf_test = adfuller(stock_close_price,autolag='AIC')
    print('Null Hypothesis: Not Stationary')
    print('ADF Statistic: %f' % adf_test[0])
    print('p-value: %f' % adf_test[1])
    print('Critical Values:')
    for key, value in adf_test[4].items():
        print('\t%s: %.3f' % (key, value))

    print("KPSS Test:")
    kpss_test = kpss(stock_close_price, regression='c', nlags=None, store=False)
    print('Null Hypothesis: Stationary')
    print('KPSS Statistic: %f' % kpss_test[0])
    print('p-value: %f' % kpss_test[1])
    print('Critical Values:')
    for key, value in kpss_test[3].items():
        print('\t%s: %.3f' % (key, value))
    
stationarity_test(PFE_df['Close'])


# In[1279]:


#Testing for stationarity of de-trended time series using ADF and KPSS Tests.

# De-trending the time series
PFE_df['Close_Detrend'] = (PFE_df['Close'] - PFE_df['Close'].shift(30))

def stationarity_test(stock_close_price):
    # Calculating rolling mean and rolling standard deviation:
    rolling_mean = stock_close_price.rolling(30).mean()
    rolling_std_dev = stock_close_price.rolling(30).std()
  
    # Plotting the statistics:
    plt.figure(figsize=(24,6))
    plt.plot(rolling_mean, label='Rolling Mean',linewidth=2.0)
    plt.plot(rolling_std_dev, label = 'Rolling Std Dev',linewidth=2.0)
    plt.plot(stock_close_price,label='De-Trended Time Series')
    plt.legend(loc='best')
    plt.title('Rolling Mean and Standard Deviation')
    plt.tight_layout()
    
    print("ADF Test:")
    adf_test = adfuller(stock_close_price,autolag='AIC')
    print('Null Hypothesis: Not Stationary')
    print('ADF Statistic: %f' % adf_test[0])
    print('p-value: %f' % adf_test[1])
    print('Critical Values:')
    for key, value in adf_test[4].items():
        print('\t%s: %.3f' % (key, value))

    print("KPSS Test:")
    kpss_test = kpss(stock_close_price, regression='c', nlags=None, store=False)
    print('Null Hypothesis: Stationary')
    print('KPSS Statistic: %f' % kpss_test[0])
    print('p-value: %f' % kpss_test[1])
    print('Critical Values:')
    for key, value in kpss_test[3].items():
        print('\t%s: %.3f' % (key, value))
    
stationarity_test(PFE_df['Close_Detrend'].dropna())

# PACF Plot
from statsmodels.graphics.tsaplots import plot_pacf
pacf = plot_pacf(PFE_df['Close_Detrend'].dropna(), lags=30)


# In[1280]:


data1=PFE_df[['Date','Close']]


# In[1281]:


data1['Date'] = pd.to_datetime(data1['Date'])


# In[1282]:


data1.head()


# In[1283]:


data1=data1.set_index('Date')


# In[1284]:


data1.head()


# In[1285]:


train_len = 410
train = data1[0 : train_len]
test = data1[train_len : ]


# In[1286]:


# Plotting the train and test sets.
plt.figure(figsize=(10,6))
plt.xlabel('Year')
plt.ylabel('Closing Price')
plt.plot(train, 'red', label='Train data')
plt.plot(test, 'black', label='Test data')
plt.legend()


# In[1287]:


#Simple moving average method
y_hat_sma = data1
ma_window = 12
y_hat_sma['sma_forecast'] = data1['Close'].rolling(ma_window).mean()
y_hat_sma['sma_forecast'][train_len:] = y_hat_sma['sma_forecast'][train_len-1]

plt.figure(figsize=(12,4))
plt.plot(train['Close'], label='Train')
plt.plot(test['Close'], label='Test')
plt.plot(y_hat_sma['sma_forecast'], label='Simple moving average forecast')
plt.legend(loc='best')
plt.title('Simple Moving Average Method')
plt.show()


# In[1288]:


# Calculate RMSE and MAPE

rmse = np.sqrt(mean_squared_error(test['Close'], y_hat_sma['sma_forecast'][train_len:])).round(2)
mape = np.round(np.mean(np.abs(test['Close']-y_hat_sma['sma_forecast'][train_len:])/test['Close'])*100,2)

results = pd.DataFrame({'Method':['Simple moving average forecast'], 'MAPE': [mape], 'RMSE': [rmse]})
results = results[['Method', 'RMSE', 'MAPE']]
results


# In[1289]:


# Simple Exponential Smoothing Method
pred_values = test.copy()
pred_values = pd.DataFrame(pred_values)

Simple_Exponential_df = pd.DataFrame(columns = ['RMS','Smoothing Level'])

from itertools import permutations
perm = permutations(list(np.linspace(0.05,1,num=20)), 1)
for i in list(perm):
  fit_sim_exp = SimpleExpSmoothing(np.asarray(train)).fit(smoothing_level = i[0])
  pred_values['Simple_Exponential'] = fit_sim_exp.forecast(len(test))

  rms = round(sqrt(mean_squared_error(test.values, pred_values.Simple_Exponential)),3)
  Simple_Exponential_df = Simple_Exponential_df.append(other = {'RMS' : rms , 'Smoothing Level' : i[0]} , ignore_index=True)

opt_values = Simple_Exponential_df.loc[Simple_Exponential_df['RMS'] == min(Simple_Exponential_df['RMS']),['Smoothing Level']].values


# Using optimised values from the lists.
fit_sim_exp = SimpleExpSmoothing(np.asarray(train)).fit(smoothing_level = opt_values[0][0])
pred_values['Simple_Exponential'] = fit_sim_exp.forecast(len(test))

plt.figure(figsize=(16,8))
plt.plot(train['Close'], label='Train')
plt.plot(test['Close'], label='Test')
plt.plot(pred_values['Simple_Exponential'], label='Simple_Exponential')
plt.legend(loc='best')
plt.show()

rms_sim_exp = sqrt(mean_squared_error(test_data.values, pred_values.Simple_Exponential))
print("Simple Exponential Smoothing RMS :- " + str(round(rms_sim_exp,3)) + " & Smoothing Level :- "+str(round(opt_values[0][0],3)))


# In[1290]:


rmse = np.sqrt(mean_squared_error(test['Close'], pred_values['Simple_Exponential'])).round(2)
mape = np.round(np.mean(np.abs(test['Close']-pred_values['Simple_Exponential'])/test['Close'])*100,2)

tempResults = pd.DataFrame({'Method':['Simple exponential smoothing forecast'], 'RMSE': [rmse],'MAPE': [mape] })
results = pd.concat([results, tempResults])
results


# In[1292]:


# Holt's Exponential Smoothing Method
holt_linear_df = pd.DataFrame(columns = ['RMS','Smoothing Level','Smoothing Slope'])

from itertools import permutations
perm = permutations(list(np.linspace(0.05,1,num=20)), 2)
for i in list(perm):
  fit_holt = Holt(np.asarray(train)).fit(smoothing_level = i[0],smoothing_slope=i[1])
  pred_values['Holt_linear'] = fit_holt.forecast(len(test))

  rms = round(sqrt(mean_squared_error(test.values, pred_values.Holt_linear)),3)
  holt_linear_df = holt_linear_df.append(other = {'RMS' : rms , 'Smoothing Level' : i[0], 'Smoothing Slope':i[1]} , ignore_index=True)

opt_values = holt_linear_df.loc[holt_linear_df['RMS'] == min(holt_linear_df['RMS']),['Smoothing Level','Smoothing Slope']].values


# Using optimised values from the lists.
fit_holt = Holt(np.asarray(train)).fit(smoothing_level = opt_values[0][0],smoothing_slope=opt_values[0][1])
pred_values['Holt_linear'] = fit_holt.forecast(len(test))

plt.figure(figsize=(16,8))
plt.plot(train['Close'], label='Train')
plt.plot(test['Close'], label='Test')
plt.plot(pred_values['Holt_linear'], label='Holt_linear')
plt.legend(loc='best')
plt.title('Holt Exponential Smoothing')
plt.show()

rms_holt_exp = sqrt(mean_squared_error(test_data.values, pred_values.Holt_linear))
print("Holt’s Exponential Smoothing RMS :- " + str(round(rms_holt_exp,3)) + " & Smoothing Level :- "+str(round(opt_values[0][0],3)) + " & Smoothing Slope :- "+str(round(opt_values[0][1],3)))


# In[1293]:


rmse = np.sqrt(mean_squared_error(test['Close'], pred_values['Holt_linear'])).round(2)
mape = np.round(np.mean(np.abs(test['Close']-pred_values['Holt_linear'])/test['Close'])*100,2)

tempResults = pd.DataFrame({'Method':['Holt\'s exponential smoothing method'], 'RMSE': [rmse],'MAPE': [mape] })
results = pd.concat([results, tempResults])
results = results[['Method', 'RMSE', 'MAPE']]
results


# In[1294]:


#Holt Winters' additive method with trend and seasonality
y_hat_hwa = test.copy()
model = ExponentialSmoothing(np.asarray(train['Close']) ,seasonal_periods=12 ,trend='add', seasonal='add')
model_fit = model.fit(optimized=True)
print(model_fit.params)
y_hat_hwa['hwa_forecast'] = model_fit.forecast(len(test))

plt.figure(figsize=(12,4))
plt.plot( train['Close'], label='Train')
plt.plot(test['Close'], label='Test')
plt.plot(y_hat_hwa['hwa_forecast'], label='Holt Winters\'s additive forecast')
plt.legend(loc='best')
plt.title('Holt Winters\' Additive Method')
plt.show()


# In[1295]:


rmse = np.sqrt(mean_squared_error(test['Close'], y_hat_hwa['hwa_forecast'])).round(2)
mape = np.round(np.mean(np.abs(test['Close']-y_hat_hwa['hwa_forecast'])/test['Close'])*100,2)

tempResults = pd.DataFrame({'Method':['Holt Winters\' additive method'], 'RMSE': [rmse],'MAPE': [mape] })
results = pd.concat([results, tempResults])
results = results[['Method', 'RMSE', 'MAPE']]
results


# In[1296]:


#Holt Winter's multiplicative method with trend and seasonality
y_hat_hwm = test.copy()
model = ExponentialSmoothing(np.asarray(train['Close']) ,seasonal_periods=12 ,trend='add', seasonal='mul')
model_fit = model.fit(optimized=True)
print(model_fit.params)
y_hat_hwm['hwm_forecast'] = model_fit.forecast(len(test))

plt.figure(figsize=(12,4))
plt.plot( train['Close'], label='Train')
plt.plot(test['Close'], label='Test')
plt.plot(y_hat_hwm['hwm_forecast'], label='Holt Winters\'s mulitplicative forecast')
plt.legend(loc='best')
plt.title('Holt Winters\' Mulitplicative Method')
plt.show()


# In[1297]:


rmse = np.sqrt(mean_squared_error(test['Close'], y_hat_hwm['hwm_forecast'])).round(2)
mape = np.round(np.mean(np.abs(test['Close']-y_hat_hwm['hwm_forecast'])/test['Close'])*100,2)

tempResults = pd.DataFrame({'Method':['Holt Winters\' multiplicative method'], 'RMSE': [rmse],'MAPE': [mape] })
results = pd.concat([results, tempResults])
results = results[['Method', 'RMSE', 'MAPE']]
results


# In[1298]:


# Auto ARIMA Method
arima_model = auto_arima(train,
                      start_p=1, start_q=1,
                      max_p=5, max_q=5,
                      test='adf',        
                      trace=True,
                      alpha=0.05,
                      scoring='mse',
                      suppress_warnings=True,
                      seasonal = False
                      )

# Fitting the final model with the order
fitted_model = arima_model.fit(train) 
print(fitted_model.summary())

# Forecasting the values.
forecast_values = fitted_model.predict(len(test), alpha=0.05) 
fcv_series = pd.Series(forecast_values[0], index=test.index)

#Plotting the predicted stock price and original price.
plt.figure(figsize=(12,5), dpi=100)
plt.plot(train['Close'], label='training')
plt.plot(test['Close'], label='Actual Stock Price')
plt.plot(fcv_series,label='Predicted Stock Price')
plt.title('Auto ARIMA - Stock Price Prediction')
plt.xlabel('Time')
plt.ylabel('Close Price')
plt.legend(loc='upper left', fontsize=8)
plt.show()

# Evaluating the model by calculating RMSE.
rms_auto_arima = sqrt(mean_squared_error(test_data.values, fcv_series))
print("Auto-Arima RMSE :- " + str(round(rms_auto_arima,3)))


# In[1299]:


# Plotting the diagnostics of the fiited model.
arima_model.plot_diagnostics(figsize=(15,8))
plt.show()


# In[1300]:


rmse = np.sqrt(mean_squared_error(test_data.values, fcv_series)).round(2)
mape = np.round(np.mean(np.abs(test['Close']-fcv_series[test.index.min():])/test['Close'])*100,2)
tempResults = pd.DataFrame({'Method':['Autoregressive integrated moving average (ARIMA) method'], 'RMSE': [rmse],'MAPE': [mape] })
results = pd.concat([results, tempResults])
results = results[['Method', 'RMSE', 'MAPE']]
results


# #### Predicting Future stock price using Holts exponential Smoothing & Simple Exponential Smoothing

# In[ ]:


#Creating future dates 
y_new_pred = pd.DataFrame(pd.date_range(datetime.datetime.strptime("2022-03-10","%Y-%m-%d"), periods=103),columns=['Date'])
y_new_pred.set_index('Date',inplace=True)


# In[ ]:


#Holts exponential Smoothing
holt_linear_df = pd.DataFrame(columns = ['RMS','Smoothing Level','Smoothing Slope'])

from itertools import permutations
perm = permutations(list(np.linspace(0.05,1,num=20)), 2)
for i in list(perm):
  fit_holt = Holt(np.asarray(train['Close'])).fit(smoothing_level = i[0],smoothing_slope=i[1])
  pred_values = fit_holt.forecast(len(test))

  rms = round(sqrt(mean_squared_error(test.values, pred_values)),3)
  holt_linear_df = holt_linear_df.append(other = {'RMS' : rms , 'Smoothing Level' : i[0], 'Smoothing Slope':i[1]} , ignore_index=True)

opt_values = holt_linear_df.loc[holt_linear_df['RMS'] == min(holt_linear_df['RMS']),['Smoothing Level','Smoothing Slope']].values


# Using optimised values from the lists.
fit_holt = Holt(np.asarray(train['Close'])).fit(smoothing_level = opt_values[0][0],smoothing_slope=opt_values[0][1])
pred_values = fit_holt.forecast(len(test))


# In[ ]:


#Predicting for 103 days from the current date - Holts exponential Smoothing
y_new_pred['Holt_linear'] = fit_holt.forecast(103)


# In[ ]:


plt.figure(figsize=(16,8))
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.plot(data1['Close'], label='Historic Stock price')
plt.plot(y_new_pred['Holt_linear'], label='Prdicted Future Stock price')
plt.legend(loc='best')
plt.title('Pfizer - Future Stock price prediction   using   [Model-Holt Exponential Smoothing]')
plt.show()


# In[ ]:


#Simple Exponential Smoothing ONLY for Hologic and RegeneronPharmaceuticals
fit_sim_exp = SimpleExpSmoothing(np.asarray(train['Close'])).fit(smoothing_level = 0.1)
pred_values= fit_sim_exp.forecast(len(test))


# In[ ]:


#Predicting for 103 days from the current date - Simple Exponential Smoothing ONLY for Hologic and RegeneronPharmaceuticals
y_new_pred['Holt_linear'] = fit_sim_exp.forecast(103)


# In[ ]:


plt.figure(figsize=(16,8))
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.plot(data1['Close'], label='Historic Stock price')
plt.plot(y_new_pred['Holt_linear'], label='Prdicted Future Stock price')
plt.legend(loc='best')
plt.title('Hologic - Future Stock price prediction   using   [Best model-Simple Exponential Smoothing]')
plt.show()

