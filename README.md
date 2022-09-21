[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=7281620&assignment_repo_type=AssignmentRepo)
# Stock Market Analysis Project



## Executive Summary

A stock (also known as equity) is a security that represents the ownership of a fraction of a corporation. (Hayes, 2021). The stock market was formed in the 16th and 17th centuries in Europe with the main trading hubs in Antwerp, Amsterdam, and London. The stock markets started appearing in the United States in the 18th century with the first stock exchange being the Philadelphia Stock Exchange (PHLX) followed by the New York Stock Exchange (NYSE). The stock market allows individual investors to buy and sell ownership in different companies with the hopes of making a profit depending on how the company performs. The stock exchange is a way to make money, but it is very volatile and hard to predict the price movements of the stocks. Investors have gone through the roller coaster rides of the Great Depression, the 2008 Recession, and recently the COVID-19 Recession. With so much uncertainty in the markets, investors need ways to help reduce their losses and predict the prices of the stock. The accurate prediction of share price movement will lead to more profit investors can make (Cheng & Alzazah, 2020).

This project will use different machine learning models to come as close as possible to predicting stock prices for different stocks. We will be using data for 13 health and pharmaceutical companies and focusing on performance since COVID-19 brought havoc to the world in 2020. During this time stock prices of some companies soared and experienced high gains, especially healthcare, entertainment, coordination, and remodeling industries. We decided to focus on one industry (healthcare) because it had the most companies represented in the top 50 companies that showed an increase in stock value during COVID-19. The data used for the project was obtained from finance.yahoo.com. We will be using time series forecasting and other machine learning models to predict the future trend of the stock prices of these 13 companies. The team members who got together to bring this project together are Tejaswi Maruthi, Heng Yi, Noreen Chihora and Sanjam Patwalia.

## Statement of Scope

This research focuses on helping stock market investors to accurately predict stock prices using different machine learning methods. The stock market is extremely hard to predict because of the many varied factors that affect the prices of the stock. Some of these factors include current events/news (like COVID-19 or Russia-Ukraine war), supply and demand, how the company is performing, the psychology of the investors etc. COVID-19 is still present, but less prevalent than 2020 when it started. We collected data from 13 healthcare/pharmaceutical companies that have been performing well during the COVID-19 pandemic and are in the top 50. These companies are Pfizer, BioNTech, Moderna, Johnson and Johnson, AstraZeneca, Regeneron Pharmaceuticals, LyondellBasell Industries, Novavax, ThermoFisher Scientific, Hologic Inc, Bio-Rad Laboratories, West Pharmaceutical Services and Abiomed. Stock data is a time series of data captured daily when the stock market is open, and that can be used to make future price predictions based on historical data. We scraped data from finance.yahoo.com for all the companies in the data ranges of our choice. Each company has 512 records of data from 03/02/2020 to 03/02/2022. This amounts to over 6500 records accumulatively that will be used for this project. The objectives of this project are as follows:

Analyze stock price fluctuations based on the collected data.

To create a machine learning model that looks at stock prices since COVID-19 hit and best predicts the future prices of stock.

We are hoping that in the end, this model will be applicable to different stocks and assist investors in making informed decisions when investing in the stock market, making minimal losses if any. We will also be able to see companies that were affected positively or negatively by this pandemic.

Target Variables
Target variable: Close

Predictor variables: Date, Open, High, Low, Volume, Adj Close

## Project Schedule

![p1](/assets/p1.PNG)

## Data Preparation

We used Python to do all the analysis presented in this project. The processes below were done for all the companies and the results were all found to be the same for all the companies. Data preparation is important because we need clean, mistake-free data to produce effective models that can be used by investors and produce more accurate results outside of the test and validation data. 

* [placeholder.csv](data/placeholder.csv)
* [some_code.py](code/some_code.py)
* [some_other.py](code/some_other.py)

 Sample Data

+ Date: Refers to the date that the stock was traded on the market

+ Open: This is the stock price when the markets open at 9:30am EST

+ Close: This is the stock price when the markets close at 4pm EST
 
+ Low: This is the highest stock price for the day 
 
+ High: This is the highest stock price for the day 
 
+ Volume: The physical number of stocks traded each day

+ Adj Close: The closing price after adjustments for all applicable corporate actions e.g., split or dividend payouts.

![p2](/assets/p2.PNG)

![p3](/assets/p3.PNG)

The data was all scraped from finance.yahoo.com. At the beginning there were 513 records of data and 7 variables shown above for each of the companies that we are exploring. One of the records was duplicated. We removed one of the duplicated records from our data for each company. 

The dates of the stock prices range from 03/02/2020 to 03/10/2022 for all the companies. Our data starts from March 2nd because the 1st was on a Sunday and the markets are open Monday to Friday.

![p4](/assets/p4.PNG)

 Data Types

The figure below shows the data types of the data that was downloaded from the yahoo finance website. The data types are the same for all the companies. All the columns except for Date have numerical data. 

![p5](/assets/p5.PNG)

In addition to this we checked for missing values, and outliers. We had no missing values in the data and some companies which had outliers in the ‘Close’ variable namely Pfizer, AstraZeneca and Hologic. We left the outliers in the data because they help us to understand the data and create a more accurate time series model. We also transformed the date to the correct data type. We created a correlation matrix to see if there is any correlation in our data. We do not want multicollinearity between the variables because it will reduce precision in our models. Lastly, we looked at descriptive statistics for numerical data and decomposition of trend, seasonality, and residue of the original time series. This allows us to breakdown the closing price of the stock and remove some noise in the data so we can potentially see some sub trends in the data for each company. After this preparation and getting to know the data, we can proceed with time series analysis and machine learning modeling. 

### Data Access

Data for this project was obtained from finance.yahoo.com. The data was scraped before it was analyzed, cleaned, and transformed. Below are links to each stock’s specific webpage. We explored data for the 13 companies between 03/01/2020 and 03/10/2022. We saved the scraped data in 13 different csv files. We chose yahoo finance because it is a reputable website that has been providing investors with financial information for stocks of their choosing for decades. The website gives investors more than just historical data but company profiles, financials, conversations, statistics etc. This information will be helpful if we also decide to take our project a step further. 

| COMPANY | STOCK TICKER | WEBSITE |
|:---:|:---:|:---:|
| Pfizer | PFE | PFE Historical Data |
| BioNTech | BNTX | BNTX Historical Data |
| Moderna | MRNA | MRNA Historical Data | 
| Johnson & Johnson | JNJ | JNJ Historical Data |
| AstraZeneca | AZN | AZN Historical Data |
| Regeneron Pharmaceuticals, Inc  | REGN | REGN Historical Data |
| LyondellBasell Industries | LYB | LYB Historical Data |
| Novavax | NVAX | NVAX Historical Data |
| ThermoFisher Scientific, Inc | TMO | TMO Historical Data |
| Hologic, Inc | HOLX | HOLX Historical Data |
| Bio-Rad Laboratories | BIO | BIO Historical Data |
| West Pharmaceuticals Services, Inc  | WST | WST Historical Data |
| Abiomed, Inc | ABMD | ABMD Historical Data |

### Data Cleaning

Missing Data

As shown below, all the variables do not have any missing data. No missing data handling procedures were performed.

![p7](/assets/p7.PNG)

Duplicate Rows

We also checked for duplication to make sure no rows were duplicated. Date is the only variable that is unique, so we used it to check for duplication. In the all the datasets, there was one duplication shown below. One row of data was repeated twice. All the companies repeated the same row of data, and the same process was performed to clean the data for analysis. 

![p8](/assets/p8.PNG)

After looking at the data for all the 13 companies that we will be analyzing, their duplicated row was for 03/10/2022 data as seen below. To make sure this duplicate did not have any effect on the analysis we decided to remove one of the rows that was duplicated. The data is almost the same, so we deleted the last row. Now our data has 512 rows and the same 7 rows for all the companies. 

![p9](/assets/p9.PNG)

Outlier Detection

Outliers can affect the outcome and performances of machine learning models, however with the unpredictability of the stock market, outliers in data are expected. We checked to see how many outliers we had for the target variable ‘Close’, for each company. Outliers are quite common in Stock analysis. We decided not to remove the outliers because they show days with the biggest profits or losses. Once we start modeling, we might consider taking log to normalize the data to avoid having bad models. Below is an example of the outliers we had for one of the companies. The same process was repeated for all the other companies. 

We started by checking to see if there were any obvious outliers by looking at the histogram. We noticed that for all the companies, the data was not normally distributed, differing in skewedness and shape. For JNJ we can see potential outliers for data close to $110 in stock price. 

![p10](/assets/p10.PNG)

Next, we checked the box plot for a visualization of outliers, to confirm what we see on the histogram. There are some outliers on the lower end of the stock pricing spectrum. We checked to see what the outliers were, considering values greater than 3 standard deviations from the mean. 

![p11](/assets/p11.PNG)

We can see for JNJ we have 4 outliers in March 2020 on the 20th, 23rd, 24th and 25th. 

We repeated the same process for all the companies and below is a summary. 

| COMPANY	| OUTLIERS PRESENT	| NUMBER OF OUTLIERS |
|:---:|:---:|:---:|
| Pfizer	| Yes	| 1 |
| BioNTech	| No	| 0 |
| Moderna	| No	| 0 |
| AstraZeneca	| Yes	| 8 |
| Regeneron Pharmaceuticals |	No |	0 |
| LyondellBasell	| No |	0 |
| Novavax	| No	| 0 |
| ThermoFisher Scientific |	No |	0 |
| Hologic |	Yes |	11 |
| Bio-Rad |	No |	0 |
| West Pharmaceutical Services |	No	| 0 |
| Abiomed	| No	| 0 |

### Data Transformation

Date Type Transformation

During this stage, only one variable needed to be transformed. As seen in the Data Preparation section, the variable ‘Date’, was an object and we decided to change it to a date format to use it to gain insightful information from our data and use it for predictive modeling. After the transformation shown below, Date now has the correct data type attached to it. This process was done for all the 13 companies’ data. 

![p13](/assets/p13.PNG)

### Data Reduction

We can see that there is a high correlation between the variables, so we will be using only the column ‘Close’ for prediction using time series. We did not see the need to reduce the data to remove the other variables because when we perform the time series analysis, we will be able to choose ‘Close’ which will be the only variable that will be used to predict the price of the stock. Once we start using other modelling methods, we will decide on how we want to treat the variables. 

![p14](/assets/p14.PNG)

### Data Consolidation

After scraping, all the data for the 13 companies was saved in 13 separate csv files. We did not need to consolidate the separate files due to the nature of our project. The data for the different companies must be kept separate because each company's stock prices are different, and consolidation would change the meaning in the data, and we would not be able to produce a model that works in the real world. 

### Data Dictionary

The data dictionary applies to all companies. 

| ATTRIBUTE NAME	| DATA TYPE	| SOURCE |	EXAMPLE |DATA| 
|:---:|:---:|:---:|:---:|:---:|
| Date	| datetime64[ns] |	finance.yahoo.com	| 2020-03-02 | [placeholder.csv](data/placeholder.csv) |
| Open	| float64 |	finance.yahoo.com	| 32.172676 | [placeholder.csv](data/placeholder.csv) |
| High	| float64 |	finance.yahoo.com |	33.159393 | [placeholder.csv](data/placeholder.csv) |
| Low	| float64	| finance.yahoo.com	| 31.736242 | [placeholder.csv](data/placeholder.csv) |
| Close	| float64	| finance.yahoo.com	| 33.092979 | [placeholder.csv](data/placeholder.csv) |
| Adj Close	| float64	| finance.yahoo.com	| 30.676327 | [placeholder.csv](data/placeholder.csv) |
| Volume	| Int64 |	finance.yahoo.com	| 42034469 | [placeholder.csv](data/placeholder.csv) |

| ATTRIBUTE NAME	| DESCRIPTION |
|:---:|:---:|
| Date | Refers to the date that the stock was traded on the market | 
| Open	| This is the stock price when the markets open at 9:30am EST |
| High	| This is the stock price when the markets close at 4pm EST |
| Low	| This is the highest stock price for the day |
| Close	| This is the highest stock price for the day |
| Adj Close	| The closing price after adjustments for all applicable corporate actions e.g., split or dividend payouts |
| Volume	| Measure of the total turnover of shares traded in a stock or contracts traded in futures or options. |
| ATTRIBUTE NAME	| PURPOSE |
| Date |	Used to organize the data in a time ordered fashion, to look at the seasonality of the stock price using time series analysis |
| Open, High, Low, Close, Adj Close |	These column values assist in trend analysis of the stock price |
| Volume	| This column helps us in looking at the total shares traded for a particular stock and to compare the volume across stocks |

## Descriptive Statistics and Analysis

With all the data sets craped and the preparation and transformations done, we will be exploring the data sets for all the companies to get some insight before we do some modeling. 

Pfizer

Column Statistics
Below is a table showing a summary of the statistics for all the columns in the Pfizer data frame. 

