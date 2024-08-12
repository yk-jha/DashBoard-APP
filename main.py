import streamlit as st
import pandas as pd
import matplotlib.pyplot as plot
st.title("Simple Data Dashboard")

uploaded_file = st.file_uploader("Upload any CSV file" , type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Data Preview")
    st.write(df.head())
    st.subheader("Data Summary")
    st.write(df.describe())
    st.subheader("Filter the Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select Columns to Filter by" , columns)
    unique_vals = df[selected_column].unique()
    selected_vals = st.selectbox("Select Value" , unique_vals)
    
    filtered_df = df[df[selected_column] == selected_vals]
    st.write(filtered_df)
    
    st.subheader("Plot The Data")
    x_column = st.selectbox("Select The X-axis"  , columns)
    y_column = st.selectbox("Select The Y-axis"  , columns)
    
    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])
else:
    st.write("Waiting on File Upload......")
        