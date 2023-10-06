import streamlit as st
import yfinance as yf
import datetime

st.title("welcome to stock market")


#ticker_symbol ='AAPL'

ticker_symbol=st.text_input("enter stock symbol","AAPL")

#start_date = '2009-12-31'

col1 ,col2 =st.columns(2)
with col1:


  start_date = st.date_input("Please Enter Start Date",datetime.date(2019,1,1))
with col2:
  end_date = st.date_input("Please Enter End Date",datetime.date(2022,12,31))


#end_date = "2010-12-31"

ticker_data = yf.Ticker(ticker_symbol)

ticker_df = ticker_data.history(period = "1mo",start=f"{start_date}",end = f"{end_date}")

col1,col2 = st.columns(2)

with col1:
    st.write("# Daily closing Price")
    st.line_chart(ticker_df['Close'])

with col2:
    st.write("# Daily High Price")
    st.line_chart(ticker_df['High'])

#st.dataframe(ticker_df)

#st.write("# Daily closing Price")
#st.line_chart(ticker_df['Close'])


#st.write("# Daily High Price")
#st.line_chart(ticker_df['High'])