|   |	Open	| High	| Low	| Close	| Adj Close |	Volume |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Count |	512	| 512	| 512 |	512 |	512	| 512 |
| Mean	| 39.951991	| 40.410697	| 39.469111 |	39.945478	| 38.617181	| 34027790 |
| Standard | Deviation	| 7.051779	| 7.208739	| 6.925717 |	7.086688	| 7.687158 |	18843640 |
| Minimum	| 27.286528	| 28.064516	| 26.451612	| 27.030361	| 25.056438	| 10846400 |
| 25% - First Quartile	| 34.982501	| 35.275143	| 34.673063	| 34.932689	| 33.192708 |	22762550 |
| Median	| 37.189999	| 37.454422 |	36.725001	| 37.164999 |	35.514814	| 28818400 |
| 75% - Third Quartile	| 43.822500	| 44.177500	| 43.265000 | 43.767501	| 43.069115 |	38661490 |
| Maximum	| 60.599998	| 61.709999	| 59.830002 |	61.250000	| 60.787823	| 230153900 |

Plots of all columns

Below are plots for each of the variables, plotted against the Date variable. This validates the results in the correlation matrix that the target and the other predictors except for volume are highly correlated. 

![p18](/assets/p18.PNG)

Plot of Closing Price

The plot brings a more refined look at the plot of the Close variable (Closing price) against Date. We can see the trend of Pfizer stock over our chosen period. We explored this variable because it is our target variable, and we are getting an overview of how the markets have been behaving and the general trend that the data is following. Generally, ‘Close’ has a positive trend. Also, there was no need to individually explore each of the other variables that are correlated to ‘Close’ because the relationship will follow the same trend. 

![p19](/assets/p19.PNG)

Plot of Volume

We explored volume next because it is not correlated with the other variables and can provide some insight into the data and price movements. It can be noted for Pfizer that the time periods that had extremely high volume also saw spikes in the stock price. 

![p20](/assets/p20.PNG)

Histograms of Closing Price and Volume
We can see from the histograms below that the neither ‘Close’ or ‘Volume’ are normally distributed. They are both exhibiting right skewedness in the data.

![p21](/assets/p21.PNG)

Box Plot of Stock Price Including the High, Low, Open, and Close Prices

The graph below shows the daily box plots of the stock price including the highest price, lowest price and closing price. The green plots show an upward movement in price and the red box plots indicate a downward movement in price. 

![p22](/assets/p22.PNG)

Box Plot for March 2022
Due to the above plot being hard to see because it covers the whole period from 03/02/2020 to 03/10/2022, we also showed the box plots for March 2022. This view makes the box plots easy to see why they are either green or red. 

![p23](/assets/p23.PNG)


Box Plot of Adjusted Close Value

Since the Adj Close was not included in the previous plot, we plotted a box plot. This plot mirrors the Close variable.

![p24](/assets/p24.PNG)

Decomposition of trend, seasonality, and residue of the original time series

For time series analysis, we separate Trend, Seasonality, and noise from the time series. This will help us better understand patterns followed by the data over time. The combination of these different components forms our time series data. We explored the variable ‘Close’ which is our target variable. 

The trend is showing that the closing price is always going up and down in a pattern but overall, there is an upward trend in the closing price of the stock. 
The seasonality is showing constant cyclical events in the stock price. The data is clearly following a repetitive pattern. 

The residual, which is noise in the data, is not highly variable. It stays constant throughout except for a few data points. 

![p25](/assets/p25.PNG)

Testing for stationarity using ADF and KPSS Tests:

![p26](/assets/p26.PNG)

Level of significance for ADF Test and KPSS Test = 0.05

ADF Test: 

Null Hypothesis – The time series is not stationary

The p value of the ADF test is 0.4351 which is greater than 0.05. We can conclude that there is not enough evidence to reject the null hypothesis that the trend is not stationary. Since the p value is not significant and the test statistics is greater than critical values, the trend is not stationary.

KPSS Test:

Null Hypothesis – The time series is stationary

The p value of the KPSS Test is 0.01 which is less than 0.05 therefore we reject the null hypothesis that the trend is stationary. 

From these two test results, we can conclude that the trend is not stationary.

Testing for Stationarity of De-trended Time Series using ADF and KPSS Tests:

![p27](/assets/p27.PNG)

Level of significance for ADF Test and KPSS Test = 0.05

ADF Test: 

Null Hypothesis – The time series is not stationary

After detrending, the p value of the ADF test is 0.000009 which is less than 0.05. We can conclude that there is enough evidence to reject the null hypothesis that the trend is not stationary and conclude that the time series is stationary. 

KPSS Test:

Null Hypothesis – The time series is stationary

The p value is 0.06 which is greater than 0.05 so we cannot reject the null hypothesis that the trend is stationary. Since the p value is not significant, and the test statistics is greater than critical values, the trend is stationary.

From these two test results, we can conclude that the trend is stationary.

![p28](/assets/p28.PNG)

The Partial AutoCorrelation Function (PACF) shows us the partial autocorrelation of the stationary time series and its own lagged values. There is some correlation at certain lags.


Abiomed

Column Statistics
Below is a table showing a summary of the statistics for all the columns in the Abiomed data frame.

||	Open|	High	|Low|	Close|	Adj Close|	Volume|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|Count	|512|	512	|512|	512	|512|	512|
|Mean|	290.006250|	295.067304	|285.064629|	290.275859|	290.275859|	347363.1|
|Standard| Deviation	|55.855447	|56.080977|	55.382787	|55.520666|	55.520666	|225485.3|
|Minimum|	132.130005|	134.740005|	119.010002|	130.509995|	130.509995|	65700|
|25% - First Quartile	|269.797493	|274.150009|	264.735008	|269.647492|	269.647492|	206650|
|Median	|304.065002	|309.150009|	298.630005|	304.680008	|304.680008|	286150|
|75% - Third Quartile|	326.327507	|331.027512	|320.755012	|325.144996|	325.144996|	402725|
|Maximum	|375.269989	|387.399994	|369.660004	|376.200012	|376.200012	|2489300|


Plots of all columns

Below are plots for each of the variables, plotted against the Date variable. This validates the results in the correlation matrix that the target and the other predictors except for volume are highly correlated. All the variables except volume mirror each other. 

![p30](/assets/p30.PNG)


Plot of Closing Price

The plot shows an upward trend in the price of stock followed by a straight sideways trend from around mid 2021 to date. Although the price fluctuates, it is not showing an upward or downward trend but horizontal price movement within a specific range. 

![p31](/assets/p31.PNG)

Plot of Volume
The volume of the stock was explored since it was not correlated to the other variables. It showed high volumes traded in April 2020. 

![p32](/assets/p32.PNG)

Histograms of Closing price and Volume

We can see from the histograms below that the neither ‘Close’ or ‘Volume’ are normally distributed. The data for the closing price is more left skewed and the volume is right skewed.

![p33](/assets/p33.PNG)

Box Plot of Stock Price Including the High, Low, Open, and Close Prices

The boxplots are showing daily price movement for Abiomed. 

![p34](/assets/p34.PNG)

Month of March

The box plots below validate what we saw earlier with the stock price of Abiomed staying in the same price range with barely any movement.

![p35](/assets/p35.PNG)

Box Plot of Adjusted close value

This plot mirrors the Close variable.

![p36](/assets/p36.PNG)

Decomposition of trend, seasonality, and residue of the original time series

The trend is showing that the closing price is always going up and down in a pattern but overall, there was an upward trend in the closing price of the stock but lately the stock shows a horizontal trendline. 

The seasonality is showing constant cyclical events in the stock price. The data is clearly following a repetitive pattern. 

The residual, which is noise in the data, is not highly variable. It stays constant throughout except for a few data points. 

![p37](/assets/p37.PNG)

Testing for stationarity using ADF and KPSS Tests:

![p38](/assets/p38.PNG)

Level of significance for ADF Test and KPSS Test = 0.05

ADF Test:

Null Hypothesis – The time series is not stationary 

The p value of the ADF test is 0.109760 which is greater than 0.05. We can conclude that there is not enough evidence to reject the null hypothesis that the trend is not stationary. Since the p value is not significant and the test statistics is greater than critical values, the trend is not stationary.

KPSS Test:

Null Hypothesis – The time series is stationary 

The p value of the KPSS Test is 0.01 which is less than 0.05 therefore we reject the null hypothesis that the trend is stationary. 

From these two test results, we can conclude that the trend is not stationary.

Testing for stationarity of de-trended time series using ADF and KPSS Tests:

![p39](/assets/p39.PNG)

ADF Test:

Null Hypothesis – The time series is not stationary 

After detrending, the p value of the ADF test is 0.005971 which is less than 0.05. We can conclude that there is enough evidence to reject the null hypothesis that the trend is not stationary

KPSS Test: 

Null Hypothesis – The time series is stationary 

The p value is 0.024823 which is less than 0.05 so we reject the null hypothesis that the trend is stationary. 

Both the ADF and KPSS tests reject the null hypothesis so we will use the critical values and test statistics to draw a conclusion. The test statistics for the KPSS test is greater than critical values, so we conclude that the trend is stationary.

From the test results, we can conclude that the trend is stationary.

AstraZeneca

Column Statistics:

Below is a table showing a summary of the statistics for all the columns in the AstraZeneca data frame.

||Open|	High	|Low	|Close|	Adj Close	|Volume|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|Count|	512	|512	|512	|512	|512	|512|
|Mean	|54.561562|	55.016621|	54.063652|	54.532832	|52.814224|	7639046|
|Standard Deviation|	4.586799	|4.518413|	4.631367|	4.540777|	4.889356|	6306104|
|Minimum	|36.810001|	38.889999|	36.150002|	37.790001	|35.893379|	1337100|
|25%- First Quartile|	52.075000	|52.310000|	51.287501	|51.697501	|49.6434887|	4319875|
|Median|	55.100001	|55.475001	|54.629999|	55.120001|	52.920546	|6085100|
|75%-Third Quartile|	57.627500	|58.165001|	57.152501	|57.74|	56.568620|	8886275|
|Maximum	|63.950001|	64.940002|	63.509998|	63.830002|	62.791473|	65540200|

Plots of all columns:

Below are plots for each of the variables, plotted against the Date variable. This validates the results in the correlation matrix that the target and the other predictors except for volume are highly correlated. All the variables except volume mirror each other.

![p41](/assets/p41.PNG)

Plot of Closing price: 

The closing price is not following a specific trend. The price went up then down at some point and seems to be currently following a horizontal trend with price staying in a specific range. 

![p42](/assets/p42.PNG)

Plot of Volume: 

The volume of AstraZeneca shares has a few times when the volume was extremely high compared to days around the same time. 

![p43](/assets/p43.PNG)

Histograms of Closing price and Volume: 

We can see from the histograms below that the Close is left skewed and Volume is right skewed.

![p44](/assets/p44.PNG)

Box Plot of Stock Price Including the High, Low, Open, and Close Prices

The boxplots are showing daily price movement for AstraZeneca.

![p45](/assets/p45.PNG)

Month of March

The box plots below validate what we saw earlier with the stock price of a given stock staying in the same price range with barely any movement.

![p46](/assets/p46.PNG)

Box Plot of Adjusted close value:

Since the Adj Close was not included in the previous plot, we plotted a box plot. This plot mirrors the Close variable.

![p47](/assets/p47.PNG)

Decomposition of trend, seasonality, and residue of the original time series

The trend is showing that the closing price is always going up and down in a pattern but overall, there is an upward trend in the closing price of the stock. 

The seasonality is showing constant cyclical events in the stock price. The data is clearly following a repetitive pattern. 

The residual, which is noise in the data, is not highly variable. It stays constant throughout except for a few data points. 

![p48](/assets/p48.PNG)

Testing for stationarity using ADF and KPSS Tests:

![p49](/assets/p49.PNG)

Level of significance for ADF Test and KPSS Test = 0.05

ADF Test:

Null Hypothesis – The time series is not stationary 

The p value of the ADF test is 0.078004 which is greater than 0.05. We can conclude that there is not enough evidence to reject the null hypothesis that the trend is not stationary. Since the p value is not significant and the test statistics is greater than critical values, the trend is not stationary.

KPSS Test:

Null Hypothesis – The time series is stationary 

The p value of the KPSS Test is 0.01 which is less than 0.05 therefore we reject the null hypothesis that the trend is stationary. 

From these two test results, we can conclude that the trend is not stationary.

Testing for stationarity of de-trended time series using ADF and KPSS Tests:

![p50](/assets/p50.PNG)

ADF Test:

Null Hypothesis – The time series is not stationary 

After detrending, the p value of the ADF test is 0.002 which is less than 0.05. We can conclude that there is enough evidence to reject the null hypothesis that the trend is not stationary. 

KPSS Test:

Null Hypothesis – The time series is stationary 

The p value is 0.1 which is greater than 0.05 so we cannot reject the null hypothesis that the trend is stationary. Since the p value is not significant, and the test statistics is greater than critical values, the trend is stationary.

From these two test results, we can conclude that the trend is stationary.

BioNTech

Column Statistics:

Below is a table showing a summary of the statistics for all the columns in the BioNTech data frame.

