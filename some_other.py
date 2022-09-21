In[ ]:
text_rows = table.text.split('\n')
text_rows
 In[ ]:
rows_list = []
for i in range(0,len(text_rows)):
    rows_list.append(text_rows[i].split(' '))
table_df = pd.DataFrame(rows_list[1:-1])
In[ ]:
table_df.columns = ['Month','Date','Year', 'Open', 'High', 'Low', 'Close', 'Adj_Close', 'Volume']
In[ ]:
table_df['Full_date'] = table_df['Month']+ ' ' + table_df['Date']+' ' +table_df['Year']
In[ ]:
table_df.to_csv('PFE.csv')
table_df.to_csv('AMBD.csv')
table_df.to_csv('AZN.csv')
table_df.to_csv('BNTX.csv')
table_df.to_csv('BIO.csv')
table_df.to_csv('HOLX.csv')
table_df.to_csv('JNJ.csv')
table_df.to_csv('LYB.csv')
table_df.to_csv('MRNA.csv')
table_df.to_csv('NVAX.csv')
table_df.to_csv('REGN.csv')
table_df.to_csv('TMO.csv')
table_df.to_csv('WST.csv')
#ABIOMED


#loading the datafile of 'Abiomed' we scraped from yahoo finance
ABMD_df= pd.read_csv('AbiomedABMD.csv')

# In[216]:
#data overview
ABMD_df.head()


# In[217]:

#convert datatype of date from object to datetime
ABMD_df['Date'] = pd.to_datetime(ABMD_df['Date'])


# In[218]:


#looking at all datatypes of the dataframe
ABMD_df.dtypes


# In[219]:


ABMD_df = ABMD_df.drop_duplicates(subset=['Date'])


# In[220]:


#Statistics of all the columns
ABMD_df.describe()


# In[221]:


#plotting all the columns
plt.figure(figsize=(16, 8)) # resizing the plot
cols = ['Open', 'Close', 'High', 'Low', 'Volume']
axes = ABMD_df[cols].plot(figsize=(11, 9), subplots = True)
plt.show()


# In[222]:


import matplotlib.dates as mdates
ax = ABMD_df.plot(x = 'Date', y = 'Close', label = "Closing price of Stock", figsize = (16,8), title = "ABMD Close price")
ax.xaxis.set_major_locator(mdates.MonthLocator(interval = 3)) # to display ticks every 3 months
ax.xaxis.set_major_formatter(mdates.DateFormatter("%m-%Y")) # to set how dates are displayed
plt.legend()


# In[223]:


import matplotlib.dates as mdates
ax = ABMD_df.plot(x = 'Date', y = 'Volume', label = "Volume of the Stock", figsize = (16,8), title = "ABMD Volume column")
ax.xaxis.set_major_locator(mdates.MonthLocator(interval = 3)) # to display ticks every 3 months
ax.xaxis.set_major_formatter(mdates.DateFormatter("%m-%Y")) # to set how dates are displayed
plt.legend()


# In[224]:


#Plotting histogram of Close price
plt.figure(figsize=(10,6))
df_close = ABMD_df['Close']
df_close.plot(style='k.',kind='hist')
plt.title('Hisogram of closing price ABMD')
plt.show()


# In[225]:


#Plotting histogram of Volume column
plt.figure(figsize=(10,6))
df_volume = ABMD_df['Volume']
df_volume.plot(style='k.',kind='hist')
plt.title('Hisogram of Volume ABMD')
plt.show()


# In[226]:

#plotting the stock price with high,low,open and closing price together
import plotly.graph_objects as go

fig = go.Figure(data=go.Ohlc(x=ABMD_df['Date'],
        open=ABMD_df['Open'],
        high=ABMD_df['High'],
        low=ABMD_df['Low'],
        close=ABMD_df['Close']))
fig.show()


# In[227]:


#boxplot of Adj Close
ABMD_df.boxplot(column=['Adj Close'])


# In[228]:


#Correlation matrix
ABMD_df.corr().style.background_gradient(cmap="Blues")


# In[229]:


# Checking decomposition of trend, seasonality and residue of the original time series.
decomposition = seasonal_decompose(ABMD_df['Close'], model='multiplicative', period=30)
fig = plt.figure()  
fig = decomposition.plot()  
fig.set_size_inches(20, 10)
#ASTRAZENECA

# In[181]:


#loading the datafile of 'AstraZeneca' we scraped from yahoo finance
AZN_df= pd.read_csv('AstraZenecaAZN.csv')


# In[182]:


#data overview
AZN_df.head()


# In[183]:


#convert datatype of date from object to datetime
AZN_df['Date'] = pd.to_datetime(AZN_df['Date'])


# In[184]:


#looking at all datatypes of the dataframe
AZN_df.dtypes


# In[185]:


