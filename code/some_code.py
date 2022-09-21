#!/usr/bin/env python
# coding: utf-8
# In[ ]:
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date, datetime, timedelta
from tqdm import tqdm
# In[ ]:
link = "https://finance.yahoo.com/quote/PFE/history?p=PFE"
#link = "https://finance.yahoo.com/quote/ABMD?p=ABMD&.tsrc=fin-srch"
#link = "https://finance.yahoo.com/quote/AZN?p=AZN&.tsrc=fin-srch"
#link = "https://finance.yahoo.com/quote/BNTX?p=BNTX&.tsrc=fin-srch"
#link = "https://finance.yahoo.com/quote/BIO?p=BIO&.tsrc=fin-srch"
#link = "https://finance.yahoo.com/quote/HOLX?p=HOLX&.tsrc=fin-srch"
#link = "https://finance.yahoo.com/quote/JNJ?p=JNJ&.tsrc=fin-srch"
#link = "https://finance.yahoo.com/quote/LYB?p=LYB&.tsrc=fin-srch"
#link = "https://finance.yahoo.com/quote/MRNA?p=MRNA&.tsrc=fin-srch"
#link = "https://finance.yahoo.com/quote/NVAX?p=NVAX&.tsrc=fin-srch"
#link = "https://finance.yahoo.com/quote/REGN?p=REGN&.tsrc=fin-srch"
#link = "https://finance.yahoo.com/quote/TMO?p=TMO&.tsrc=fin-srch"
#link = "https://finance.yahoo.com/quote/WST?p=WST&.tsrc=fin-srch"
driver = webdriver.Firefox(executable_path=r'C:\Users\tejas\OneDrive\Documents\Courses\Fall 2021\MSIS5193 - Programming 2\geckodriver-v0.30.0-win64\geckodriver.exe')
driver.maximize_window()
driver.get(link)
# In[ ]:
table = driver.find_element_by_xpath(xpath='//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table')