||	Open	|High|	Low	|Close	|Adj| Close|	Volume|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|Count	|512	|512	|512	|512|	512|	512|
|Mean	|155.11259	|159.82956	|149.337598|	154.765332	|154.765332|	2923595|
|Standard Deviation	|97.563291|	100.911561	|93.852146|	93.852146 |97.685434	|2311294|
|Minimum	|28.99	|30.395|	28	|28.549999|	28.549999|	77000|
|25% - First Quartile|	76.877499	|78.255001|	70.760001	|73.529997	|73.529997	|1468725|
|Median|	114.944999	|117.785	|112.36	|114.68	|114.68	|2344300|
|75% - Third Quartile|	228.315498|	233.575004|	220.394749	|227.857494|	227.857494	|3641475|

Plots of all columns:

Below are plots for each of the variables, plotted against the Date variable. This validates the results in the correlation matrix that the target and the other predictors except for volume are highly correlated. All the variables except volume mirror each other.

![p52](/assets/p52.PNG)

Plot of Closing price: 

The plot shows that the prices of BNTX were initially following an upward trend but lately reversed the trend and are following a downward trend. 

![p53](/assets/p53.PNG)

Plot of Volume: 

We explored volume next because it is not correlated with the other variables and can provide some insight into the data and price movements. The volume for BNTX is consistently high and low without much stability. 

![p54](/assets/p54.PNG)

Histograms of Closing price and Volume: 

We can see from the histograms below that both Close and Volume are right skewed

![p55](/assets/p55.PNG)

Box Plot of Stock Price Including the High, Low, Open, and Close Prices

The boxplots are showing daily price movement for BioNTech.

![p56](/assets/p56.PNG)

Month of March:

The box plots below validate what we saw earlier with the stock price of a given stock staying in the same price range with barely any movement.

![p57](/assets/p57.PNG)

Box Plot of Adjusted close value:

Since the Adj Close was not included in the previous plot, we plotted a box plot. This plot mirrors the Close variable.

![p58](/assets/p58.PNG)

Decomposition of trend, seasonality, and residue of the original time series

The trend is showing that the closing price is always going up and down in a pattern but overall, there is an upward trend in the closing price of the stock with a downward trend forming. 

The seasonality is showing constant cyclical events in the stock price. The data is clearly following a repetitive pattern. 

The residual, which is noise in the data, is variable. There are some data points that show more noise in the data, but nothing concerning. 

![p59](/assets/p59.PNG)


Testing for stationarity using ADF and KPSS Tests:

![p60](/assets/p60.PNG)

Level of significance for ADF Test and KPSS Test = 0.05

ADF Test:

Null Hypothesis – The time series is not stationary 

The p value of the ADF test is 0.109760 which is greater than 0.05. We can conclude that there is not enough evidence to reject the null hypothesis that the trend is not stationary. Since the p value is not significant and the test statistics is greater than critical values, the trend is not stationary.

KPSS Test:

Null Hypothesis – The time series is stationary 

The p value of the KPSS Test is 0.01 which is less than 0.05 therefore we reject the null hypothesis that the trend is stationary. 

From these two test results, we can conclude that the trend is not stationary.

Testing for stationarity of de-trended time series using ADF and KPSS Tests:

![p61](/assets/p61.PNG)

ADF Test:

Null Hypothesis – The time series is not stationary 

After detrending, the p value of the ADF test is 0.011580 which is less than 0.05. We can conclude that there is enough evidence to reject the null hypothesis that the trend is not stationary

KPSS Test:

Null Hypothesis – The time series is stationary 

The p value is 0.1 which is greater than 0.05 so we cannot reject the null hypothesis that the trend is stationary. Since the p value is not significant, and the test statistics is greater than critical values, the trend is stationary.

From these two test results, we can conclude that the trend is stationary.

![p62](/assets/p62.PNG)

The Partial AutoCorrelation Function (PACF) shows us the partial autocorrelation of the stationary time series and its own lagged values. There is some correlation at certain lags.

Bio-Rad Laboratories

Column Statistics:

Below is a table showing a summary of the statistics for all the columns in the Bio-Rad Laboratories data frame.

|	|Open|	High	|Low	|Close	|Adj Close|	Volume|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|Count|	512|	512	|512	|512	|512	|512|
|Mean|	593.063712	|601.103184|	584.57834	|592.861405|	592.861405|	192174.8|
|Standard Deviation|	117.019276|	116.856815|	116.334287|	116.273175 |116.273175 |194862.1|
|Minimum	|315|	335.649994|	309.380005|	320.01001|	320.01001|	40200|
|25% - First Quartile|	516.660004	|521.209991	|508.85749|	515.654999	|515.654999|	113125|
|Median|	588.595001|	596.235016|	579.744995|	588.029999	|588.029999	|159900|
|75% - Third Quartile	|667.949982	|676.122498	|659.654984	|666.927521|	666.927521|	230850|
|Maximum	|822.729980	|832.700012	|817.169983|	825.77002	|825.77002|	3960900|

Plots of all columns:

Below are plots for each of the variables, plotted against the Date variable. This validates the results in the correlation matrix that the target and the other predictors except for volume are highly correlated. All the variables except volume mirror each other.

![p64](/assets/p64.png)

Plot of Closing price:

The plot shows an upward trend in the price of stock followed by a downward trend from around late 2021 to date.

![p65](/assets/p65.png)

Plot of Volume:

We explored volume next because it is not correlated with the other variables and can provide some insight into the data and price movements. In 2020, there was a date when the volume was extremely high but otherwise has stayed in a consistent range throughout.

![p66](/assets/p66.png)

Histograms of Closing price and Volume:

We can see from the histograms below that the Close is normally distributed and Volume is right skewed.

![p67](/assets/p67.png)

Box Plot of Stock Price Including the High, Low, Open, and Close Prices

The boxplots are showing daily price movement for Bio-Rad Laboratories.

![p68](/assets/p68.png)

Month of March:

The box plots below validate what we saw earlier with the stock price of a given stock staying in the same price range with barely any movement.

![p69](/assets/p69.png)

Box Plot of Adjusted close value:

Since the Adj Close was not included in the previous plot, we plotted a box plot. This plot mirrors the Close variable.

![p70](/assets/p70.png)

Decomposition of trend, seasonality, and residue of the original time series

The trend is showing that the closing price is always going up and down in a pattern but overall, there is an upward trend in the closing price of the stock with a downward trend forming. 

The seasonality is showing constant cyclical events in the stock price. The data is clearly following a repetitive pattern. 

The residual, which is noise in the data, is not highly variable. It stays constant throughout except for a few data points.
 
![p71](/assets/p71.png)

Testing for stationarity using ADF and KPSS Tests:

![p72](/assets/p72.png)

Level of significance for ADF Test and KPSS Test = 0.05

ADF Test:

Null Hypothesis – The time series is not stationary 

The p value of the ADF test is 0.317 which is greater than 0.05. We can conclude that there is not enough evidence to reject the null hypothesis that the trend is not stationary. Since the p value is not significant and the test statistics is greater than critical values, the trend is not stationary.

KPSS Test:

Null Hypothesis – The time series is stationary 

The p value of the KPSS Test is 0.01 which is less than 0.05 therefore we reject the null hypothesis that the trend is stationary. 

From these two test results, we can conclude that the trend is not stationary.

Testing for stationarity of de-trended time series using ADF and KPSS Tests:

![p73](/assets/p73.png)

ADF Test:

Null Hypothesis – The time series is not stationary 

After detrending, the p value of the ADF test is 0.052865 which is larger than 0.05. We can conclude that there is not enough evidence to reject the null hypothesis that the trend is not stationary. Since the p value is not significant and the test statistics is greater than critical values, the trend is not stationary.

KPSS Test:

Null Hypothesis – The time series is stationary 

The p value of the KPSS Test is 0.034131 which is less than 0.05 therefore we reject the null hypothesis that the trend is stationary. 

From these two test results, we can conclude that the trend is not stationary.

![p74](/assets/p74.png)

The Partial AutoCorrelation Function (PACF) shows us the partial autocorrelation of the stationary time series and its own lagged values. There is some correlation at certain lags.

Hologic

Column Statistics:

Below is a table showing a summary of the statistics for all the columns in the Hologic data frame.

	||Open	|High	|Low	|Close|	Adj Close|	Volume|
 |:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|Count|	512	|512|	512	|512	|512	|512|
|Mean	|66.823555	|67.711914|	65.849727|	66.778086|	66.778086|	2147370|
|Standard Deviation	|11.053804|	11.006685|	11.043491|	10.991973| 10.991973|	1088479|
|Minimum	|29.639999|	31.15|	26.49	|29.379999|	29.379999|	571700|
|25% - First Quartile|	62.4125|	63.2375|	61.68	|62.449999	|62.449999|	1455125|
|Median	|70.259998	|71.199997|	69.455002|	70.255001|	70.255001	|1853750|
|75% - Third Quartile|	74.132502	|75.1425	|73.125002	|74.102501|	74.102501	|2629425|
|Maximum	|85|85	|82.599998|	83.720001|	83.720001|	9441300|

Plots of all columns:

Below are plots for each of the variables, plotted against the Date variable. This validates the results in the correlation matrix that the target and the other predictors except for volume are highly correlated. All the variables except volume mirror each other.

![p76](/assets/p76.png)

Plot of Closing price:

The trend increased in 05-2020, then it followed the same trend.

![p77](/assets/p77.png)

Plot of Volume:

We explored volume next because it is not correlated with the other variables and can provide some insight into the data and price movements.

![p78](/assets/p78.png)

Histograms of Closing price and Volume:

We can see from the histograms below that the Close is left skewed and Volume is right skewed.

![p79](/assets/p79.png)

Box Plot of Stock Price Including the High, Low, Open, and Close Prices

The boxplots are showing daily price movement for Hologic.

![p80](/assets/p80.png)

Month of March:

The box plots below validate what we saw earlier with the stock price of a given stock staying in the same price range with barely any movement.

![p81](/assets/p81.png)

Box Plot of Adjusted close value:

Since the Adj Close was not included in the previous plot, we plotted a box plot. This plot mirrors the Close variable.

![p82](/assets/p82.png)

Decomposition of trend, seasonality, and residue of the original time series

The trend is showing that the closing price was initially going up then started following a horizontal trend.

The seasonality is showing constant cyclical events in the stock price. The data is clearly following a repetitive pattern. 

The residual, which is noise in the data, is not highly variable. It stays constant throughout except for a few data points.

![p83](/assets/p83.png)

Testing for stationarity using ADF and KPSS Tests:

![p84](/assets/p84.png)

Level of significance for ADF Test and KPSS Test = 0.05

ADF Test:

Null Hypothesis – The time series is not stationary 

The p value of the ADF test is 0.33 which is greater than 0.05. We can conclude that there is not enough evidence to reject the null hypothesis that the trend is not stationary. Since the p value is not significant and the test statistics is greater than critical values, the trend is not stationary.

KPSS Test:

Null Hypothesis – The time series is stationary 

The p value of the KPSS Test is 0.01 which is less than 0.05 therefore we reject the null hypothesis that the trend is stationary. 

From these two test results, we can conclude that the trend is not stationary.

Testing for stationarity of de-trended time series using ADF and KPSS Tests:

![p85](/assets/p85.png)

ADF Test:

Null Hypothesis – The time series is not stationary 

After detrending, the p value of the ADF test is 0.000286 which is less than 0.05. We can conclude that there is enough evidence to reject the null hypothesis that the trend is not stationary.

KPSS Test:

Null Hypothesis – The time series is stationary 

The p value of the KPSS Test is 0.032895 which is less than 0.05 therefore we reject the null hypothesis that the trend is stationary. 

From these two test results, we can conclude that the trend is not stationary.

![p86](/assets/p86.png)

The Partial AutoCorrelation Function (PACF) shows us the partial autocorrelation of the stationary time series and its own lagged values. There is some correlation at certain lags.

Johnson & Johnson

Column Statistics:

Below is a table showing a summary of the statistics for all the columns in the J&J data frame.

||Open	|High|	Low|	Close|Adj Close	|Volume|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|Count|	512|	512	|512	|512	|512|	512|
|Mean|	157.374434	|158.685058|	156.039277|	157.403379|	153.254717|	7658388|
|Standard Deviation|	11.671043|	11.335790|	12.039835	|11.7081 |13.189613	|3203968|
|Minimum|	117|	118.559998	|109.160004|	111.139999|	105.534302|	2114900|
|25% - First Quartile|	148.444996|	148.347504|	146.860001	|148.134998|	141.78701	|5649025|
|Median|	160.48001|	161.57	|159.5|	160.43	|157.376289|	6876650|
|75% - Third Quartile	|166.145004	|167.59	|164.732498	|166.044994	|163.617267|	8515375|
|Maximum	|179.5	|179.919998|	178.070007|	179.470001	|176.118301	|2250590|

Plots of all columns:

Below are plots for each of the variables, plotted against the Date variable. This validates the results in the correlation matrix that the target and the other predictors except for volume are highly correlated. All the variables except volume mirror each other.

![p88](/assets/p88.png)

Plot of Closing price:

The trend increased in around 05-2020, and there was also a peak increase in around 08-2021.

![p89](/assets/p89.png)

Plot of Volume:

We explored volume next because it is not correlated with the other variables and can provide some insight into the data and price movements.

![p90](/assets/p90.png)

Histograms of Closing price and Volume:

We can see from the histograms below that the Close is left skewed and Volume is right skewed.

![p91](/assets/p91.png)

Box Plot of Stock Price Including the High, Low, Open, and Close Prices

The boxplots are showing daily price movement for J&J.

![p92](/assets/p92.png)

Month of March:

The box plots below validate what we saw earlier with the stock price of a given stock staying in the same price range with barely any movement.

![p93](/assets/p93.png)

Box Plot of Adjusted close value:

Since the Adj Close was not included in the previous plot, we plotted a box plot. This plot mirrors the Close variable.

![p94](/assets/p94.png)

Decomposition of trend, seasonality, and residue of the original time series

The trend is showing that the closing price is always going up and down in a pattern but overall, there is an upward trend in the closing price of the stock, but it looks like a horizontal trend is forming. 

The seasonality is showing constant cyclical events in the stock price. The data is clearly following a repetitive pattern. 

The residual, which is noise in the data, is not highly variable. It stays constant throughout.

![p95](/assets/p95.png)

Testing for stationarity using ADF and KPSS Tests:

![p96](/assets/p96.png)

Level of significance for ADF Test and KPSS Test = 0.05

ADF Test:

Null Hypothesis – The time series is not stationary 

The p value of the ADF test is 0.13 which is greater than 0.05. We can conclude that there is not enough evidence to reject the null hypothesis that the trend is not stationary. Since the p value is not significant and the test statistics is greater than critical values, the trend is not stationary.

KPSS Test:

Null Hypothesis – The time series is stationary 

The p value of the KPSS Test is 0.01 which is less than 0.05 therefore we reject the null hypothesis that the trend is stationary. 

From these two test results, we can conclude that the trend is not stationary.

Testing for stationarity of de-trended time series using ADF and KPSS Tests:

![p97](/assets/p97.png)

ADF Test:

Null Hypothesis – The time series is not stationary 

The p value of the ADF test is 0.00104 which is less than 0.05. We can conclude that there is enough evidence to reject the null hypothesis that the trend is not stationary. 

KPSS Test:

Null Hypothesis – The time series is stationary 

The p value of the KPSS Test is 0.1 which is large than 0.05 therefore we do not reject the null hypothesis that the trend is stationary. Since the p value is not significant and the test statistics is greater than critical values, the trend is not stationary. 

From these two test results, we can conclude that the trend is not stationary.

![p98](/assets/p98.png)

The Partial AutoCorrelation Function (PACF) shows us the partial autocorrelation of the stationary time series and its own lagged values. There is some correlation at certain lags.

Lyondell Basell Industries

Column Statistics:

Below is a table showing a summary of the statistics for all the columns in the Lyondell Basell Industries data frame.

||Open	|High|	Low|	Close|Adj Close	|Volume|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|Count|	512	|512|	512	|512	|512|	512|
|Mean	|86.493965	|87.876719	|85.108066|	86.478789|	82.566816|	2164909|
|Standard Deviation	|18.083014	|17.930977|	18.119767	|18.042215	|18.664390	|1121908|
|Minimum	|36.139999|	42.27	|33.709999	|34.900002|	31.702772|	255700|
|25% - First Quartile	|70.884998	|72.5	|69.287502	|70.4975	|65.685644	|1395850|
|Median	|92.064999	|93.420002	|91.320003|	92.205002|	89.455552	|1913050|
|75% - Third Quartile	|100.127498|	101.389999	|98.912503|	100.162501	|97.561051|	2624525|
|Maximum	|117.330002|	118.019997|	115.410004	|117.860001|	112.711372	|9219300|

Plots of all columns:

Below are plots for each of the variables, plotted against the Date variable. This validates the results in the correlation matrix that the target and the other predictors except for volume are highly correlated. All the variables except volume mirror each other.

![p100](/assets/p100.png)

Plot of Closing price:

There was a decrease in trend after 08-2021.

![p101](/assets/p101.png)

Plot of Volume:

We explored volume next because it is not correlated with the other variables and can provide some insight into the data and price movements.

![p102](/assets/p102.png)

Histograms of Closing price and Volume:

We can see from the histograms below that the Close is left skewed and Volume is right skewed.

![p103](/assets/p103.png)

Box Plot of Stock Price Including the High, Low, Open, and Close Prices

The boxplots are showing daily price movement for Lyondell Basell.

![p104](/assets/p104.png)

Month of March:

The box plots below validate what we saw earlier with the stock price of a given stock staying in the same price range with barely any movement.

![p105](/assets/p105.png)

Box Plot of Adjusted close value:

Since the Adj Close was not included in the previous plot, we plotted a box plot. This plot mirrors the Close variable.

![p106](/assets/p106.png)

Decomposition of trend, seasonality, and residue of the original time series

The trend is showing that the closing price is always going up and down in a pattern but overall, there is an upward trend in the closing price of the stock with a potential horizontal trend forming. 

The seasonality is showing constant cyclical events in the stock price. The data is clearly following a repetitive pattern. 

The residual, which is noise in the data, is not highly variable. It stays constant throughout except for a few data points. 

![p107](/assets/p107.png)

Testing for stationarity using ADF and KPSS Tests:

![p108](/assets/p108.png)

Level of significance for ADF Test and KPSS Test = 0.05

ADF Test:

Null Hypothesis – The time series is not stationary 

The p value of the ADF test is 0.57 which is greater than 0.05. We can conclude that there is not enough evidence to reject the null hypothesis that the trend is not stationary. Since the p value is not significant and the test statistics is greater than critical values, the trend is not stationary.

KPSS Test:

Null Hypothesis – The time series is stationary 

The p value of the KPSS Test is 0.01 which is less than 0.05 therefore we reject the null hypothesis that the trend is stationary. 

From these two test results, we can conclude that the trend is not stationary.

Testing for stationarity of de-trended time series using ADF and KPSS Tests:

![p109](/assets/p109.png)

Null Hypothesis – The time series is not stationary 

The p value of the ADF test is 0.000335 which is less than 0.05. We can conclude that there is enough evidence to reject the null hypothesis that the trend is not stationary. 

KPSS Test:

Null Hypothesis – The time series is stationary 

The p value of the KPSS Test is 0.040724 which is less than 0.05 therefore we reject the null hypothesis that the trend is stationary. 

From these two test results, we can conclude that the trend is not stationary.

![p110](/assets/p110.png)

Moderna

Column Statistics:

Below is a table showing a summary of the statistics for all the columns in the Moderna data frame.

||Open	|High|	Low|	Close|Adj Close	|Volume|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|Count	|512	|512	|512	|512|	512|	512|
|Mean	|166.089303	|171.872350	|160.584826|	166.594668|	166.594668	|15624390|
|Standard Deviation	|111.003436	|114.881559	|107.64231|	111.592811|	111.592811	|14359650|
|Minimum	|22.540001	|23.469999	|19.309999	|21.299999	|21.299999|	3735100|
|25% - First Quartile	|69.584997	|71.537502	|67.747502	|69.99	|69.99|	7330850|
|Median	|147.175003	|152.25|	140.955002|	146.904999	|146.904999	|11446000|
|75% - Third Quartile|	229.739998|	235.100006	|221.015007|	232.794994|	232.794994|	17192800|
|Maximum	|485.5|	497.48999|	454	|484.470001	|484.470001|	125130400|

Plots of all columns:

Below are plots for each of the variables, plotted against the Date variable. This validates the results in the correlation matrix that the target and the other predictors except for volume are highly correlated. All the variables except volume mirror each other.

![p112](/assets/p112.png)

Plot of Closing price:

From the trend below we can see that the trend is decreasing and dropping continuously.

![p113](/assets/p113.png)

Plot of Volume:

We explored volume next because it is not correlated with the other variables and can provide some insight into the data and price movements.

![p114](/assets/p114.png)

Histograms of Closing price and Volume:

We can see from the histograms below that the Close is right skewed and Volume is right skewed.

![p115](/assets/p115.png)

Box Plot of Stock Price Including the High, Low, Open, and Close Prices

The boxplots are showing daily price movement for Moderna.

![p116](/assets/p116.png)

Month of March:

The box plots below validate what we saw earlier with the stock price of a given stock staying in the same price range with barely any movement.

![p117](/assets/p117.png)

Box Plot of Adjusted close value:

Since the Adj Close was not included in the previous plot, we plotted a box plot. This plot mirrors the Close variable.

![p118](/assets/p118.png)

Decomposition of trend, seasonality, and residue of the original time series

The trend is showing that the closing price is always going up and down in a pattern but overall, there is an upward trend in the closing price of the stock. The data is starting to show a downward trend. 

The seasonality is showing constant cyclical events in the stock price. The data is clearly following a repetitive pattern. 

The residual, which is noise in the data, is variable. The noise is looking a bit cyclical.

![p119](/assets/p119.png)

Testing for stationarity using ADF and KPSS Tests:

![p120](/assets/p120.png)

Level of significance for ADF Test and KPSS Test = 0.05

ADF Test:

Null Hypothesis – The time series is not stationary 

The p value of the ADF test is 0.49 which is greater than 0.05. We can conclude that there is not enough evidence to reject the null hypothesis that the trend is not stationary. Since the p value is not significant and the test statistics is greater than critical values, the trend is not stationary.

KPSS Test:

Null Hypothesis – The time series is stationary 

The p value of the KPSS Test is 0.01 which is less than 0.05 therefore we reject the null hypothesis that the trend is stationary. 

From these two test results, we can conclude that the trend is not stationary.

Testing for stationarity of de-trended time series using ADF and KPSS Tests:

![p121](/assets/p121.png)

ADF Test:

Null Hypothesis – The time series is not stationary 

The p value of the ADF test is 0.000335 which is less than 0.05. We can conclude that there is enough evidence to reject the null hypothesis that the trend is not stationary.

KPSS Test:

Null Hypothesis – The time series is stationary 

The p value of the KPSS Test is 0.040724 which is less than 0.05 therefore we reject the null hypothesis that the trend is stationary. 

From these two test results, we can conclude that the trend is not stationary.

![p122](/assets/p122.png)

Novavax

Column Statistics:

Below is a table showing a summary of the statistics for all the columns in the Novavax data 

||Open	|High|	Low|	Close|Adj Close	|Volume|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|Count	|512	|512	|512	|512|	512|	512|
|Mean|	137.554141	|143.688281|	131.407598	|137.552207|	137.552207	|5852209|
|Standard Deviation|	69.692582|	72.345219|	66.743645|	69.574579|	69.574579|	5254702|
|Minimum|	7.77|	8.14	|6.77	|6.91|	6.91|	1480500|
|25% - First Quartile|	88.039999|	92.927498|	85.657499	|89.412502	|89.412502	|3007250|
|Median	|133.670006|	140.684998	|127.529999|	134.990005	|134.990005	|4437500|
|75% - Third Quartile	|188.014996	|195.770001	|180.250004	|188.412503	|188.412503|	6781200|
|Maximum	|324.5	|331.679993|	312	|319.929993|	319.929993|	74649600|

Plots of all columns:

Below are plots for each of the variables, plotted against the Date variable. This validates the results in the correlation matrix that the target and the other predictors except for volume are highly correlated. All the variables except volume mirror each other.

![p124](/assets/p124.png)

Plot of Closing price:

From the trend below we can observe that the current trend is dropping and decreasing continuously.

![p125](/assets/p125.png)

Plot of Volume:

We explored volume next because it is not correlated with the other variables and can provide some insight into the data and price movements.

![p126](/assets/p126.png)

Histograms of Closing price and Volume:

From the below histogram we can see that close is normally distributed and volume is right skewed.

![p127](/assets/p127.png)

Box Plot of Stock Price Including the High, Low, Open, and Close Prices

The boxplots are showing daily price movement for Novavax.

![p128](/assets/p128.png)

Month of March:

The box plots below validate what we saw earlier with the stock price of a given stock staying in the same price range with barely any movement.

![p129](/assets/p129.png)

Box Plot of Adjusted close value:

Since the Adj Close was not included in the previous plot, we plotted a box plot. This plot mirrors the Close variable.

![p130](/assets/p130.png)

Decomposition of trend, seasonality, and residue of the original time series

The trend is showing that the closing price is always going up and down in a pattern but overall, there is an upward trend in the closing price of the stock. The data looks like it is now switching to a downward trend.

The seasonality is showing constant cyclical events in the stock price. The data is clearly following a repetitive pattern. 

The residual, which is noise in the data, is variable. It is not constant throughout and keeps changing. 

![p131](/assets/p131.png)

Testing for stationarity using ADF and KPSS Tests:

![p132](/assets/p132.png)

Level of significance for ADF Test and KPSS Test = 0.05

ADF Test:

Null Hypothesis – The time series is not stationary 

The p value of the ADF test is 0.15 which is greater than 0.05. We can conclude that there is not enough evidence to reject the null hypothesis that the trend is not stationary. Since the p value is not significant and the test statistics is greater than critical values, the trend is not stationary.

KPSS Test:

Null Hypothesis – The time series is stationary 

