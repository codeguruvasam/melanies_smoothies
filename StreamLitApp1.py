import streamlit as st
from snowflake.snowpark.context import get_active_session

# Write directly to the app
#st.title(f"Customize Your Smoothie!")
st.title(":cup_with_straw: Smoothie Time! :cup_with_straw:")
st.write(
  """Choose fruits you want in your custom Smoothie!
    """
)

import streamlit as st

option = st.selectbox(
    "What is your favorite fruit?",
    ("Banana", "Strawberries", "Peaches"),
)

st.write("You favorite fruit is:", option)

session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options")
st.dataframe(data=my_dataframe, use_container_width=True)