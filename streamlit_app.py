import streamlit
streamlit.title('Web-Data Application for Diner')
streamlit.header('Breakfast Favourites')
streamlit.text('🥣 Omega3 and Blueberry Oat meal')
streamlit.text('🥗 Kale Spinach and Rocket Smoothie')
streamlit.text('🐔 Hard Boiled free range eggs')
streamlit.text('🥑 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list= pandas.read_csv(" https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