AZN_df = AZN_df.drop_duplicates(subset=['Date'])


# In[186]:


#Statistics of all the columns
AZN_df.describe()


# In[187]:


#plotting all the columns
plt.figure(figsize=(16, 8)) # resizing the plot
cols = ['Open', 'Close', 'High', 'Low', 'Volume']
axes = AZN_df[cols].plot(figsize=(11, 9), subplots = True)
plt.show()


# In[188]:


import matplotlib.dates as mdates
ax = AZN_df.plot(x = 'Date', y = 'Close', label = "Closing price of Stock", figsize = (16,8), title = "AZN Close price")
ax.xaxis.set_major_locator(mdates.MonthLocator(interval = 3)) # to display ticks every 3 months
ax.xaxis.set_major_formatter(mdates.DateFormatter("%m-%Y")) # to set how dates are displayed
plt.legend()


# In[189]:


import matplotlib.dates as mdates
ax = AZN_df.plot(x = 'Date', y = 'Volume', label = "Volume of the Stock", figsize = (16,8), title = "AZN Volume column")
ax.xaxis.set_major_locator(mdates.MonthLocator(interval = 3)) # to display ticks every 3 months
ax.xaxis.set_major_formatter(mdates.DateFormatter("%m-%Y")) # to set how dates are displayed
plt.legend()


# In[190]:


#Plotting histogram of Close price
plt.figure(figsize=(10,6))
df_close = AZN_df['Close']
df_close.plot(style='k.',kind='hist')
plt.title('Hisogram of closing price AZN')
plt.show()


# In[191]:


#Plotting histogram of Volume column
plt.figure(figsize=(10,6))
df_close = AZN_df['Volume']
df_close.plot(style='k.',kind='hist')
plt.title('Hisogram of Volume AZN')
plt.show()


# In[192]:


#plotting the stock price with high,low,open and closing price together
import plotly.graph_objects as go

fig = go.Figure(data=go.Ohlc(x=AZN_df['Date'],
        open=AZN_df['Open'],
        high=AZN_df['High'],
        low=AZN_df['Low'],
        close=AZN_df['Close']))
fig.show()


# In[193]:


#boxplot of Adj Close
AZN_df.boxplot(column=['Adj Close'])


# In[194]:


#Correlation matrix
AZN_df.corr().style.background_gradient(cmap="Blues")


# In[195]:


# Checking decomposition of trend, seasonality and residue of the original time series.
decomposition = seasonal_decompose(AZN_df['Close'], model='multiplicative', period=30)
fig = plt.figure()  
fig = decomposition.plot()  
fig.set_size_inches(20, 10)
#BIONTECH

#loading the datafile of 'BioNTech' we scraped from yahoo finance
BNTX_df= pd.read_csv('BioNTechBNTX.csv')


# In[233]:


#data overview
BNTX_df.head()


# In[234]:


#convert datatype of date from object to datetime
BNTX_df['Date'] = pd.to_datetime(BNTX_df['Date'])


# In[235]:


#looking at all datatypes of the dataframe
BNTX_df.dtypes


# In[236]:


BNTX_df = BNTX_df.drop_duplicates(subset=['Date'])


# In[237]:


#Statistics of all the columns
BNTX_df.describe()


# In[238]:


#plotting all the columns
plt.figure(figsize=(16, 8)) # resizing the plot
cols = ['Open', 'Close', 'High', 'Low', 'Volume']
axes = BNTX_df[cols].plot(figsize=(11, 9), subplots = True)
plt.show()


# In[239]:


import matplotlib.dates as mdates
ax = BNTX_df.plot(x = 'Date', y = 'Close', label = "Closing price of Stock", figsize = (16,8), title = "BNTX Close price")
ax.xaxis.set_major_locator(mdates.MonthLocator(interval = 3)) # to display ticks every 3 months
ax.xaxis.set_major_formatter(mdates.DateFormatter("%m-%Y")) # to set how dates are displayed
plt.legend()


# In[240]:


import matplotlib.dates as mdates
ax = BNTX_df.plot(x = 'Date', y = 'Volume', label = "Volume of the Stock", figsize = (16,8), title = "BNTX Volume column")
ax.xaxis.set_major_locator(mdates.MonthLocator(interval = 3)) # to display ticks every 3 months
ax.xaxis.set_major_formatter(mdates.DateFormatter("%m-%Y")) # to set how dates are displayed
plt.legend()


# In[241]:


#Plotting histogram of Close price
plt.figure(figsize=(10,6))
df_close = BNTX_df['Close']
df_close.plot(style='k.',kind='hist')
plt.title('Hisogram of closing price BNTX')
plt.show()


# In[242]:


#Plotting histogram of Volume column
plt.figure(figsize=(10,6))
df_volume = BNTX_df['Volume']
df_volume.plot(style='k.',kind='hist')
plt.title('Hisogram of Volume BNTX')
plt.show()


