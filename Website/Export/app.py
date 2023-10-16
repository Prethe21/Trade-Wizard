import streamlit as st
import pandas as pd
import plotly.express as px

# Read the "Train dataset" to get options for "Product/Sector" and "Reporting Economy"
train_dataset = pd.read_excel("Train dataset.xlsx")  # Change the file name to the actual dataset

# Extract unique values for Product/Sector and Reporting Economy
unique_sectors = train_dataset["Product/Sector"].unique()
unique_economies = train_dataset["Reporting Economy"].unique()

# Streamlit app title
st.title("Dynamic Visualization App with Hardcoded Datasets")

# Hardcoded Datasets
dataset1 = pd.read_excel("2018.xlsx")
dataset2 = pd.read_excel("2019.xlsx")
dataset3 = pd.read_excel("2020.xlsx")

# Dictionary to store datasets
datasets = {
    'Dataset 1': dataset1,
    'Dataset 2': dataset2,
    'Dataset 3': dataset3
}

# Upload dataset
uploaded_file = st.file_uploader("Upload Dataset (CSV or Excel)", type=["csv", "xlsx"])

# Check if a file is uploaded
if uploaded_file is not None:
    # Read the uploaded file into a DataFrame
    selected_df = pd.read_excel(uploaded_file, engine='openpyxl')  # Use engine='openpyxl' for Excel files

    # Streamlit app title
    st.title("Dynamic Visualization App with Uploaded Dataset")

    # Select visualization type
    visualization_type = st.selectbox("Select Visualization Type:", ["Bar Chart", "Pie Chart", "Line Chart"], key="uploaded_vis_type")

    # Check if a visualization type is selected
    if visualization_type == "Bar Chart":
        # Select columns for X and Y axes
        x_column = st.selectbox("Select X-axis Data:", selected_df.columns, key="uploaded_x_column")
        y_column = st.selectbox("Select Y-axis Data:", selected_df.columns, key="uploaded_y_column")
        # Create bar chart
        fig = px.bar(selected_df, x=x_column, y=y_column, title="Bar Chart (Uploaded Dataset)")
        st.plotly_chart(fig)

    elif visualization_type == "Pie Chart":
        # Select column for pie chart
        pie_column = st.selectbox("Select Data for Pie Chart:", selected_df.columns, key="uploaded_pie_column")
        # Create pie chart
        fig = px.pie(selected_df, names=pie_column, title="Pie Chart (Uploaded Dataset)")
        st.plotly_chart(fig)

    elif visualization_type == "Line Chart":
        # Select columns for X and Y axes
        x_column = st.selectbox("Select X-axis Data:", selected_df.columns, key="uploaded_x_column")
        y_column = st.selectbox("Select Y-axis Data:", selected_df.columns, key="uploaded_y_column")
        # Create line chart
        fig = px.line(selected_df, x=x_column, y=y_column, title="Line Chart (Uploaded Dataset)")
        st.plotly_chart(fig)

# Select dataset from hardcoded datasets
selected_dataset = st.selectbox("Select Dataset:", list(datasets.keys()), key="selected_dataset")

# Check if a dataset is selected
if selected_dataset:
    selected_df = datasets[selected_dataset]

    # Select visualization type
    visualization_type = st.selectbox("Select Visualization Type:", ["Bar Chart", "Pie Chart", "Line Chart"], key="hardcoded_vis_type")

    # Check if a visualization type is selected
    if visualization_type == "Bar Chart":
        # Select columns for X and Y axes
        x_column = st.selectbox("Select X-axis Data:", selected_df.columns, key="hardcoded_x_column")
        y_column = st.selectbox("Select Y-axis Data:", selected_df.columns, key="hardcoded_y_column")
        # Create bar chart
        fig = px.bar(selected_df, x=x_column, y=y_column, title=f"Bar Chart - {selected_dataset}")
        st.plotly_chart(fig)

    elif visualization_type == "Pie Chart":
        # Select column for pie chart
        pie_column = st.selectbox("Select Data for Pie Chart:", selected_df.columns, key="hardcoded_pie_column")
        # Create pie chart
        fig = px.pie(selected_df, names=pie_column, title=f"Pie Chart - {selected_dataset}")
        st.plotly_chart(fig)

    elif visualization_type == "Line Chart":
        # Select columns for X and Y axes
        x_column = st.selectbox("Select X-axis Data:", selected_df.columns, key="hardcoded_x_column")
        y_column = st.selectbox("Select Y-axis Data:", selected_df.columns, key="hardcoded_y_column")
        # Create line chart
        fig = px.line(selected_df, x=x_column, y=y_column, title=f"Line Chart - {selected_dataset}")
        st.plotly_chart(fig)

# Create a section for custom prediction
st.header("Custom Prediction for 2021")

# Input fields for custom prediction
product_sector = st.selectbox("Select Product/Sector:", unique_sectors)
reporting_economy = st.selectbox("Select Reporting Economy:", unique_economies)
custom_year = 2021

# Button for custom prediction
if st.button("Predict Value"):
    # Call your ML model to predict the value based on the selected inputs
    # Replace the following line with your model's prediction logic
    prediction = 0  # Replace with the actual prediction

    # Display the predicted value in a small box
    st.success(f"Predicted Value: {prediction}")