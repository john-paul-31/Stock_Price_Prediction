import pandas as pd 
import streamlit as st 
import yfinance as yf 
from datetime import datetime

#ticker_df = pd.read_csv("tickers.csv")

#Header
st.write(""" 

# Stock Price Prediction

Below are the Tesla Stocks's *Closing Price* and *Volume of Shares* Traded

""")


#Adding Image
st.image("./logo.jpg")

#Getting the Start Date
start_date = st.date_input("Input Start Date")

# Setting End date as today's date
end_date = datetime.now().strftime("%Y-%m-%d")

#Ticker Selection
ticker_symbol = "TSLA"
#ticker_selected = st.selectbox('Select the Ticker Symbol', ticker_df['Ticker'])



#Extract Data
ticker_data = yf.Ticker(ticker_symbol)
#ticker_data = yf.Ticker(ticker_selected)
ticker_df = ticker_data.history(period = "1d", start = f"{start_date}", end = end_date) 

#Display Data as df in the webpage
st.dataframe(ticker_df)

#Line Chart
st.write("""
## Daily Closing Price Chart
""")
st.line_chart(ticker_df.Close)
st.write("""
## Volume of Shares Traded
""")
st.line_chart(ticker_df.Volume)


#Expander to add Notes/Explanations
with st.expander("Readme"):
    st.write("""
        - The above chart shows the Tesla stock prices
        - You can refer the line chart to understand the trend
    """)