# In[243]:


#plotting the stock price with high,low,open and closing price together
import plotly.graph_objects as go

fig = go.Figure(data=go.Ohlc(x=BNTX_df['Date'],
        open=BNTX_df['Open'],
        high=BNTX_df['High'],
        low=BNTX_df['Low'],
        close=BNTX_df['Close']))
fig.show()


# In[244]:


#boxplot of Adj Close
BNTX_df.boxplot(column=['Adj Close'])


# In[245]:


#Correlation matrix
BNTX_df.corr().style.background_gradient(cmap="Blues")


# In[246]:


# Checking decomposition of trend, seasonality and residue of the original time series.
decomposition = seasonal_decompose(BNTX_df['Close'], model='multiplicative', period=30)
fig = plt.figure()  
fig = decomposition.plot()  
fig.set_size_inches(20, 10)
#loading the datafile of 'Hologic' we scraped from yahoo finance
HOLX_df= pd.read_csv('HologicHOLX.csv')


# In[266]:


#data overview
HOLX_df.head()


# In[267]:


#convert datatype of date from object to datetime
HOLX_df['Date'] = pd.to_datetime(HOLX_df['Date'])


# In[268]:


#looking at all datatypes of the dataframe
HOLX_df.dtypes


# In[269]:


HOLX_df = HOLX_df.drop_duplicates(subset=['Date'])


# In[270]:


#Statistics of all the columns
HOLX_df.describe()


# In[271]:


#plotting all the columns
plt.figure(figsize=(16, 8)) # resizing the plot
cols = ['Open', 'Close', 'High', 'Low', 'Volume']
axes = HOLX_df[cols].plot(figsize=(11, 9), subplots = True)
plt.show()


# In[272]:


import matplotlib.dates as mdates
ax = HOLX_df.plot(x = 'Date', y = 'Close', label = "Closing price of Stock", figsize = (16,8), title = "HOLX Close price")
ax.xaxis.set_major_locator(mdates.MonthLocator(interval = 3)) # to display ticks every 3 months
ax.xaxis.set_major_formatter(mdates.DateFormatter("%m-%Y")) # to set how dates are displayed
plt.legend()


# In[273]:


import matplotlib.dates as mdates
ax = HOLX_df.plot(x = 'Date', y = 'Volume', label = "Volume of the Stock", figsize = (16,8), title = "HOLX Volume column")
ax.xaxis.set_major_locator(mdates.MonthLocator(interval = 3)) # to display ticks every 3 months
ax.xaxis.set_major_formatter(mdates.DateFormatter("%m-%Y")) # to set how dates are displayed
plt.legend()


# In[274]:


#Plotting histogram of Close price
plt.figure(figsize=(10,6))
df_close = HOLX_df['Close']
df_close.plot(style='k.',kind='hist')
plt.title('Hisogram of closing price HOLX')
plt.show()


# In[275]:


#Plotting histogram of Volume column
plt.figure(figsize=(10,6))
df_volume = HOLX_df['Volume']
df_volume.plot(style='k.',kind='hist')
plt.title('Hisogram of Volume HOLX')
plt.show()


# In[276]:


#plotting the stock price with high,low,open and closing price together
import plotly.graph_objects as go

fig = go.Figure(data=go.Ohlc(x=HOLX_df['Date'],
        open=HOLX_df['Open'],
        high=HOLX_df['High'],
        low=HOLX_df['Low'],
        close=HOLX_df['Close']))
fig.show()


# In[277]:


#boxplot of Adj Close
HOLX_df.boxplot(column=['Adj Close'])


# In[278]:


#Correlation matrix
HOLX_df.corr().style.background_gradient(cmap="Blues")


# In[279]:


# Checking decomposition of trend, seasonality and residue of the original time series.
decomposition = seasonal_decompose(HOLX_df['Close'], model='multiplicative', period=30)
fig = plt.figure()  
fig = decomposition.plot()  
fig.set_size_inches(20, 10)
#Johnson & Johnson


#loading the datafile of 'Johnson & Johnson' we scraped from yahoo finance
JNJ_df= pd.read_csv('Johnson & JohnsonJNJ.csv')


# In[285]:


#data overview
JNJ_df.head()


# In[286]:


#convert datatype of date from object to datetime
JNJ_df['Date'] = pd.to_datetime(JNJ_df['Date'])


# In[287]:


#looking at all datatypes of the dataframe
JNJ_df.dtypes


# In[288]:


JNJ_df = JNJ_df.drop_duplicates(subset=['Date'])


# In[289]:


#Statistics of all the columns
JNJ_df.describe()


# In[290]:


#plotting all the columns
plt.figure(figsize=(16, 8)) # resizing the plot
cols = ['Open', 'Close', 'High', 'Low', 'Volume']
axes = JNJ_df[cols].plot(figsize=(11, 9), subplots = True)
plt.show()