The p value of the KPSS Test is 0.01 which is less than 0.05 therefore we reject the null hypothesis that the trend is stationary. 

From these two test results, we can conclude that the trend is not stationary.

Testing for stationarity of de-trended time series using ADF and KPSS Tests:

![p133](/assets/p133.png)

ADF Test:

Null Hypothesis – The time series is not stationary 

The p value of the ADF test is 0.00021 which is less than 0.05. We can conclude that there is enough evidence to reject the null hypothesis that the trend is not stationary. 

KPSS Test:

Null Hypothesis – The time series is stationary 

The p value of the KPSS Test is0.047293 which is less than 0.05 therefore we reject the null hypothesis that the trend is stationary. 

From these two test results, we can conclude that the trend is not stationary.

![p134](/assets/p134.png)

Regeneron Pharmaceutical

Column Statistics:

Below is a table showing a summary of the statistics for all the columns in the Regeneron Pharmaceutical data frame.

||Open	|High|	Low|	Close|Adj Close	|Volume|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|Count	|512	|512	|512	|512|	512|	512|
|Mean|	564.738302	|572.728672	|556.230663	|564.61131|	564.61131	|946485.2|
|Standard Deviation	|61.599506|	61.812238|	61.347555|	61.929342|	61.929342|	638849|
|Minimum	|426.51001	|451.850006|	418.01001	|429.779999	|429.779999	|289100|
|25% - First Quartile	|505.670006	|513.429992	|498.357498|	504.952507|	504.952507|	637375|
|Median	|573.420014|	578.984985|	563.475006	|573.820007	|573.820007	|826350|
|75% - Third Quartile	|616.169998	|624.657501|	608.69249|	618.137481	|618.137481|	1062600|
|Maximum	|683.5|686.619995	|674.570007	|680.960022	|680.960022	|7869500|

Plots of all columns:

Below are plots for each of the variables, plotted against the Date variable. This validates the results in the correlation matrix that the target and the other predictors except for volume are highly correlated. All the variables except volume mirror each other.

![p136](/assets/p136.png)

Plot of Closing price:

We can see an increase in trend in around 05-2021 and then an extreme drop in around 11-2021.

![p137](/assets/p137.png)

Plot of Volume:

We explored volume next because it is not correlated with the other variables and can provide some insight into the data and price movements.

![p138](/assets/p138.png)

Histograms of Closing price and Volume:

From the below histogram we can see that that close is normally distributed and volume is right skewed.

![p139](/assets/p139.png)

Box Plot of Stock Price Including the High, Low, Open, and Close Prices

The boxplots show daily price movement for the above-mentioned stock.

![p140](/assets/p140.png)

Month of March:

The box plots below validate what we saw earlier with the stock price of a given stock staying in the same price range with barely any movement.

![p141](/assets/p141.png)

Box Plot of Adjusted close value:

Since the Adj Close was not included in the previous plot, we plotted a box plot. This plot mirrors the Close variable.

![p142](/assets/p142.png)

Decomposition of trend, seasonality, and residue of the original time series

The trend is showing that the closing price is always going up and down in a pattern but overall, there is an upward trend in the closing price of the stock. The data is currently showing a horizontal trend.

The seasonality is showing constant cyclical events in the stock price. The data is clearly following a repetitive pattern. 

The residual, which is noise in the data, is not highly variable. It stays constant throughout except for a few data points. 

![p143](/assets/p143.png)

Testing for stationarity using ADF and KPSS Tests:

![p144](/assets/p144.png)

Level of significance for ADF Test and KPSS Test = 0.05

ADF Test:

Null Hypothesis – The time series is not stationary 

The p value of the ADF test is 0.23 which is greater than 0.05. We can conclude that there is not enough evidence to reject the null hypothesis that the trend is not stationary. Since the p value is not significant and the test statistics is greater than critical values, the trend is not stationary.

KPSS Test:

Null Hypothesis – The time series is stationary 

The p value of the KPSS Test is 0.02 which is less than 0.05 therefore we reject the null hypothesis that the trend is stationary. 

From these two test results, we can conclude that the trend is not stationary.

Testing for stationarity of de-trended time series using ADF and KPSS Tests:

![p145](/assets/p145.png)

ADF Test:

Null Hypothesis – The time series is not stationary 

The p value of the ADF test is 0.0046 which is less than 0.05. We can conclude that there is enough evidence to reject the null hypothesis that the trend is not stationary. 

KPSS Test:

Null Hypothesis – The time series is stationary 

The p value of the KPSS Test is 0.1 which is greater than 0.05 therefore we do not reject the null hypothesis that the trend is stationary. Since the p value is not significant and the test statistics is greater than critical values, the trend is not stationary. 

From these two test results, we can conclude that the trend is not stationary.

![p146](/assets/p146.png)

ThermoFisher Scientific

Column Statistics:

Below is a table showing a summary of the statistics for all the columns in the ThermoFisher Scientific data frame.

||Open	|High|	Low|	Close|Adj Close	|Volume|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|Count	|512	|512	|512	|512|	512|	512|
|Mean	|478.49959	|484.054844	|472.747383	|478.369102|	477.627864|	1607559|
|Standard Deviation	|96.532271|	96.548727	|95.845381	|96.036743	|96.391229|	711400.2|
|Minimum	|263.549988	|275	|250.210007|	255.300003	|254.373535|	442100|
|25% - First Quartile|	420.120003	|424.77501	|416.420006|	420.725006	|417.633194	|1137875|
|Median	|472.265	|478.98999	|467.744995|	471.665008	|470.776596	|1464150|
|75% - Third Quartile	|550.067505	|554.285019	|542.464996	|549.960007	|549.875641	|1876000|
|Maximum	|665.5	|672.340027|	663.330017|	667.239990	|667.239990	|5272300|

Plots of all columns:

Below are plots for each of the variables, plotted against the Date variable. This validates the results in the correlation matrix that the target and the other predictors except for volume are highly correlated. All the variables except volume mirror each other.

![p148](/assets/p148.png)

Plot of Closing price:

Overall, there was an increase in the trend, the trend started dropping recently.

![p149](/assets/p149.png)

Plot of Volume:

We explored volume next because it is not correlated with the other variables and can provide some insight into the data and price movements.

![p150](/assets/p150.png)

Histograms of Closing price and Volume:

We can see from the histograms below that Close is normally distributed and Volume is right skewed.

![p151](/assets/p151.png)

Box Plot of Stock Price Including the High, Low, Open, and Close Prices

The boxplots show daily price movement for the above-mentioned stock.

![p152](/assets/p152.png)

Month of March:

The box plots below validate what we saw earlier with the stock price of a given stock staying in the same price range with barely any movement.

![p153](/assets/p153.png)

Box Plot of Adjusted close value:

Since the Adj Close was not included in the previous plot, we plotted a box plot. This plot mirrors the Close variable.

![p154](/assets/p154.png)

Decomposition of trend, seasonality, and residue of the original time series

The trend is showing that the closing price is always going up and down in a pattern but overall, there is an upward trend in the closing price of the stock. 

The seasonality is showing constant cyclical events in the stock price. The data is clearly following a repetitive pattern. 

The residual, which is noise in the data, is not highly variable. It stays constant throughout except for a few data points. 

![p155](/assets/p155.png)

Testing for stationarity using ADF and KPSS Tests:

![p156](/assets/p156.png)

Level of significance for ADF Test and KPSS Test = 0.05

ADF Test:

Null Hypothesis – The time series is not stationary 

The p value of the ADF test is 0.42 which is greater than 0.05. We can conclude that there is not enough evidence to reject the null hypothesis that the trend is not stationary. Since the p value is not significant and the test statistics is greater than critical values, the trend is not stationary.

KPSS Test:

Null Hypothesis – The time series is stationary 

The p value of the KPSS Test is 0.02 which is less than 0.05 therefore we reject the null hypothesis that the trend is stationary. 

From these two test results, we can conclude that the trend is not stationary.

Testing for stationarity of de-trended time series using ADF and KPSS Tests:

![p157](/assets/p157.png)

ADF Test:

Null Hypothesis – The time series is not stationary 

The p value of the ADF test is 0.0046 which is less than 0.05. We can conclude that there is enough evidence to reject the null hypothesis that the trend is not stationary. 

KPSS Test:

Null Hypothesis – The time series is stationary 

The p value of the KPSS Test is 0.1 which is greater than 0.05 therefore we do not reject the null hypothesis that the trend is stationary. Since the p value is not significant and the test statistics is greater than critical values, the trend is not stationary. 

From these two test results, we can conclude that the trend is not stationary.

![p158](/assets/p158.png)

West Pharmaceutical Services

Column Statistics:

Below is a table showing a summary of the statistics for all the columns in the West Pharmaceutical Services data frame.

||Open	|High|	Low|	Close|Adj Close	|Volume|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|Count	|512	|512	|512	|512|	512|	512|
|Mean	|315.302363	|319.442637	|311.002089	|315.412363|	314.872912	|486601.6|
|Standard Deviation|	87.10174	|87.522775	|86.143934	|86.833543|	87.014969	|739512.1|
|Minimum	|130.449997	|132.619995|	124.529999|	128.960007	|128.369873	|147100|
|25% - First Quartile	|270.049987	|274.364998	|266.302498	|268.957496|	268.364029	|310075|
|Median	|294.940002|	298.449997|	291.475006|	294.809998|	294.08081|	406650|
|75% - Third Quartile	|389.417511|	394.932503	|381.317504|	390.652504	|390.51371	|528300|
|Maximum|	471.119995|	475.350006	|468.260010	|471.339996	|471.116608|	16495700|

Plots of all columns:

Below are plots for each of the variables, plotted against the Date variable. This validates the results in the correlation matrix that the target and the other predictors except for volume are highly correlated. All the variables except volume mirror each other.

![p160](/assets/p160.png)

Plot of Closing price:

Overall, there was an increase in the trend, the trend started dropping recently.

![p161](/assets/p161.png)

Plot of Volume:

We explored volume next because it is not correlated with the other variables and can provide some insight into the data and price movements.

![p162](/assets/p162.png)

Histograms of Closing price and Volume:

We can see from the histograms below that Close is left skewed and Volume is right skewed.

![p163](/assets/p163.png)

Box Plot of Stock Price Including the High, Low, Open, and Close Prices

The boxplots show daily price movement for the above-mentioned stock.

![p164](/assets/p164.png)

Month of March:

The box plots below validate what we saw earlier with the stock price of a given stock staying in the same price range with barely any movement.

![p165](/assets/p165.png)

Box Plot of Adjusted close value:

Since the Adj Close was not included in the previous plot, we plotted a box plot. This plot mirrors the Close variable.

![p166](/assets/p166.png)

Decomposition of trend, seasonality, and residue of the original time series

The trend is showing that the closing price is always going up and down in a pattern but overall, there is an upward trend in the closing price of the stock. The data currently shows a horizontal trend that is potentially switching to a downward trend. 

The seasonality is showing constant cyclical events in the stock price. The data is clearly following a repetitive pattern. 

The residual, which is noise in the data, is not highly variable. It stays constant throughout except for a few data points. 
 
![p167](/assets/p167.png)

Testing for stationarity using ADF and KPSS Tests:

![p168](/assets/p168.png)

Level of significance for ADF Test and KPSS Test = 0.05

ADF Test:

Null Hypothesis – The time series is not stationary 

The p value of the ADF test is 0.41 which is greater than 0.05. We can conclude that there is not enough evidence to reject the null hypothesis that the trend is not stationary. Since the p value is not significant and the test statistics is greater than critical values, the trend is not stationary.

KPSS Test:

Null Hypothesis – The time series is stationary 

The p value of the KPSS Test is 0.02 which is less than 0.05 therefore we reject the null hypothesis that the trend is stationary. 

From these two test results, we can conclude that the trend is not stationary.

Testing for stationarity of de-trended time series using ADF and KPSS Tests:

![p169](/assets/p169.png)

ADF Test:

Null Hypothesis – The time series is not stationary 

After detrending, the p value of the ADF test is 0.03 which is less than 0.05. We can conclude that there is enough evidence to reject the null hypothesis that the trend is not stationary

KPSS Test: 

Null Hypothesis – The time series is stationary 

The p value is 0.08 which is more than 0.05 so we fail to reject the null hypothesis that the trend is stationary. 

ADF reject the null hypothesis so we will use the critical values and test statistics to draw a conclusion.

From the test results, we can conclude that the trend is stationary. 

![p170](/assets/p170.png)

ANALYSIS AND PREDICTIVE MODELLING

When forecasting future stock prices, we used Simple moving average forecast, Simple exponential smoothing forecast, Holt's Exponential Smoothing Method, Holt's Winters' additive Method, Holt's Winters' multiplicative Method and Autoregressive integrated moving average.  The graph below shows the route taken to determine the best models used for analysis. 

![p171](/assets/p171.png)

The data used in this analysis contains more than 10 observations, therefore our option is ARIMA or Exponential Smoothing. If trend does not exist in the data, the Simple exponential smoothing is the appropriate model. When the data shows a trend or the trend is not clear, we moved on to check seasonality. Holt Winters’ was applied to seasonal data and Holt’s method to non-seasonal data. For ARIMA, seasonal data that has exogenous variables was modeled on SARIMAX and SARIMA. Seasonal data that did not have exogenous variables was modeled on ARIMAX and ARIMA.

