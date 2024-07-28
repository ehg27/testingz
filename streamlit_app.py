import streamlit as st
import gspread
from google.oauth2 import service_account

# Create a connection object.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
    ],
)
client = gspread.authorize(credentials)

# Open the Google Sheet
sheet = client.open("Your Sheet Name").sheet1

st.title('Update Google Sheet')

# Input fields
name = st.text_input('Enter name')
age = st.number_input('Enter age', min_value=0, max_value=120)

if st.button('Submit'):
    # Update the sheet when the button is pressed
    sheet.append_row([name, age])
    st.success('Data added to Google Sheet!')