# In[291]:


import matplotlib.dates as mdates
ax = JNJ_df.plot(x = 'Date', y = 'Close', label = "Closing price of Stock", figsize = (16,8), title = "JNJ Close price")
ax.xaxis.set_major_locator(mdates.MonthLocator(interval = 3)) # to display ticks every 3 months
ax.xaxis.set_major_formatter(mdates.DateFormatter("%m-%Y")) # to set how dates are displayed
plt.legend()


# In[292]:


import matplotlib.dates as mdates
ax = JNJ_df.plot(x = 'Date', y = 'Volume', label = "Volume of the Stock", figsize = (16,8), title = "JNJ Volume column")
ax.xaxis.set_major_locator(mdates.MonthLocator(interval = 3)) # to display ticks every 3 months
ax.xaxis.set_major_formatter(mdates.DateFormatter("%m-%Y")) # to set how dates are displayed
plt.legend()


# In[293]:


#Plotting histogram of Close price
plt.figure(figsize=(10,6))
df_close = JNJ_df['Close']
df_close.plot(style='k.',kind='hist')
plt.title('Hisogram of closing price JNJ')
plt.show()


# In[294]:


#Plotting histogram of Volume column
plt.figure(figsize=(10,6))
df_volume = JNJ_df['Volume']
df_volume.plot(style='k.',kind='hist')
plt.title('Hisogram of Volume JNJ')
plt.show()


# In[295]:


#plotting the stock price with high,low,open and closing price together
import plotly.graph_objects as go

fig = go.Figure(data=go.Ohlc(x=JNJ_df['Date'],
        open=JNJ_df['Open'],
        high=JNJ_df['High'],
        low=JNJ_df['Low'],
        close=JNJ_df['Close']))
fig.show()


# In[296]:


#boxplot of Adj Close
JNJ_df.boxplot(column=['Adj Close'])


# In[297]:


#Correlation matrix
JNJ_df.corr().style.background_gradient(cmap="Blues")


# In[298]:


# Checking decomposition of trend, seasonality and residue of the original time series.
decomposition = seasonal_decompose(JNJ_df['Close'], model='multiplicative', period=30)
fig = plt.figure()  
fig = decomposition.plot()  
fig.set_size_inches(20, 10)
#LyondellBasellIndustries

#loading the datafile of 'Lyondell Basell Industries' we scraped from yahoo finance
LYB_df= pd.read_csv('LyondellBasellIndustriesLYB.csv')


# In[302]:


#data overview
LYB_df.head()


# In[303]:


#convert datatype of date from object to datetime
LYB_df['Date'] = pd.to_datetime(LYB_df['Date'])


# In[304]:


#looking at all datatypes of the dataframe
LYB_df.dtypes


# In[305]:


LYB_df = LYB_df.drop_duplicates(subset=['Date'])


# In[306]:


#Statistics of all the columns
LYB_df.describe()


# In[307]:


#plotting all the columns
plt.figure(figsize=(16, 8)) # resizing the plot
cols = ['Open', 'Close', 'High', 'Low', 'Volume']
axes = LYB_df[cols].plot(figsize=(11, 9), subplots = True)
plt.show()


# In[308]:


import matplotlib.dates as mdates
ax = LYB_df.plot(x = 'Date', y = 'Close', label = "Closing price of Stock", figsize = (16,8), title = "LYB Close price")
ax.xaxis.set_major_locator(mdates.MonthLocator(interval = 3)) # to display ticks every 3 months
ax.xaxis.set_major_formatter(mdates.DateFormatter("%m-%Y")) # to set how dates are displayed
plt.legend()


# In[309]:


import matplotlib.dates as mdates
ax = LYB_df.plot(x = 'Date', y = 'Volume', label = "Volume of the Stock", figsize = (16,8), title = "LYB Volume column")
ax.xaxis.set_major_locator(mdates.MonthLocator(interval = 3)) # to display ticks every 3 months
ax.xaxis.set_major_formatter(mdates.DateFormatter("%m-%Y")) # to set how dates are displayed
plt.legend()


# In[310]:


#Plotting histogram of Close price
plt.figure(figsize=(10,6))
df_close = LYB_df['Close']
df_close.plot(style='k.',kind='hist')
plt.title('Hisogram of closing price LYB')
plt.show()


# In[311]:


#Plotting histogram of Volume column
plt.figure(figsize=(10,6))
df_volume = LYB_df['Volume']
df_volume.plot(style='k.',kind='hist')
plt.title('Hisogram of Volume LYB')
plt.show()


# In[312]:


#plotting the stock price with high,low,open and closing price together
import plotly.graph_objects as go

