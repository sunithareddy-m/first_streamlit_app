import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My new Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega3 and Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard Boiled & Free Range Egg')
streamlit.text('🥑🍞 Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')

#Let's put a pick list here so that they can pick the fruit they want to include
fruits_selected=streamlit.multiselect("Pick Some Fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]

#display the table - fruits list
streamlit.dataframe(fruits_to_show)

#create a function for repeatable code
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

#new section to display fruityvice API response
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information")
  else:
    back_from_function=get_fruityvice_data(this_fruit_choice)
    streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()

streamlit.stop()

#import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contins:")
streamlit.dataframe(my_data_rows)
#Allow the end user to add a fruit to the list
add_my_fruit=streamlit.text_input('What fruit would you like add?','jackfruit')
streamlit.write('Thx for adding ', add_my_fruit)

#This will not work correctly  but just go with it now
my_cur.execute("insert into fruit_load_list values('from streamlit')")
