# This creates the page for displaying data visualizations.
# It should read data from both 'data.csv' and 'data.json' to create graphs.

import streamlit as st
import pandas as pd
import json # The 'json' module is needed to work with JSON files.
import os   # The 'os' module helps with file system operations.

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Visualizations",
    page_icon="📈",
)

# PAGE TITLE AND INFORMATION
st.title("Data Visualizations 📈")
st.write("This page displays graphs based on the collected data.")


# DATA LOADING
# A crucial step is to load the data from the files.
# It's important to add error handling to prevent the app from crashing if a file is empty or missing.

st.divider()
st.header("Load Data")

# TO DO:
# 1. Load the data from 'data.csv' into a pandas DataFrame.
#    - Use a 'try-except' block or 'os.path.exists' to handle cases where the file doesn't exist.
# 2. Load the data from 'data.json' into a Python dictionary.
#    - Use a 'try-except' block here as well.
csv_file = "data.csv"
json_file = "data.json"
my_file = "MyNewData.csv"

data_df = None
json_data = None
my_file = None

try:
    if os.path.exists(csv_file):
        data_df = pd.read_csv(csv_file)
        st.success(f"Loaded CSV data from **{csv_file}**")
    else:
        st.error(f"CSV file '{csv_file}' not found.")
except Exception as error:
    st.error(f"Error loading JSON file: {error}")

st.info("Your inputted data will be shown in Graph 1.")


# GRAPH CREATION
# The lab requires you to create 3 graphs: one static and two dynamic.
# You must use both the CSV and JSON data sources at least once.

st.divider()
st.header("Graphs")

# GRAPH 1: STATIC GRAPH
st.subheader("Graph 1: Input Graph") # CHANGE THIS TO THE TITLE OF YOUR GRAPH
# TO DO:
# - Create a static graph (e.g., bar chart, line chart) using st.bar_chart() or st.line_chart().
# - Use data from either the CSV or JSON file.
# - Write a description explaining what the graph shows.
if data_df is not None and not data_df.empty:
    st.bar_chart(data_df.set_index(data_df.columns[0]))
    st.caption("This bar chart shows the collected data from the CSV file.")
else:
    st.warning("CSV data is errored. Please submit data in the Survey page.")

st.warning("Categories and values are as inputted.")


# GRAPH 2: DYNAMIC GRAPH
st.subheader("Graph 2: Filtered View") # CHANGE THIS TO THE TITLE OF YOUR GRAPH
# TODO:
# - Create a dynamic graph that changes based on user input.
# - Use at least one interactive widget (e.g., st.slider, st.selectbox, st.multiselect).
# - Use Streamlit's Session State (st.session_state) to manage the interaction.
# - Add a '#NEW' comment next to at least 3 new Streamlit functions you use in this lab.
# - Write a description explaining the graph and how to interact with it.
if json_data is not None and not json_data.empty:
    #NEW - use streamlit select box for user input
    category_list = json_data[json_data.columns[0]] == st.session_state.selected_category]
    selected_category = st.selectbox("Select a category to display:", category_list, key ="category_select")
    #NEW - store the selected category in session state
    st.session_state.selected_category = selected_category

    filtered_df = json_data[json_df[json_df.columns[0]] == st.session_state.selected_category]
    #NEW - create line chart to act as dynamic graph
    st.line_chart(filtered_df.set_index(filtered_df.columns[0]))
    st.caption)f"This dynamic line chart updates based on the selected category: **{selected category}**")
st.warning("JSON data unavailable.")


# GRAPH 3: DYNAMIC GRAPH
st.subheader("Graph 3: My Own Data") # CHANGE THIS TO THE TITLE OF YOUR GRAPH
# TO DO:
# - Create another dynamic graph.
# - If you used CSV data for Graph 1 & 2, you MUST use JSON data here (or vice-versa).
# - This graph must also be interactive and use Session State.
# - Remember to add a description and use '#NEW' comments.
if my_file is not None and not my_file.empty:
    #NEW - use streamlit select box for user input
    category_list = my_file[my_file.columns[0]] == st.session_state.selected_category]
    selected_category = st.selectbox("Select a coding language to display:", category_list, key ="category_select")
    #NEW - store the selected category in session state
    st.session_state.selected_category = selected_category

    filtered_df = my_file[my_file[my_file.columns[0]] == st.session_state.selected_category]
    #NEW - create line chart to act as dynamic graph
    st.line_chart(filtered_df.set_index(filtered_df.columns[0]))
    st.caption)f"This dynamic line chart updates based on the selected category: **{selected category}**")
st.warning("My own data unavailable.")
st.warning("Graph pending.")
