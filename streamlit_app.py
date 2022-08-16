import streamlit
streamlit.title('My new Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega3 and Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard Boiled & Free Range Egg')
streamlit.text('🥑🍞 Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')

#Let's put a pick list here so that they can pick the fruit they want to include
streamlit.multiselect("Pick Some Fruits:",list(my_fruit_list.index))

#display the table - fruits list
streamlit.dataframe(my_fruit_list)
