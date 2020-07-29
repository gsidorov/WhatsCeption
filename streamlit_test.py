import yfinance as yf
import streamlit as st
import pandas as pd
from methods import *
from charts import *

"""
https://www.youtube.com/watch?v=skpiLtEN3yk [How To Deploy Streamlit Apps (Using Heroku)]

https://www.youtube.com/watch?v=ZZ4B0QUHuNc [How to Build Your First Data Science Web App in Python (Streamlit Tutorial Part 1)]

https://towardsdatascience.com/quickly-build-and-deploy-an-application-with-streamlit-988ca08c7e83

"""

st.write("""
# WhatsCeption by gleb.ai
Shown are the details of your **Whatsapp conversation**
Enjoy!
""")

''' By Gleb, checking the documentation https://docs.streamlit.io/en/stable/getting_started.html'''
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'Longest Word': [1, 2, 3, 4],
    'Most Used Emoji': [10, 20, 30, 40]
}))

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'GOOGL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume
""")
st.line_chart(tickerDf.Volume)