EXPONENTIAL SMOOTHING - SINGLE

Single Exponential Smoothing (SES) is a time series forecasting approach for univariate data without a trend or seasonality. It is also known as Simple Exponential Smoothing.

Alpha (a), often known as the smoothing factor or smoothing coefficient, is the only parameter required.

This parameter determines how quickly the influence of previous time steps' observations decays exponentially. The value of Alpha is frequently set to a number between 0 and 1. Large values indicate that the model focuses on the most recent historical observations, whilst smaller values indicate that the model considers more of the history when generating a forecast.

EXPONENTIAL SMOOTHING - DOUBLE

Double Exponential Smoothing is an expansion of Exponential Smoothing that explicitly includes trend support in univariate time series. A second smoothing factor, beta, is added to the alpha parameter to manage the decay of the influence of the change in trend (b).

The approach is compatible with trends that change in two ways: additive and multiplicative, depending on whether the trend is linear or exponential. Holt's linear trend model, named after the method's creator Charles Holt, is a standard moniker for Double Exponential Smoothing with an additive trend.

•	Additive Trend: Double Exponential Smoothing with a linear trend.

•	Multiplicative Trend: Double Exponential Smoothing with an exponential trend.

EXPONENTIAL SMOOTHING - TRIPPLE

Triple Exponential Smoothing is a variant of Exponential Smoothing that explicitly accounts for seasonality in univariate time series. This method is also known as Holt-Winters Exponential Smoothing, after two of the system's contributors, Charles Holt, and Peter Winters. A new parameter, gamma (g), is added to the alpha and beta smoothing parameters to adjust the influence on the seasonal component. For a linear or exponential change in seasonality, the seasonality can be treated as an additive or multiplicative process, just as the trend.

AUTOREGRESSIVE INTEGRATED MOVING AVERAGE (ARIMA)

One of the most famous and commonly used statistical models for time-series forecasting is the Auto Regressive Integrated Moving Average (ARIMA) model. It is a group of statistical models that identify the regular temporal dependencies that are particular to time series data. ARIMA models must be used with time series that are stationary. The statistical features of a stationary time series, such as mean and standard deviation, do not change throughout time. Unfortunately, most of the real-world time - series data are not stationary, necessitating transformations to make them so. Integration is the term for the transformation process. Below are the different components of ARIMA: Auto Regressive (AR), Integrated (I), and the Moving Average (MA)

•	AR: Models attempt to forecast future values using data from the past. The time series must be stationary for AR models to work.

•	MA: Models try to anticipate forecasts based on forecasting errors in the past. MA models presume that the supplied series can be approximated by an autoregressive model. This should not be confused with the moving average, which is more of a smoothing technique than a forecasting model.

•	I: The integrated element of ARIMA tries to convert the time-series data's non-stationarity toward something more stationary.

DATA SPLITTING

To assess our models and to see if they were effective in predicting the future price of stock, we split the data into training and validation/test data. The training dataset was used to train the model to recognize patterns and trends in the data and the test dataset was used to see if the model was able to correctly make predictions. For all the 13 companies, the data was split so that 80% of the total data was used in the training of the model and the remaining 20% to test/validate to see if the model could predict well.  This amounted to the first 410 months of data being used as the training dataset and the remaining 103 months as the testing dataset. 

Pfizer

![p172](/assets/p172.png)

The graph above shows the data split with the red line showing the training data and the black line showing the testing data. 

From the graph below, it can be noted that Pfizer has an upward trend. Pfizer shows seasonality, but it is subjective to the eye and the data is only two years old, so we decided to consider both Holt Winters’ and Holt’s and chose the best model using RMSE and MAPE. We also used Auto ARIMA as it considers seasonality irrespective of the trend.

![p173](/assets/p173.png)

MODELS

Holt Exponential Smoothing

![p174](/assets/p174.png)

Holt exponential smoothing forecast (the green line) is showing an upward trend in its forecast. The smoothing RMS is –5.877, the smoothing level is –0.05 and the smoothing slope is –0.6. 

Holt Winters Additive Method

![p175](/assets/p175.png)

The Holt Winters Additive method is also showing an upward trend. The trend looks less steep than that for Holt’s method. The smoothing slope is 7.5026. 

Holt Winters Multiplicative Method

![p176](/assets/p176.png)

The Holt Winter Multiplicative method shows an upward trend with a smooth slope of 1.1859.

Auto ARIMA

![p177](/assets/p177.png)

The Auto ARIMA automatically performed a stepwise search and chose a model that had the lowest AIC. The best model chosen was SARIMAX (0,1,1) as shown above. This model has an AIC of 832.397. Using this model, the prediction below was made, and ARIMA shows a horizontal price trend from the end of the training data. This model shows no trend and is the worst model of all the four models used to look at Pfizer stock. 

![p178](/assets/p178.png)

To compare all four models, we considered the RMSE and MAPE for each of the models.

| METHOD | RMSE | MAPE |
|:---:|:---:|:---:|
| Holt’s exponential smoothing method  | 5.89 | 9.23 |
| Holt Winter’s additive method	| 9.77	| 15.98 |
| Holt Winter’s multiplicative method	| 9.78	| 16.01 |
| Auto ARIMA	| 10.81	| 18.11 |

Based on the RMSE and MAPE results shown below, Holt’s Exponential smoothing has the lowest RMSE and MAPE, making it the best forecasting model. 

Abiomed

![p179](/assets/p179.png)

The graph above shows the data split with the red line showing the training data and the black line showing the testing data.  

From the graph below, it can be noted that Abiomed has An upward trend. Abiomed shows seasonality, but it is subjective to the eye and the data is only two years old, so we decided to consider both Holt Winters’ and Holt’s and chose the best model using RMSE and MAPE. We also used Auto ARIMA as it considers seasonality irrespective of the trend.

![p180](/assets/p180.png)

MODELS

Holt's Exponential Smoothing Method

![p181](/assets/p181.png)

Holt exponential smoothing forecast (the green line) is showing and downward trend in its forecast. The smoothing RMS is –269.095, the smoothing level is –0.3 and the smoothing slope is –0.8.  

Holt Winters Additive Method

![p182](/assets/p182.png)

The Holt Winters Additive method is also showing a downward trend. The smoothing slope is 0.05263.

Holt Winters Multiplicative Method

![p183](/assets/p183.png)

The Holt Winter Multiplicative method shows an upward trend with a smoothing slope of 0.00102.

Auto ARIMA Method

![p184](/assets/p184.png)

The Auto ARIMA automatically performed a stepwise search and chose a model that had the lowest AIC. The best model chosen was SARIMAX (0,1,0) as shown above. This model has an AIC of 2692.913. Using this model, the prediction below was made, and ARIMA shows a horizontal price trend from the end of the training data. This model shows no trend and is the worst model of all the four models used to look at Abiomed stock.

![p185](/assets/p185.png)

To compare all four models, we considered the RMSE and MAPE for each of the models.

| METHOD | RMSE | MAPE |
|:---:|:---:|:---:|
| Holt’s exponential smoothing method  | 18.04 | 4.37 |
| Holt Winter’s additive method	| 26.83	| 6.51 |
| Holt Winter’s multiplicative method	| 33.17	| 9.22 |
| Auto ARIMA	| 284.97	| 7.58 |

Based on the RMSE and MAPE results shown below, Holt’s Exponential smoothing has the lowest RMSE and MAPE, making it the best forecasting model. 

AstraZeneca

![p186](/assets/p186.png)

The graph above shows the data split with the red line showing the training data and the black line showing the testing data.  

From the graph below, it can be noted that AstraZeneca has an upward trend. AstraZeneca shows seasonality, but it is subjective to the eye and the data is only two years old, so we decided to consider both Holt Winters’ and Holt’s and chose the best model using RMSE and MAPE. We also used Auto ARIMA as it considers seasonality irrespective of the trend.

![p187](/assets/p187.png)

MODELS

Holt's Exponential Smoothing Method

![p188](/assets/p188.png)

Holt exponential smoothing forecast (the green line) is showing a downward trend in its forecast. The smoothing RMS is –9.406, the smoothing level is –0.85 and the smoothing slope is –0.95.  

Holt Winters Additive Method

![p189](/assets/p189.png)

![p190](/assets/p190.png)

The Holt Winters Additive method is also showing an upward trend. The smoothing slope is 4.6118. 

Holt Winters Multiplicative Method

![p191](/assets/p191.png)

![p192](/assets/p192.png)

The Holt Winter Multiplicative method shows an upward trend with a smoothing slope of 2.0333. 

Auto ARIMA Method

![p193](/assets/p193.png)

![p194](/assets/p194.png)

The Auto ARIMA automatically performed a stepwise search and chose a model that had the lowest AIC. The best model chosen was SARIMAX (2,1,2) as shown above. This model has an AIC of 1131.636. Using this model, the prediction below was made, and ARIMA shows a horizontal price trend from the end of the training data. This model shows no trend and is the worst model of all the four models used to look at AstraZeneca stock.

![p195](/assets/p195.png)

To compare all four models, we considered the RMSE and MAPE for each of the models.

| METHOD | RMSE | MAPE |
|:---:|:---:|:---:|
| Holt’s exponential smoothing method  | 2.50 | 3.55 |
| Holt Winter’s additive method	| 4.66	| 7.30 |
| Holt Winter’s multiplicative method	| 4.66	| 7.29 |
| Auto ARIMA	| 10.46	| 4.40 |

Based on the RMSE and MAPE results shown below, Holt’s Exponential smoothing has the lowest RMSE and MAPE, making it the best forecasting model. 

BioNTech

![p196](/assets/p196.png)

The graph above shows the data split with the red line showing the training data and the black line showing the testing data.  

From the graph below, it can be noted that BioNTech has an upward trend that is possibly turning into a downward trend. BioNTech shows seasonality, but it is subjective to the eye and the data is only two years old, so we decided to consider both Holt Winters’ and Holt’s and chose the best model using RMSE and MAPE. We also used Auto ARIMA as it considers seasonality irrespective of the trend

![p197](/assets/p197.png)

MODELS

Holt's Exponential Smoothing Method

![p198](/assets/p198.png)

Holt exponential smoothing forecast (the green line) is showing a downward trend in its forecast. The smoothing RMS is –163.309, the smoothing level is –0.55 and the smoothing slope is –0.25.  

Holt Winters Additive Method

![p199](/assets/p199.png)

![p200](/assets/p200.png)

The Holt Winters Additive method is also showing an upward trend. The smoothing slope is 9.1703. 

Holt Winters Multiplicative Method

![p201](/assets/p201.png)

![p202](/assets/p202.png)

The Holt Winter Multiplicative method shows an upward trend with a smoothing slope of 1.4286. 

Auto ARIMA Method

![p203](/assets/p203.png)

![p204](/assets/p204.png)

The Auto ARIMA automatically performed a stepwise search and chose a model that had the lowest AIC. The best model chosen was SARIMAX (0,1,0) as shown above. This model has an AIC of 3020.609. Using this model, the prediction below was made, and ARIMA shows a horizontal price trend from the end of the training data. This model shows no trend and is the worst model of all the four models used to look at BioNTech stock.

![p205](/assets/p205.png)

To compare all four models, we considered the RMSE and MAPE for each of the models.

| METHOD | RMSE | MAPE |
|:---:|:---:|:---:|
| Holt’s exponential smoothing method  | 50.70 | 19.01 |
| Holt Winter’s additive method	| 89.10	| 40.61 |
| Holt Winter’s multiplicative method	| 84.11	| 38.29 |
| Auto ARIMA	| 198.34	| 30.02 |

Based on the RMSE and MAPE results shown below, Holt’s Exponential smoothing has the lowest RMSE and MAPE, making it the best forecasting model. 

Bio-Rad Laboratories

![p206](/assets/p206.png)

The graph above shows the data split with the red line showing the training data and the black line showing the testing data.  

From the graph below, it can be noted that Bio-Rad has an upward trend. Bio-Rad Laboratories shows seasonality, but it is subjective to the eye and the data is only two years old, so we decided to consider both Holt Winters’ and Holt’s and chose the best model using RMSE and MAPE. We also used Auto ARIMA as it considers seasonality irrespective of the trend.

![p207](/assets/p207.png)

MODELS

Holt's Exponential Smoothing Method

![p208](/assets/p208.png)

Holt exponential smoothing forecast (the green line) is showing a downward trend in its forecast. The smoothing RMS is –602.946, the smoothing level is –0.1 and the smoothing slope is –0.05.   

Holt Winters Additive Method

![p209](/assets/p209.png)

![p210](/assets/p210.png)

The Holt Winters Additive method is also showing a downward trend. The smoothing slope is 0.05263. 

Holt Winters Multiplicative Method

![p211](/assets/p211.png)

![p212](/assets/p212.png)

The Holt Winter Multiplicative method shows an upward trend with a smoothing slope of 9.2067. 

Auto ARIMA Method

