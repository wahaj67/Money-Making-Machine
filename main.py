import streamlit as st 
import random 
import time
import requests

st.title('💸 Money Making Machine')

def generate_money():
    return random.randint(1,1000)

st.subheader('🤑 Instant Cash Generator')
if st.button('Generate Money'):
    with st.spinner('Counting your money...'):
        time.sleep(2)
        amount = generate_money()
    st.info(f'you made ${amount}!')


def fetch_side_hustles():
    try:
        response = requests.get('http://127.0.0.1:8000/side_hustles?apiKey=12345')
        if response.status_code == 200:
            hustles = response.json()
            return hustles['side_hustles']
        else:
            return "Freelancing"
        
    except:
        return ('Something went wrong!')
    

st.subheader('💼 Side Hustles Ideas')
if st.button('Generate Ideas'):
    with st.spinner('Thinking for a hustle...'):
        time.sleep(2)
        hustkes = fetch_side_hustles()
    st.info(f"{hustkes}")


def get_money_quotes():
    try:
        response = requests.get('http://127.0.0.1:8000/money_quotes?apiKey=12345678911')
        if response.status_code == 200:
            quotes = response.json()
            return quotes['money_quotes']
        else:
            return 'no quotes found!'
    except:
        return ('Something went wrong')
    

st.subheader('💬 Money Quotes')
if st.button('Get Inspired'):
    with st.spinner('Thinking a great quote...'):
        time.sleep(2)
    
        quotes = get_money_quotes()
    st.info(f'{quotes}')

