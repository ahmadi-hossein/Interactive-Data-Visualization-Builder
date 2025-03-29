import streamlit as st
import pandas as pd
import plotly.express as px

# Streamlit app title
st.title("Interactive Data Visualization Builder by Hossein Ahmadi")

# File uploader
st.write("Upload your dataset (CSV format):")
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    # Load the dataset
    df = pd.read_csv(uploaded_file)

    # Display the dataset preview
    st.write("Dataset Preview:")
    st.dataframe(df.head())

    # Chart type selection
    chart_type = st.selectbox(
        "Select a chart type:",
        ["Scatter Plot", "Bar Chart", "Line Chart", "Histogram", "Box Plot"]
    )

    # Column selection
    st.write("Select columns for visualization:")
    x_axis = st.selectbox("X-axis:", df.columns)
    y_axis = st.selectbox("Y-axis:", df.columns)

    # Optional: Grouping/coloring
    color_column = st.selectbox("Color by (optional):", ["None"] + list(df.columns))

    # Title and labels
    chart_title = st.text_input("Chart Title:", "Your Chart Title")
    x_label = st.text_input("X-axis Label:", x_axis)
    y_label = st.text_input("Y-axis Label:", y_axis)

    # Generate the visualization
    if st.button("Generate Visualization"):
        try:
            # Create the chart based on the selected type
            if chart_type == "Scatter Plot":
                fig = px.scatter(
                    df,
                    x=x_axis,
                    y=y_axis,
                    color=None if color_column == "None" else color_column,
                    title=chart_title,
                    labels={x_axis: x_label, y_axis: y_label}
                )
            elif chart_type == "Bar Chart":
                fig = px.bar(
                    df,
                    x=x_axis,
                    y=y_axis,
                    color=None if color_column == "None" else color_column,
                    title=chart_title,
                    labels={x_axis: x_label, y_axis: y_label}
                )
            elif chart_type == "Line Chart":
                fig = px.line(
                    df,
                    x=x_axis,
                    y=y_axis,
                    color=None if color_column == "None" else color_column,
                    title=chart_title,
                    labels={x_axis: x_label, y_axis: y_label}
                )
            elif chart_type == "Histogram":
                fig = px.histogram(
                    df,
                    x=x_axis,
                    color=None if color_column == "None" else color_column,
                    title=chart_title,
                    labels={x_axis: x_label}
                )
            elif chart_type == "Box Plot":
                fig = px.box(
                    df,
                    x=x_axis,
                    y=y_axis,
                    color=None if color_column == "None" else color_column,
                    title=chart_title,
                    labels={x_axis: x_label, y_axis: y_label}
                )

            # Display the chart
            st.plotly_chart(fig, use_container_width=True)

            # Export options
            st.write("Export Options:")
            if st.button("Download Chart as PNG"):
                fig.write_image("chart.png")
                st.success("Chart saved as 'chart.png'")
        except Exception as e:
            st.error(f"An error occurred: {e}")
else:
    st.warning("Please upload a dataset to proceed.")