fig = go.Figure(data=go.Ohlc(x=LYB_df['Date'],
        open=LYB_df['Open'],
        high=LYB_df['High'],
        low=LYB_df['Low'],
        close=LYB_df['Close']))
fig.show()


# In[313]:


#boxplot of Adj Close
JNJ_df.boxplot(column=['Adj Close'])


# In[314]:


#Correlation matrix
LYB_df.corr().style.background_gradient(cmap="Blues")


# In[315]:


# Checking decomposition of trend, seasonality and residue of the original time series.
decomposition = seasonal_decompose(LYB_df['Close'], model='multiplicative', period=30)
fig = plt.figure()  
fig = decomposition.plot()  
fig.set_size_inches(20, 10)
#Moderna

#loading the datafile of 'Moderna' we scraped from yahoo finance
MRNA_df= pd.read_csv('ModernaMRNA.csv')


# In[319]:


#data overview
MRNA_df.head()


# In[320]:


#convert datatype of date from object to datetime
MRNA_df['Date'] = pd.to_datetime(MRNA_df['Date'])


# In[321]:


#looking at all datatypes of the dataframe
MRNA_df.dtypes


# In[322]:


MRNA_df = MRNA_df.drop_duplicates(subset=['Date'])


# In[323]:


#Statistics of all the columns
MRNA_df.describe()


# In[324]:


#plotting all the columns
plt.figure(figsize=(16, 8)) # resizing the plot
cols = ['Open', 'Close', 'High', 'Low', 'Volume']
axes = MRNA_df[cols].plot(figsize=(11, 9), subplots = True)
plt.show()


# In[325]:


import matplotlib.dates as mdates
ax = MRNA_df.plot(x = 'Date', y = 'Close', label = "Closing price of Stock", figsize = (16,8), title = "MRNA Close price")
ax.xaxis.set_major_locator(mdates.MonthLocator(interval = 3)) # to display ticks every 3 months
ax.xaxis.set_major_formatter(mdates.DateFormatter("%m-%Y")) # to set how dates are displayed
plt.legend()


# In[326]:


import matplotlib.dates as mdates
ax = MRNA_df.plot(x = 'Date', y = 'Volume', label = "Volume of the Stock", figsize = (16,8), title = "MRNA Volume column")
ax.xaxis.set_major_locator(mdates.MonthLocator(interval = 3)) # to display ticks every 3 months
ax.xaxis.set_major_formatter(mdates.DateFormatter("%m-%Y")) # to set how dates are displayed
plt.legend()


# In[327]:


#Plotting histogram of Close price
plt.figure(figsize=(10,6))
df_close = MRNA_df['Close']
df_close.plot(style='k.',kind='hist')
plt.title('Hisogram of closing price MRNA')
plt.show()


# In[328]:


#Plotting histogram of Volume column
plt.figure(figsize=(10,6))
df_volume = MRNA_df['Volume']
df_volume.plot(style='k.',kind='hist')
plt.title('Hisogram of Volume MRNA')
plt.show()


# In[329]:


#plotting the stock price with high,low,open and closing price together
import plotly.graph_objects as go

fig = go.Figure(data=go.Ohlc(x=MRNA_df['Date'],
        open=MRNA_df['Open'],
        high=MRNA_df['High'],
        low=MRNA_df['Low'],
        close=MRNA_df['Close']))
fig.show()


# In[330]:


#boxplot of Adj Close
MRNA_df.boxplot(column=['Adj Close'])


# In[331]:


#Correlation matrix
MRNA_df.corr().style.background_gradient(cmap="Blues")


# In[332]:


# Checking decomposition of trend, seasonality and residue of the original time series.
decomposition = seasonal_decompose(MRNA_df['Close'], model='multiplicative', period=30)
fig = plt.figure()  
fig = decomposition.plot()  
fig.set_size_inches(20, 10)
#Novavax

#loading the datafile of 'Novavax' we scraped from yahoo finance
NVAX_df= pd.read_csv('NovavaxNVAX.csv')


# In[337]:


#data overview
NVAX_df.head()


# In[338]:


#convert datatype of date from object to datetime
NVAX_df['Date'] = pd.to_datetime(NVAX_df['Date'])


# In[339]:


#looking at all datatypes of the dataframe
NVAX_df.dtypes


# In[340]:


NVAX_df = NVAX_df.drop_duplicates(subset=['Date'])


# In[341]:


#Statistics of all the columns
NVAX_df.describe()


# In[342]:


#plotting all the columns
plt.figure(figsize=(16, 8)) # resizing the plot
cols = ['Open', 'Close', 'High', 'Low', 'Volume']
axes = NVAX_df[cols].plot(figsize=(11, 9), subplots = True)
plt.show()


# In[343]:


import matplotlib.dates as mdates
ax = NVAX_df.plot(x = 'Date', y = 'Close', label = "Closing price of Stock", figsize = (16,8), title = "NVAX Close price")
ax.xaxis.set_major_locator(mdates.MonthLocator(interval = 3)) # to display ticks every 3 months
ax.xaxis.set_major_formatter(mdates.DateFormatter("%m-%Y")) # to set how dates are displayed
plt.legend()


# In[344]:


import matplotlib.dates as mdates
ax = NVAX_df.plot(x = 'Date', y = 'Volume', label = "Volume of the Stock", figsize = (16,8), title = "NVAX Volume column")
ax.xaxis.set_major_locator(mdates.MonthLocator(interval = 3)) # to display ticks every 3 months
ax.xaxis.set_major_formatter(mdates.DateFormatter("%m-%Y")) # to set how dates are displayed
plt.legend()


# In[345]:


#Plotting histogram of Close price
plt.figure(figsize=(10,6))
df_close = NVAX_df['Close']
df_close.plot(style='k.',kind='hist')
plt.title('Hisogram of closing price NVAX')
plt.show()


# In[346]:


#Plotting histogram of Volume column
plt.figure(figsize=(10,6))
df_volume = NVAX_df['Volume']
df_volume.plot(style='k.',kind='hist')
plt.title('Hisogram of Volume NVAX')
plt.show()


# In[347]:


#plotting the stock price with high,low,open and closing price together
import plotly.graph_objects as go

fig = go.Figure(data=go.Ohlc(x=NVAX_df['Date'],
        open=NVAX_df['Open'],
        high=NVAX_df['High'],
        low=NVAX_df['Low'],
        close=NVAX_df['Close']))
fig.show()


# In[348]:


#boxplot of Adj Close
NVAX_df.boxplot(column=['Adj Close'])


# In[349]:


#Correlation matrix
NVAX_df.corr().style.background_gradient(cmap="Blues")


# In[350]:


# Checking decomposition of trend, seasonality and residue of the original time series.
decomposition = seasonal_decompose(NVAX_df['Close'], model='multiplicative', period=30)
fig = plt.figure()  
fig = decomposition.plot()  
fig.set_size_inches(20, 10)
#Pfizer

#loading the datafile of 'Pfizer' we scraped from yahoo finance
PFE_df= pd.read_csv('PfizerPFE.csv')


# In[199]:


#data overview
PFE_df.head()


# In[200]:


#convert datatype of date from object to datetime
PFE_df['Date'] = pd.to_datetime(PFE_df['Date'])


# In[201]:


#looking at all datatypes of the dataframe
PFE_df.dtypes


# In[202]:


PFE_df = PFE_df.drop_duplicates(subset=['Date'])


# In[203]:


#Statistics of all the columns
PFE_df.describe()


# In[204]:


#plotting all the columns
plt.figure(figsize=(16, 8)) # resizing the plot
cols = ['Open', 'Close', 'High', 'Low', 'Volume']
axes = PFE_df[cols].plot(figsize=(11, 9), subplots = True)
plt.show()


# In[205]:


import matplotlib.dates as mdates
ax = PFE_df.plot(x = 'Date', y = 'Close', label = "Closing price of Stock", figsize = (16,8), title = "PFE Close price")
ax.xaxis.set_major_locator(mdates.MonthLocator(interval = 3)) # to display ticks every 3 months
ax.xaxis.set_major_formatter(mdates.DateFormatter("%m-%Y")) # to set how dates are displayed
plt.legend()


# In[206]:


import matplotlib.dates as mdates
ax = PFE_df.plot(x = 'Date', y = 'Volume', label = "Volume of the Stock", figsize = (16,8), title = "PFE Volume column")
ax.xaxis.set_major_locator(mdates.MonthLocator(interval = 3)) # to display ticks every 3 months
ax.xaxis.set_major_formatter(mdates.DateFormatter("%m-%Y")) # to set how dates are displayed
plt.legend()


# In[207]:


#Plotting histogram of Close price
plt.figure(figsize=(10,6))
df_close = PFE_df['Close']
df_close.plot(style='k.',kind='hist')
plt.title('Hisogram of closing price PFE')
plt.show()


# In[208]:


#Plotting histogram of Volume column
plt.figure(figsize=(10,6))
df_volume = PFE_df['Volume']
df_volume.plot(style='k.',kind='hist')
plt.title('Hisogram of Volume PFE')
plt.show()


# In[209]:


#plotting the stock price with high,low,open and closing price together
import plotly.graph_objects as go

fig = go.Figure(data=go.Ohlc(x=PFE_df['Date'],
        open=PFE_df['Open'],
        high=PFE_df['High'],
        low=PFE_df['Low'],
        close=PFE_df['Close']))
fig.show()


# In[210]:


#boxplot of Adj Close
PFE_df.boxplot(column=['Adj Close'])


# In[211]:


#Correlation matrix
PFE_df.corr().style.background_gradient(cmap="Blues")


# In[212]:


# Checking decomposition of trend, seasonality and residue of the original time series.
decomposition = seasonal_decompose(PFE_df['Close'], model='multiplicative', period=30)
fig = plt.figure()  
fig = decomposition.plot()  
fig.set_size_inches(20, 10)
#RegeneronPharmaceuticals

#loading the datafile of 'Regeneron Pharmaceuticals' we scraped from yahoo finance
REGN_df= pd.read_csv('RegeneronPharmaceuticalsREGN.csv')


# In[356]:


#data overview
REGN_df.head()


# In[357]:


#convert datatype of date from object to datetime
REGN_df['Date'] = pd.to_datetime(REGN_df['Date'])


# In[358]:


#looking at all datatypes of the dataframe
REGN_df.dtypes


# In[359]:


REGN_df = REGN_df.drop_duplicates(subset=['Date'])


# In[360]:


#Statistics of all the columns
REGN_df.describe()


# In[361]:


#plotting all the columns
plt.figure(figsize=(16, 8)) # resizing the plot
cols = ['Open', 'Close', 'High', 'Low', 'Volume']
axes = REGN_df[cols].plot(figsize=(11, 9), subplots = True)
plt.show()


# In[362]:


import matplotlib.dates as mdates
ax = REGN_df.plot(x = 'Date', y = 'Close', label = "Closing price of Stock", figsize = (16,8), title = "REGN Close price")
ax.xaxis.set_major_locator(mdates.MonthLocator(interval = 3)) # to display ticks every 3 months
ax.xaxis.set_major_formatter(mdates.DateFormatter("%m-%Y")) # to set how dates are displayed
plt.legend()


# In[363]:


import matplotlib.dates as mdates
ax = REGN_df.plot(x = 'Date', y = 'Volume', label = "Volume of the Stock", figsize = (16,8), title = "REGN Volume column")
ax.xaxis.set_major_locator(mdates.MonthLocator(interval = 3)) # to display ticks every 3 months
ax.xaxis.set_major_formatter(mdates.DateFormatter("%m-%Y")) # to set how dates are displayed
plt.legend()


# In[364]:


#Plotting histogram of Close price
plt.figure(figsize=(10,6))
df_close = REGN_df['Close']
df_close.plot(style='k.',kind='hist')
plt.title('Hisogram of closing price REGN')
plt.show()


# In[365]:


#Plotting histogram of Volume column
plt.figure(figsize=(10,6))
df_volume = REGN_df['Volume']
df_volume.plot(style='k.',kind='hist')
plt.title('Hisogram of Volume REGN')
plt.show()


# In[366]:


#plotting the stock price with high,low,open and closing price together
import plotly.graph_objects as go

fig = go.Figure(data=go.Ohlc(x=REGN_df['Date'],
        open=REGN_df['Open'],
        high=REGN_df['High'],
        low=REGN_df['Low'],
        close=REGN_df['Close']))
fig.show()


# In[367]:


#boxplot of Adj Close
REGN_df.boxplot(column=['Adj Close'])


# In[368]:


#Correlation matrix
REGN_df.corr().style.background_gradient(cmap="Blues")


# In[369]:


# Checking decomposition of trend, seasonality and residue of the original time series.
decomposition = seasonal_decompose(REGN_df['Close'], model='multiplicative', period=30)
fig = plt.figure()  
fig = decomposition.plot()  
fig.set_size_inches(20, 10)
#ThermoFisherScientific

#loading the datafile of 'ThermoFisher Scientific' we scraped from yahoo finance
TMO_df= pd.read_csv('ThermoFisherScientificTMO.csv')


# In[375]:


#data overview
TMO_df.head()


# In[376]:


#convert datatype of date from object to datetime
TMO_df['Date'] = pd.to_datetime(TMO_df['Date'])


# In[377]:


#looking at all datatypes of the dataframe
TMO_df.dtypes


# In[378]:


TMO_df = TMO_df.drop_duplicates(subset=['Date'])


# In[379]:


#Statistics of all the columns
TMO_df.describe()


# In[380]:


#plotting all the columns
plt.figure(figsize=(16, 8)) # resizing the plot
cols = ['Open', 'Close', 'High', 'Low', 'Volume']
axes = TMO_df[cols].plot(figsize=(11, 9), subplots = True)
plt.show()


# In[381]:


import matplotlib.dates as mdates
ax = TMO_df.plot(x = 'Date', y = 'Close', label = "Closing price of Stock", figsize = (16,8), title = "TMO Close price")
ax.xaxis.set_major_locator(mdates.MonthLocator(interval = 3)) # to display ticks every 3 months
ax.xaxis.set_major_formatter(mdates.DateFormatter("%m-%Y")) # to set how dates are displayed
plt.legend()


