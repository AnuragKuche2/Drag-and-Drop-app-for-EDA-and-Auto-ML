# imports
import streamlit as st

# import numpy as np
import pandas as pd

# import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
matplotlib.use('Agg')


def main():

    st.title('Semi Auto ML application')
    st.text("Using StreamLit")

    activities = ["EDA", "Plot", "Model Building", 'About']

    choice = st.sidebar.selectbox("Select Activity", activities)
    if choice == "EDA":
        st.subheader("Exploratory Data Analysis")

        data = st.file_uploader("Upload Dataset", type=['csv', 'txt'])
        if data is not None:
            df = pd.read_csv(data)
            st.dataframe(df.head())

            if st.checkbox('show shape'):
                st.write(df.shape)

            columnslist = []

            if st.checkbox('Show Columns'):
                columnslist = df.columns.tolist()
                st.write(columnslist)

            if st.checkbox('Select the columns to Show'):
                selected_columns = st.multiselect('select columns', columnslist)
                new_df = df[selected_columns]
                st.dataframe(new_df)

            if st.checkbox('Show Summary'):
                st.write(df.describe())

            if st.checkbox('Show Value Counts'):
                st.write(df.iloc[:, -1].value_counts)

    if choice == "Plot":
        st.subheader("Plotting different columns")

        data = st.file_uploader("Upload Dataset", type=['csv', 'txt'])
        if data is not None:
            df = pd.read_csv(data)
            st.dataframe(df.head())

            if st.checkbox('Correlation with Seaborn'):
                st.write(sns.heatmap(df.corr(),annot=True))
                st.pyplot()

            if st.checkbox('Pie Chart'):
                all_column = df.columns.to_list()
                columns_to_plot = st.selectbox('Select columns', all_column)
                pie_plot = df[columns_to_plot].value_counts()
                st.write(pie_plot)
                st.pyplot()






    if choice == "Model Building":
        st.subheader("Using different ML algorithm to build a model")

    if choice == "About":
        st.subheader("About the application")


if __name__ == "__main__":
    main()