![p213](/assets/p213.png)

![p214](/assets/p214.png)

The Auto ARIMA automatically performed a stepwise search and chose a model that had the lowest AIC. The best model chosen was SARIMAX (0,1,0) as shown above. This model has an AIC of 3149.771. Using this model, the prediction below was made, and ARIMA shows a horizontal price trend from the end of the training data. This model shows no trend and is the worst model of all the four models used to look at Bio-Rad Laboratories stock.

![p215](/assets/p215.png)

To compare all four models, we considered the RMSE and MAPE for each of the models.

| METHOD | RMSE | MAPE |
|:---:|:---:|:---:|
| Holt’s exponential smoothing method  | 53.04 | 6.37 |
| Holt Winter’s additive method	| 123.76	| 17.19 |
| Holt Winter’s multiplicative method	| 117.64	| 14.33 |
| Auto ARIMA	| 658.57	| 10.73 |

Based on the RMSE and MAPE results shown below, Holt’s Exponential smoothing has the lowest RMSE and MAPE, making it the best forecasting model.

Hologic

![p216](/assets/p216.png)

The graph above shows the data split with the red line showing the training data and the black line showing the testing data.  

From the graph below, it can be noted that Hologic is hard to tell whether it has a trend. Due to this uncertainty, we also considered Simple exponential smoothing. It can however be noted that Holigic shows seasonality, but it is subjective to the eye and the data is only two years old, so we decided to consider both Holt Winters’ and Holt’s and chose the best model using RMSE and MAPE. We also used Auto ARIMA as it considers seasonality irrespective of the trend.

![p217](/assets/p217.png)

MODELS

Simple Exponential Smoothing Method

![p218](/assets/p218.png)

The simple exponential smoothing shows a horizontal line for the forecast. This value went up from the last stock price in the training data, then it stayed the same. This is consistent with the validation data because the stock price is also following a horizontal trend, staying in the same price range.   

Holt's Exponential Smoothing Method

![p219](/assets/p219.png)

Holt exponential smoothing forecast is showing an upward trend in its forecast. The smoothing RMS is –21.056, the smoothing level is –1.0 and the smoothing slope is –0.6.  

Holt’s Additive Method

![p220](/assets/p220.png)

![p221](/assets/p221.png)

The Holt Winters Additive method is also showing a downward trend. The smoothing slope is 0.0526.  

Holt’s Multiplicative Method

![p222](/assets/p222.png)

![p223](/assets/p223.png)

The Holt Winter Multiplicative method shows a slight upward trend with a smoothing slope of 1.5505.

Auto ARIMA Method

![p224](/assets/p224.png)

![p225](/assets/p225.png)

The Auto ARIMA automatically performed a stepwise search and chose a model that had the lowest AIC. The best model chosen was SARIMAX (0,1,0) as shown above. This model has an AIC of 1477.011. Using this model, the prediction below was made, and ARIMA shows a horizontal price trend from the end of the training data. This model shows no trend, and the test data also follows the same horizontal trend.

![p226](/assets/p226.png)

To compare all four models, we considered the RMSE and MAPE for each of the models.

| METHOD | RMSE | MAPE |
|:---:|:---:|:---:|
| Simple exponential smoothing forecast | 2.36 | 2.75 |
| Holt’s exponential smoothing method	| 2.89	| 3.36 |
| Holt Winter’s multiplicative method	| 3.11	| 3.36 |
| Auto ARIMA	| 19.65	| 3.55 |

Based on the RMSE and MAPE results shown below, Simple Exponential smoothing has the lowest RMSE and MAPE, making it the best forecasting model. 

Johnson & Johnson

![p227](/assets/p227.png)

The graph above shows the data split with the red line showing the training data and the black line showing the testing data.

From the graph below, it can be noted that it has an upward trend. There is seasonality, but it is subjective to the eye and the data is only two years old, so we decided to consider both Holt Winters’ and Holt’s and chose the best model using RMSE and MAPE. We also used Auto ARIMA as it considers seasonality irrespective of the trend.

![p228](/assets/p228.png)

MODELS

Holt's Exponential Smoothing Method

![p229](/assets/p229.png)

Holt exponential smoothing forecast (the green line) is showing an upward trend in its forecast. The smoothing RMS is –115.143, the smoothing level is –1.0 and the smoothing slope is –0.55.    

Holt Winters Additive Method

![p230](/assets/p230.png)

![p231](/assets/p231.png)

The Holt Winters Additive method is also showing a downward trend. This contradicts the trend shown in the test data. The smooth slope is 0.0526 

Holt Winters Multiplicative Method

![p232](/assets/p232.png)

![p233](/assets/p233.png)

The Holt Winter Multiplicative method shows an upward trend with a smooth slope of 7.54e- 40. 

Auto ARIMA Method

![p234](/assets/p234.png)

![p235](/assets/p235.png)

The Auto ARIMA automatically performed a stepwise search and chose a model that had the lowest AIC. The best model chosen was SARIMAX (3,0,2) as shown above. This model has an AIC of 1773.259. Using this model, the prediction below was made, and ARIMA shows a horizontal price trend from the end of the training data. This model shows no trend and is the worst model of all the four models used to look at this stock.

![p236](/assets/p236.png)

To compare all four models, we considered the RMSE and MAPE for each of the models.

| METHOD | RMSE | MAPE |
|:---:|:---:|:---:|
| Holt’s exponential smoothing method  | 4.14 | 2.04 |
| Holt Winter’s additive method	| 24.30	| 12.83 |
| Holt Winter’s multiplicative method	| 6.34	| 3.28 |
| Auto ARIMA	| 108.01	| 4.38 |

Based on the RMSE and MAPE results shown below, Holt’s Exponential smoothing has the lowest RMSE and MAPE, making it the best forecasting model.

Lyondell Basell Industries

![p237](/assets/p237.png)

The graph above shows the data split with the red line showing the training data and the black line showing the testing data.

From the graph below, it can be noted that it has an upward trend. Lyondell Basell shows seasonality, but it is subjective to the eye and the data is only two years old, so we decided to consider both Holt Winters’ and Holt’s and chose the best model using RMSE and MAPE. We also used Auto ARIMA as it considers seasonality irrespective of the trend.

![p238](/assets/p238.png)

MODELS

Holt's Exponential Smoothing Method

![p239](/assets/p239.png)

Holt exponential smoothing forecast (the green line) is showing an upward trend in its forecast. The smoothing RMS is –44.777, the smoothing level is –0.05 and the smoothing slope is - 0.25   

Holt Winters Additive Method

![p240](/assets/p240.png)

![p241](/assets/p241.png)

The Holt Winters Additive method is also showing a horizontal trend. The trend looks less steep than that for Holt’s method. The smoothing slope is 0.0348

Holt Winters Multiplicative Method

![p242](/assets/p242.png)

![p243](/assets/p243.png)

The Holt Winter Multiplicative method shows a slightly upward trend with a smooth slope of 1.15e- 41. 

Auto ARIMA Method

![p244](/assets/p244.png)

![p245](/assets/p245.png)

The Auto ARIMA automatically performed a stepwise search and chose a model that had the lowest AIC. The best model chosen was SARIMAX (0,1,0) as shown above. This model has an AIC of 1884.199. Using this model, the prediction below was made, and ARIMA shows a horizontal price trend from the end of the training data. This model shows no trend and is the worst model of all the four models used to look at this stock.

![p246](/assets/p246.png)

To compare all four models, we considered the RMSE and MAPE for each of the models.

| METHOD | RMSE | MAPE |
|:---:|:---:|:---:|
| Holt’s exponential smoothing method  | 4.42 | 3.90 |
| Holt Winter’s additive method	| 4.99	| 4.50 |
| Holt Winter’s multiplicative method	| 6.16	| 5.43 |
| Auto ARIMA	| 45.42	| 4.18 |

Based on the RMSE and MAPE results shown below, Holt’s Exponential smoothing has the lowest RMSE and MAPE, making it the best forecasting model.

Moderna

![p247](/assets/p247.png)

The graph above shows the data split with the red line showing the training data and the black line showing the testing data.

From the graph below, it can be noted that it has an upward trend that might be turning into a downward trend. Moderna shows seasonality, but it is subjective to the eye and the data is only two years old, so we decided to consider both Holt Winters’ and Holt’s and chose the best model using RMSE and MAPE. We also used Auto ARIMA as it considers seasonality irrespective of the trend.

![p248](/assets/p248.png)

MODELS

Holt's Exponential Smoothing Method

![p249](/assets/p249.png)

Holt exponential smoothing forecast (the green line) shows a downward trend in its forecast. The exponential smoothing RMS is - 191.117, smoothing level is - 0.1 and the smoothing slope is - 0.05.  

Holt Winters Additive Method

![p250](/assets/p250.png)

![p251](/assets/p251.png)

The Holt Winters Additive method is also showing an upward trend. The trend looks less steep than that for Holt’s method. The smoothing slope is 1.57e-10.

Holt Winters Multiplicative Method

![p252](/assets/p252.png)

![p253](/assets/p253.png)

The Holt Winter Multiplicative method shows an upward trend with a smooth slope of 0.003. The upward trend prediction contradicts the downward trend in the test data.

Auto ARIMA Method

![p254](/assets/p254.png)

![p255](/assets/p255.png)

The Auto ARIMA automatically performed a stepwise search and chose a model that had the lowest AIC. The best model chosen was SARIMAX (3,1,0) as shown above. This model has an AIC of 3005.483. Using this model, the prediction below was made, and ARIMA shows a horizontal price trend from the end of the training data. This model shows no trend and is the worst model of all the four models used to look at this stock.

![p256](/assets/p256.png)

To compare all four models, we considered the RMSE and MAPE for each of the models.

| METHOD | RMSE | MAPE |
|:---:|:---:|:---:|
| Holt’s exponential smoothing method  | 32.31 | 11.42 |
| Holt Winter’s additive method	| 156.79	| 75.13 |
| Holt Winter’s multiplicative method	| 136.73	| 65.52 |
| Auto ARIMA	| 270.14	| 54.62 |

Based on the RMSE and MAPE results shown below, Holt’s Exponential smoothing has the lowest RMSE and MAPE, making it the best forecasting model.

Novavax

![p257](/assets/p257.png)

The graph above shows the data split with the red line showing the training data and the black line showing the testing data.

From the graph below, it can be noted that it has an upward trend that could potentially turn into a downward trend and seasonality, but it is subjective to the eye and the data is only two years old, so we decided to consider both Holt Winters’ and Holt’s and chose the best model using RMSE and MAPE. We also used Auto ARIMA as it considers seasonality irrespective of the trend.

![p258](/assets/p258.png)

MODELS

Holt's Exponential Smoothing Method

![p259](/assets/p259.png)

Holt exponential smoothing forecast (the green line) shows a downward trend in its forecast. The smoothing RMS is –80.83, the smoothing level is –0.8 and the smoothing slope is –0.3.  

Holt Winters Additive Method

![p260](/assets/p260.png)

![p261](/assets/p261.png)

The Holt Winters Additive method is also showing a downward trend. The trend looks less steep than that for Holt’s method. The smooth slope is 0.0526

Holt Winters Multiplicative Method

![p262](/assets/p262.png)

![p263](/assets/p263.png)

The Holt Winters Multiplicative method is also showing a horizontal line. There are some slight up and down trends showing in the data but not enough to define an upward or downward trend. The smooth slope is 2.3485

Auto ARIMA Method

![p264](/assets/p264.png)

![p265](/assets/p265.png)

The Auto ARIMA automatically performed a stepwise search and chose a model that had the lowest AIC. The best model chosen was SARIMAX (0,1,1) as shown above. This model has an AIC of 3123.791. Using this model, the prediction below was made, and ARIMA shows a horizontal price trend from the end of the training data. This model shows no trend and is the worst model of all the four models used to look at this stock.

![p266](/assets/p266.png)

To compare all four models, we considered the RMSE and MAPE for each of the models.

| METHOD | RMSE | MAPE |
|:---:|:---:|:---:|
| Holt’s exponential smoothing method  | 31.40 | 20.22 |
| Holt Winter’s additive method	| 92.75	| 74.50 |
| Holt Winter’s multiplicative method	| 53.95	| 45.18 |
| Auto ARIMA	| 115.90	| 45.87 |

Based on the RMSE and MAPE results shown below, Holt’s Exponential smoothing has the lowest RMSE and MAPE, making it the best forecasting model.

Regeneron Pharmaceuticals

![p267](/assets/p267.png)

The graph above shows the data split with the red line showing the training data and the black line showing the testing data for Regeneron.  

From the graph below, it can be noted that Regeneron is hard to tell whether it has a trend. Due to this uncertainty, we also considered Simple exponential smoothing. It can however be noted that Regeneron shows seasonality, but it is subjective to the eye and the data is only two years old, so we decided to consider both Holt Winters’ and Holt’s and chose the best model using RMSE and MAPE. We also used Auto ARIMA as it considers seasonality irrespective of the trend. 

![p268](/assets/p268.png)

MODELS

Simple Exponential Smoothing Method

![p269](/assets/p269.png)