# In[382]:


import matplotlib.dates as mdates
ax = TMO_df.plot(x = 'Date', y = 'Volume', label = "Volume of the Stock", figsize = (16,8), title = "TMO Volume column")
ax.xaxis.set_major_locator(mdates.MonthLocator(interval = 3)) # to display ticks every 3 months
ax.xaxis.set_major_formatter(mdates.DateFormatter("%m-%Y")) # to set how dates are displayed
plt.legend()


# In[383]:


#Plotting histogram of Close price
plt.figure(figsize=(10,6))
df_close = TMO_df['Close']
df_close.plot(style='k.',kind='hist')
plt.title('Hisogram of closing price TMO')
plt.show()


# In[384]:


#Plotting histogram of Volume column
plt.figure(figsize=(10,6))
df_volume = TMO_df['Volume']
df_volume.plot(style='k.',kind='hist')
plt.title('Hisogram of Volume TMO')
plt.show()


# In[385]:


#plotting the stock price with high,low,open and closing price together
import plotly.graph_objects as go

fig = go.Figure(data=go.Ohlc(x=TMO_df['Date'],
        open=TMO_df['Open'],
        high=TMO_df['High'],
        low=TMO_df['Low'],
        close=TMO_df['Close']))
fig.show()


# In[386]:


#boxplot of Adj Close
TMO_df.boxplot(column=['Adj Close'])


# In[387]:


#Correlation matrix
TMO_df.corr().style.background_gradient(cmap="Blues")


# In[388]:


# Checking decomposition of trend, seasonality and residue of the original time series.
decomposition = seasonal_decompose(TMO_df['Close'], model='multiplicative', period=30)
fig = plt.figure()  
fig = decomposition.plot()  
fig.set_size_inches(20, 10)
#WestPharmaceuticalServices

#loading the datafile of 'West Pharmaceutical Services' we scraped from yahoo finance
WST_df= pd.read_csv('WestPharmaceuticalServicesWST.csv')


# In[394]:


#data overview
WST_df.head()


# In[395]:


#convert datatype of date from object to datetime
WST_df['Date'] = pd.to_datetime(WST_df['Date'])


# In[396]:


#looking at all datatypes of the dataframe
WST_df.dtypes


# In[397]:


WST_df = WST_df.drop_duplicates(subset=['Date'])


# In[398]:


#Statistics of all the columns
WST_df.describe()


# In[399]:


#plotting all the columns
plt.figure(figsize=(16, 8)) # resizing the plot
cols = ['Open', 'Close', 'High', 'Low', 'Volume']
axes = WST_df[cols].plot(figsize=(11, 9), subplots = True)
plt.show()


# In[400]:


import matplotlib.dates as mdates
ax = WST_df.plot(x = 'Date', y = 'Close', label = "Closing price of Stock", figsize = (16,8), title = "WST Close price")
ax.xaxis.set_major_locator(mdates.MonthLocator(interval = 3)) # to display ticks every 3 months
ax.xaxis.set_major_formatter(mdates.DateFormatter("%m-%Y")) # to set how dates are displayed
plt.legend()


# In[401]:


import matplotlib.dates as mdates
ax = WST_df.plot(x = 'Date', y = 'Volume', label = "Volume of the Stock", figsize = (16,8), title = "WST Volume column")
ax.xaxis.set_major_locator(mdates.MonthLocator(interval = 3)) # to display ticks every 3 months
ax.xaxis.set_major_formatter(mdates.DateFormatter("%m-%Y")) # to set how dates are displayed
plt.legend()


# In[402]:


#Plotting histogram of Close price
plt.figure(figsize=(10,6))
df_close = WST_df['Close']
df_close.plot(style='k.',kind='hist')
plt.title('Hisogram of closing price WST')
plt.show()


# In[403]:


#Plotting histogram of Volume column
plt.figure(figsize=(10,6))
df_volume = WST_df['Volume']
df_volume.plot(style='k.',kind='hist')
plt.title('Hisogram of Volume WST')
plt.show()


# In[404]:


#plotting the stock price with high,low,open and closing price together
import plotly.graph_objects as go

fig = go.Figure(data=go.Ohlc(x=WST_df['Date'],
        open=WST_df['Open'],
        high=WST_df['High'],
        low=WST_df['Low'],
        close=WST_df['Close']))
fig.show()


# In[405]:


#boxplot of Adj Close
WST_df.boxplot(column=['Adj Close'])


# In[406]:


#Correlation matrix
WST_df.corr().style.background_gradient(cmap="Blues")


# In[407]:


# Checking decomposition of trend, seasonality and residue of the original time series.
decomposition = seasonal_decompose(WST_df['Close'], model='multiplicative', period=30)
fig = plt.figure()  
fig = decomposition.plot()  
fig.set_size_inches(20, 10)




















