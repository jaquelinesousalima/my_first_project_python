import streamlit as st

customer = st.text_input("Type name of the customer: ")
st.info("The name of costumer is: " + customer)


file = open("customer.txt", "w", encoding="utf-8")