The simple exponential smoothing shows a horizontal line for the forecast. This value went up from the last stock price in the training data, then it stayed the same. This is consistent with the validation data because the stock price has no trend but is bouncing off the same price range.   

Holt's Exponential Smoothing Method

![p270](/assets/p270.png)

Holt’s exponential smoothing forecast is showing an upward trend in its forecast. The smoothing RMS is –551.472, the smoothing level is –0.95 and the smoothing slope is –0.7.   

Holt’s Additive Method

![p271](/assets/p271.png)

![p272](/assets/p272.png)

Holt’s exponential smoothing forecast is showing an upward trend in its forecast with some up and down small trends that look like waves. The smoothing slope is 1.91879.  

Holt’s Multiplicative Method

![p273](/assets/p273.png)

![p274](/assets/p274.png)

Holt’s exponential smoothing forecast is showing an upward trend in its forecast with some up and down small trends that look like waves. The smoothing slope is 2.07255.

Auto ARIMA Method

![p275](/assets/p275.png)

![p276](/assets/p276.png)

The Auto ARIMA automatically performed a stepwise search and chose a model that had the lowest AIC. The best model chosen was ARIMA (1,1,1) as shown above. This model has an AIC of 3189.163. Using this model, the prediction below was made, and ARIMA shows a horizontal price trend from the end of the training data. This model shows no trend and is the worst model of all the four models used to look at Regeneron stock.

![p277](/assets/p277.png)

To compare all four models, we considered the RMSE and MAPE for each of the models.

| METHOD | RMSE | MAPE |
|:---:|:---:|:---:|
| Simple exponential smoothing forecast | 31.17 | 4.26 |
| Holt’s exponential smoothing method	| 42.49	| 5.35 |
| Holt Winter’s additive method | 71.26 | 10.63 |
| Holt Winter’s multiplicative method	| 70.41	| 10.49 |
| Auto ARIMA	| 495.50	| 11.94 |

From this comparison, Simple exponential smoothing has the lowest RMSE and MAPE making it the best for predicting stock price for Regeneron. 

ThermoFisher Scientific

![p278](/assets/p278.png)

The graph above shows the data split with the red line showing the training data and the black line showing the testing data for ThermoFisher.  

From the graph below, it can be noted that ThermoFisher has an upward trend. It can also be said that ThermoFisher shows seasonality, but it is subjective to the eye and the data is only two years old, so we decided to consider both Holt Winters’ and Holt’s and chose the best model using RMSE and MAPE. We also used Auto ARIMA as it considers seasonality irrespective of the trend. 

![p279](/assets/p279.png)

MODELS

Holt's Exponential Smoothing Method

![p280](/assets/p280.png)

Holt exponential smoothing forecast is showing an upward trend in its forecast. This upward trend continues although the testing data at some point starts experiencing a downward trend.  The smoothing RMS is –561.337, the smoothing level is –0.05 and the smoothing slope is –0.25.  

Holt Winters Additive Method

![p281](/assets/p281.png)

![p282](/assets/p282.png)

The Holt Winters Additive method is also showing an upward trend. The smoothing slope is 1.368.

Holt Winters Multiplicative Method

![p283](/assets/p283.png)

![p284](/assets/p284.png)

The Holt Winter Multiplicative method shows an upward trend with a smoothing slope of 2.3985.

Auto ARIMA Method

![p285](/assets/p285.png)

![p286](/assets/p286.png)

The Auto ARIMA automatically performed a stepwise search and chose a model that had the lowest AIC. The best model chosen was SARIMAX (1,1,0) as shown above. This model has an AIC of 2883.009. Using this model, the prediction below was made, and ARIMA shows a horizontal price trend from the end of the training data. This model shows no trend and is the worst model of all the four models used to look at ThermoFisher stock.

![p287](/assets/p287.png)

To compare all four models, we considered the RMSE and MAPE for each of the models.

| METHOD | RMSE | MAPE |
|:---:|:---:|:---:|
| Holt’s exponential smoothing method  | 44.12 | 6.31 |
| Holt Winter’s additive method	| 53.84	| 8.02 |
| Holt Winter’s multiplicative method	| 54.02	| 8.06 |
| Auto ARIMA	| 523.53	| 6.98 |

Based on the RMSE and MAPE results shown below, Holt’s Exponential smoothing has the lowest RMSE and MAPE, making it the best forecasting model.

West Pharmaceutical Services

![p288](/assets/p288.png)

The graph above shows the data split with the red line showing the training data and the black line showing the testing data.  

From the graph below, it can be noted that West Pharmaceuticals follows an upward trend. It can also be said that West Pharmaceuticals shows seasonality, but it is subjective to the eye and the data is only two years old, so we decided to consider both Holt Winters’ and Holt’s and chose the best model using RMSE and MAPE. We also used Auto ARIMA as it considers seasonality irrespective of the trend.

![p289](/assets/p289.png)

MODELS

Holt's Exponential Smoothing Method

![p290](/assets/p290.png)

Holt exponential smoothing forecast is showing a slight downward trend in its forecast. The smoothing RMS is –349.402, the smoothing level is –0.25 and the smoothing slope is –0.8.  

Holt Winters Additive Method

![p291](/assets/p291.png)

![p292](/assets/p292.png)

The Holt Winters Additive method is also showing a steep downward trend. The trend looks less steep than that for Holt’s method. The smoothing slope is 0.0705.

Holt Winters Multiplicative Method

![p293](/assets/p293.png)

![p294](/assets/p294.png)

The Holt Winter Multiplicative method shows an upward trend with a smoothing slope of 0.00428.  This trend conflicts with the downward trend seen in Holt Winters Additive Method and Holt’s Exponential Smoothing. 

Auto ARIMA Method

![p295](/assets/p295.png)

![p296](/assets/p296.png)

The Auto ARIMA automatically performed a stepwise search and chose a model that had the lowest AIC. The best model chosen was SARIMAX (0,1,0) as shown above. This model has an AIC of 2497.497. Using this model, the prediction below was made, and ARIMA shows a horizontal price trend from the end of the training data. This model shows no trend and is the worst model of all the four models used to look at West Pharmaceuticals stock.

![p297](/assets/p297.png)

To compare all four models, we considered the RMSE and MAPE for each of the models.

| METHOD | RMSE | MAPE |
|:---:|:---:|:---:|
| Holt’s exponential smoothing method  | 29.69 | 5.77 |
| Holt Winter’s additive method	| 110.64	| 25.09 |
| Holt Winter’s multiplicative method	| 39.56	| 8.50 |
| Auto ARIMA	| 351.76	| 6.01 |

Based on the RMSE and MAPE results shown below, Holt’s Exponential smoothing has the lowest RMSE and MAPE, making it the best forecasting model.

Predictions - Future Stock Price

After building various models like Simple Exponential Smoothing Method, Holt's Exponential Smoothing Method, Holt Winters' additive method with trend and seasonality, Holt Winter's multiplicative method with trend and seasonality, Auto ARIMA Method for companies based on the individual company’s trend and seasonality, we found that ‘Holt's Exponential Smoothing Method’ gave best MAPE, RMSE for 11 out of the 13 companies. For 2 companies Hologic and Regeneron Pharmaceutical ‘Simple Exponential Smoothing Method’, ‘Holt's Exponential Smoothing Method’ gave similar best results because the trend hasn’t been clear and consistent. So below we used these best models for the respective companies to predict their future stock price trend.

Pfizer: Holt's Exponential Smoothing Method

![p298](/assets/p298.png)

Pfizer’s future stock price forecast trend looks quite promising with a Smoothing Level of 0.05 & Smoothing Slope of 0.6. The stock price of Pfizer is expected to go up from its current value of 49.2 to 59.96 

Abiomed: Holt's Exponential Smoothing Method

![p299](/assets/p299.png)

The stock price of Abiomed is expected to go up from the current value of 305.61 and then drop finally ending at 298.33 in 3 months.

AstraZeneca: Holt's Exponential Smoothing Method

![p300](/assets/p300.png)

The stock price of AstraZeneca is expected to drop from its current value of 60.9 to 57.62

BioNTech: Holt's Exponential Smoothing Method

![p301](/assets/p301.png)

The stock price of BioNTech is expected to go up from the current value of 137.27 and then drop finally ending at 182.68 in 3 months.

Bio-Rad Laboratories: Holt's Exponential Smoothing Method

![p302](/assets/p302.png)

The stock price of Bio-Rad Laboratories is expected to go up from the current value of 541.34 and then drop finally ending at 556.87 in 3 months.

Hologic: Simple Exponential Smoothing Method, Holt's Exponential Smoothing Method

![p303](/assets/p303.png)

![p304](/assets/p304.png)

The stock price is expected to stay still or surge from the current value of 70.27 to 73.09. More historical data is required to confirm the trend for this company.

Johnson & Johnson: Holt's Exponential Smoothing Method

![p305](/assets/p305.png)

The stock price of Bio-Rad Laboratories is expected to drop from the current value of 169.66 and then rise finally ending at 172.94 in 3 months.

Lyondell Basell Industries: Holt's Exponential Smoothing Method

![p306](/assets/p306.png)

The stock price of Lyondell Basell Industries is expected to drop from the current value of 99.73 and then rise finally ending at 101.70 in 3 months.

Moderna: Holt's Exponential Smoothing Method

![p307](/assets/p307.png)

The stock price of Moderna is expected to go up from the current value of 139.52 and then drop finally ending at 98.20 in 3 months

Novavax: Holt's Exponential Smoothing Method

![p308](/assets/p308.png)

The stock price of Novavax is expected to go up from the current value of 77.77 and then drop finally ending at 92.76 in 3 months.

Regeneron Pharmaceutical: Simple Exponential Smoothing Method, Holt's Exponential Smoothing Method

![p309](/assets/p309.png)

![p310](/assets/p310.png)

The stock price of Regeneron Pharmaceutical is expected to stay still or drop from the current value of 630.36 and then rise finally ending at 655.58 in 3 months. More historical data is required to confirm the trend for this company.

ThermoFisher Scientific: Holt's Exponential Smoothing Method

![p311](/assets/p311.png)

The stock price of ThermoFisher Scientific is expected to surge from the current value of 538.25 to 624.04.

West Pharmaceutical Services: Holt's Exponential Smoothing Method

![p312](/assets/p312.png)

The stock price of West Pharmaceutical Services is expected to go up from the current value of 371.47 and then drop finally ending at 397.28 in 3 months.

## Conclusion and Discussion

Disclaimer: The results below are for academic research purposes only and should not be used to make real time investments. Do your due diligence when making investments. We are not in any way associated with any of these companies.

Stock Price in 3 months:

| Company | Current Stock Price | Stock Price at end of 3 months | Difference inStock price |
|:---:|:---:|:---:|:---:|
| Pfizer | 49.2 | 59.96 | 10.76 |
| Abiomed | 305.61 | 298.33 | -7.28 |
| AstraZeneca | 60.9 | 57.62 | -3.28 |
| BioNTech | 137.27 | 182.68 | 45.41 |
| Bio-Rad Laboratories | 541.34 | 556.87 | 15.53 |
| Hologic | 70.27 | 73.09 | 2.82 |
| Johnson & Johnson | 169.66 | 172.94 | 3.28 |
| Lyondell Basell Industries | 99.73 | 101.70 | 1.97 |
| Moderna | 139.52 | 98.20 | -41.32 |
| Novavax | 77.77 | 92.76 | 14.99 |
| Regeneron Pharmaceutical | 630.36 | 655.58 | 25.22 |
| ThermoFisher Scientific | 538.25 | 624.04 | 85.79 |
| West Pharmaceutical Services | 371.47 | 397.28 | 25.81 |

From the above predicted values of Stock prices of the 13 companies at the end of 3 months, we observe that

•	ThermoFisher Scientific, BioNTech are excellent investment opportunities, followed by West Pharmaceutical Services and Regeneron Pharmaceutical. It's best to hold these stocks and invest more in these 4 companies.

•	Bio-Rad Laboratories, Novavax and Pfizer are expected to give decent profits of around $10 per unit stock. 

•	Johnson & Johnson, Hologic and Lyondell Basell Industries are expected to stay the same without any profit or loss, so its users can hold on to these stocks.

•	Abiomed and AstraZeneca stock price is expected to drop, but not drastically.

•	Moderna’s stock price is expected to drop a whopping $41 per unit by the end of 3 months. It's better to sell stocks like these.

REFERENCES

https://www.investopedia.com/articles/basics/04/100804.asp

https://www.investopedia.com/articles/investing/082614/how-stock-market-works.asp

Hayes, A. (2021, November 13). A breakdown of how the Stock Market Works. Investopedia. Retrieved https://www.investopedia.com/articles/investing/082614/how-stock-market-works.asp 

https://www.intechopen.com/chapters/72381

https://towardsdatascience.com/forecasting-time-series-data-stock-price-analysis-324bcc520af5

https://github.com/pujappathak/Retail-Giant-Sales-Forecasting/blob/main/Puja%20Pathak%20-%20Retail%20Giant%20Sales%20Forecasting%20Assignment.ipynb

https://towardsdatascience.com/time-series-prediction-beyond-test-data-3f4625019fd9
