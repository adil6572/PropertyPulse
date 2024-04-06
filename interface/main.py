import json
import streamlit as st
from utils import scrape_realtor_properties, transform_response
import pandas as pd
from io import BytesIO

st.title('PropertyPulse')
st.write('Real estate data scraper')

# Offer options to choose from the website to scrape
website_choice = st.radio("Select a website to scrape:", ('Realtor', 'Zillow'))

# Create a unique session state to persist data across app refreshes
session_state = st.session_state.setdefault('data', {'df': None, 'realtor_data': None})

if website_choice == 'Realtor':
    realtor_url = st.text_input('Enter Realtor URL:')
    if st.button('Scrape'):
        if realtor_url:
            with st.spinner('Scraping data from Realtor...'):
                realtor_data, response_message = scrape_realtor_properties(realtor_url)
            if realtor_data is not None:
                df = transform_response(realtor_data)
                session_state['df'] = df
                session_state['realtor_data'] = realtor_data
                st.dataframe(df)
        else:
            st.warning('Please enter a valid Realtor URL')

elif website_choice == 'Zillow':
    zillow_url = st.text_input('Enter Zillow URL:')
    if st.button('Scrape'):
        if zillow_url:
            with st.spinner('Scraping data from Zillow...'):
                zillow_data = scrape_realtor_properties(zillow_url)
            st.json(zillow_data)
        else:
            st.warning('Please enter a valid Zillow URL')

# Download button
if session_state['df'] is not None:
    download_format = st.selectbox("Select Download Format", ("JSON", "CSV", "Excel"))
    filename = st.text_input("Enter filename (without extension):", "realtor_data")
    if download_format == "JSON":
        json_data = session_state['realtor_data']
        json_file = json.dumps(json_data, indent=4)
        st.download_button(label="Download JSON", data=json_file.encode(), file_name=f"{filename}.json", mime="application/json")
    elif download_format == "CSV":
        csv = session_state['df'].to_csv(index=False)
        st.download_button(label="Download CSV", data=csv.encode(), file_name=f"{filename}.csv", mime="text/csv")
    elif download_format == "Excel":
        excel_buffer = BytesIO()
        session_state['df'].to_excel(excel_writer=excel_buffer, index=False)
        excel_buffer.seek(0)
        st.download_button(label="Download Excel", data=excel_buffer, file_name=f"{filename}.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
