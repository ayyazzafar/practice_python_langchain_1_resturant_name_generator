import os

import streamlit as st

from langchain_helper import generate_restaurant_name_and_items
from secret_key import open_api_key

os.environ["OPENAI_API_KEY"] = open_api_key
st.title('Restaurant Name Generator')

cuisine = st.sidebar.selectbox('Select a cuisine', ['Chinese', 'Indian', 'Italian', 'Japanese', 'Korean', 'Mexican', 'Thai', 'Vietnamese'])

if cuisine:
    restaurant = generate_restaurant_name_and_items(cuisine)
    st.header(restaurant['restaurant_name'].strip())
    menu_items = restaurant['menu_items'].split(',')
    st.subheader('**Menu Items**')

    for item in menu_items:
        st.write('- '+item.strip())


