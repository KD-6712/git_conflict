import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math

stocks = pd.read_csv('constituents_csv.csv')
IEX_CLOUD_API_TOKEN = 'Tpk_059b97af715d417d9f49f50b51b1c448'
symbol='AAPL'
api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote?token={IEX_CLOUD_API_TOKEN}'
data = requests.get(api_url).json()
data

