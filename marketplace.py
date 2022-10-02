
from turtle import onclick
import streamlit as st
import pandas as pd
import numpy as np

people = []
def populate_people():
    st.header('People')
    #list of people in community + items willing to barter
    df = pd.DataFrame(
    people,
    columns=('col %d' % i for i in range(2)))
    st.table(df)

def handle_registration():
    with st.sidebar:
        st.subheader('Registration')
        reg_form=st.form(key='reg')
        fname=reg_form.text_input('First Name:')
        lname=reg_form.text_input('Last Name:')
        email=reg_form.text_input('Email:')
        community=reg_form.text_input('Community:')
        items=reg_form.text_input('Pick one item')
        quantity=reg_form.slider('Pick how many',0,25)
        address=reg_form.text_area('Enter Address:')
        # creating a submit button
        submit=reg_form.form_submit_button('Submit')
        st.session_state['first_name'] = fname
        st.session_state['last_name'] = lname
        st.session_state['item'] = items
        st.session_state['quantity'] = quantity

def main():
    st.write('# BigBarter MarketPlace')  #st.title('Avocado Prices dashboard')
    st.markdown('''
    This is a decentralized item-to-item bartering system within your custom community.\n
    First register to get started!

    ''')
    
    request = st.button("Make Request")
    if request:
        st.subheader('Requests')
        #display all requests with approve and reject button
        #if approved, add transaction to transactions table
        #update quantities of commodities
        req_form=st.form(key='req')
        fname=req_form.text_input('First Name:')
        lname=req_form.text_input('Last Name:')
        quantity=req_form.text_input('Quantity:')
        item=req_form.text_input('Item:')
        # creating a submit button
        submit=req_form.form_submit_button('Submit')


        #send request information
        request = False
    populate_people()
    option = st.sidebar.selectbox('Where next?', ('home','registration','transactions','requests'))
    if option == 'home':
        with st.sidebar:
            st.subheader('Home')
            st.write('Welcome to BigBarter Marketplace! Feel free to make an account with your current inventory' + 
                    'and begin bartering with people in your community')
    elif option == 'transactions':
        with st.sidebar:
            st.subheader('Previous Transactions')
            df = pd.DataFrame(
            np.random.randn(10, 5),
            columns=('col %d' % i for i in range(5)))
            st.table(df)
    elif option == 'registration':
        handle_registration()
    elif option == 'requests':
        with st.sidebar:
            st.subheader('Requests')
            #display all requests with approve and reject button
            #if approved, add transaction to transactions table
            #update quantities of commodities


if __name__ == '__main__':
    main()


    #store Name (first/last), items