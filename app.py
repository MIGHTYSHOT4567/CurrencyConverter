import streamlit as st
from currency_converter import CurrencyConverter
import pycountry

st.write('# <span style = "color: blue; text-align: center;">Currency Converter</span>',unsafe_allow_html = True)
st.image("logo.png",caption = "" , width = 150 , use_column_width = True)



st.write("_____")

converter = CurrencyConverter ()

currencies = converter.currencies

currencies = converter.currencies

currency_to_country = {currency: pycountry.currencies.get(alpha_3 = currency).name for currency in currencies if pycountry.currencies.get(alpha_3 = currency)}

amount = st.number_input("Enter amount:", min_value = 0.0)
from_currency = st.selectbox("From currency:", options = list(currency_to_country.keys()))
from_country = currency_to_country.get(from_currency, "Unknown")
st.write(f"From country:{from_country}")
to_currency = st.selectbox("To currency:",options = list(currency_to_country.keys()))
to_country = currency_to_country.get(to_currency,"Unknown")
st.write(f"To country:{to_currency}")


converted_amount = converter.convert(amount, from_currency, to_currency)
if st.button('Convert Currency'):
    st.write(f"Converted amount: {converted_amount:.2f} {to_currency}")