import random
from turtle import onclick
import streamlit as st
import pandas as pd
import numpy as np
import uuid
<<<<<<< HEAD
=======

people = [['Aditya', 'banan'], ['Ad', 'apple']]

>>>>>>> 97655155d0b4f3127204b68f3a9f7540dfbdddc5

def populate_people():
    st.header("People")
    # list of people in community + items willing to barter
    df = pd.DataFrame(people, columns=['Seller', 'Commodity Selling'])
    st.table(df)


def handle_registration():
    with st.sidebar:
        st.subheader("Registration")
        reg_form = st.form(key="reg")
        fname = reg_form.text_input("First Name:")
        lname = reg_form.text_input("Last Name:")
        email = reg_form.text_input("Email:")
        community = reg_form.text_input("Community:")
        items = reg_form.text_input("Pick one item")
        quantity = reg_form.slider("Pick how many", 0, 25)
        address = reg_form.text_area("Enter Address:")
        # creating a submit button
        submit = reg_form.form_submit_button("Submit")
<<<<<<< HEAD
    if(submit):
        people.append([str(uuid.uuid4()), 'Apple'])
=======
        st.session_state["first_name"] = fname
        st.session_state["last_name"] = lname
        st.session_state["item"] = items
        st.session_state["quantity"] = quantity

    if submit:
        people.append([st.session_state['first_name'],st.session_state['last_name']])
        print(people)
        st.session_state['people'] = people
>>>>>>> 97655155d0b4f3127204b68f3a9f7540dfbdddc5
        populate_people()


def main():
    st.write("# BigBarter MarketPlace")  # st.title('Avocado Prices dashboard')
    st.markdown(
        """
    This is a decentralized item-to-item bartering system within your custom community.\n
    First register to get started!

    """
    )

    request = st.button("Make Request")
<<<<<<< HEAD
    community = st.button("Join Community")
=======
>>>>>>> 97655155d0b4f3127204b68f3a9f7540dfbdddc5

    if request:
        st.subheader("Requests")
        # display all requests with approve and reject button
        # if approved, add transaction to transactions table
        # update quantities of commodities
        req_form = st.form(key="req")
<<<<<<< HEAD
        fname = req_form.text_input("Seller Id:")
=======
        fname = req_form.text_input("First Name:")
        lname = req_form.text_input("Last Name:")
>>>>>>> 97655155d0b4f3127204b68f3a9f7540dfbdddc5
        quantity = req_form.text_input("Quantity:")
        item = req_form.text_input("Item:")
        # creating a submit button
        submit = req_form.form_submit_button("Submit")
<<<<<<< HEAD

        # send request information
        request = True
    
    if community:
        st.subheader('Community')
        com_form = st.form(key='com')
        com = com_form.text_input('Community:')
        submit = com_form.form_submit_button("Submit")
        community = True
=======
>>>>>>> 97655155d0b4f3127204b68f3a9f7540dfbdddc5

        # send request information
        request = True

<<<<<<< HEAD
=======
    populate_people()
>>>>>>> 97655155d0b4f3127204b68f3a9f7540dfbdddc5
    option = st.sidebar.selectbox(
        "Where next?", ("home", "registration", "transactions", "requests")
    )
    if option == "home":
        with st.sidebar:
            st.subheader("Home")
            st.write(
                "Welcome to BigBarter Marketplace! Feel free to make an account with your current inventory"
                + "and begin bartering with people in your community"
            )
    elif option == "transactions":
        with st.sidebar:
            st.subheader("Previous Transactions")

            num_rows = 100
            owner = [str(uuid.uuid4()) for _ in range(num_rows)]
            seller = [str(uuid.uuid4()) for _ in range(num_rows)]
            buyer = [str(uuid.uuid4()) for _ in range(num_rows)]

            choices = ['Apples', 'Eggs', 'Bread', 'Cow', 'Ice', 'Water', 'Horses', 'Shirts']
            commodity_bought = [np.random.choice(choices) for _ in range(num_rows)]
            commodity_bought_amt = [np.random.randint(low=1, high=50) for _ in range(num_rows)]

            commodity_sold = [np.random.choice(choices) for _ in range(num_rows)]
            commodity_sold_amt = [np.random.randint(low=1, high=50) for _ in range(num_rows)]

            df = pd.DataFrame({
                "Owner": owner,
                'Seller': seller,
                'Buyer': buyer,
                'Commodity Bought': commodity_bought,
                'Commodity Bought Amount': commodity_bought_amt,
                'Commodity Sold': commodity_sold,
                'Commodity Sold Amount': commodity_sold_amt
            }

            )
            st.table(df)
<<<<<<< HEAD
=======

>>>>>>> 97655155d0b4f3127204b68f3a9f7540dfbdddc5
    elif option == "registration":
        handle_registration()
    elif option == "requests":
        with st.sidebar:
            st.subheader("Requests")
            # display all requests with approve and reject button
            # if approved, add transaction to transactions table
            # update quantities of commodities

            df = pd.DataFrame({
                'Buyer': str(uuid.uuid4()),
                'Seller': str(uuid.uuid4()),
                'Commodity Buying': "Apples",
                'Commodity Buying Amount': 10,
                'Commodity Requesting': 'Eggs',
                'Commodity Requesting Amount': 10
            }, index=[0])
            st.table(df)
<<<<<<< HEAD
=======

>>>>>>> 97655155d0b4f3127204b68f3a9f7540dfbdddc5
            col1, col2 = st.sidebar.columns([1, 1])

            with col1:
                st.button("Accept", kwargs={
                    'clicked_button_ix': 1, 'n_buttons': 2
                })
            with col2:
                st.button("Reject", kwargs={
                    'clicked_button_ix': 2, 'n_buttons': 2
                })
<<<<<<< HEAD
            
=======
>>>>>>> 97655155d0b4f3127204b68f3a9f7540dfbdddc5


if __name__ == "__main__":
    main()

<<<<<<< HEAD
    # store Name (first/last), items
=======
    # store Name (first/last), items
>>>>>>> 97655155d0b4f3127204b68f3a9f7540dfbdddc5
