import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to load the dataset
def load_data():
    data = pd.read_csv("C:\\Users\\sanja\\Desktop\\ml\\streamlitapp\\Iris.csv")
    return data

# Load the Iris dataset
data = load_data()

# Set the title and description of the Streamlit app
st.title('Iris Data Visualization Dashboard')
st.write('This is an interactive dashboard to visualize the Iris dataset.')

# Display the dataset
st.subheader('Dataset')
st.dataframe(data)

# Display summary statistics if checkbox is selected
if st.checkbox('Show Summary Statistics'):
    st.write('Summary Statistics')
    st.write(data.describe())

# Display correlation matrix if checkbox is selected
if st.checkbox('Show Correlation Matrix'):
    st.write('Correlation Matrix')
    numeric_data = data.select_dtypes(include='number')
    corr_matrix = numeric_data.corr()
    plt.figure(figsize=(10, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
    st.pyplot(plt)

# Display visualization options
st.subheader('Visualizations')

# Select the type of visualization
viz_type = st.selectbox('Select Visualization Type', ['','Scatter Plot', 'Histogram', 'Line Chart', 'Pair Plot'])

# Conditional rendering of visualizations based on user selection
if viz_type == 'Scatter Plot':
    st.write('Scatter Plot')
    x_axis = st.selectbox('Select X-axis', data.columns)
    y_axis = st.selectbox('Select Y-axis', data.columns)
    plot_title = st.text_input('Plot Title', 'Scatter Plot')
    x_label = st.text_input('X-axis Label', x_axis)
    y_label = st.text_input('Y-axis Label', y_axis)
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=x_axis, y=y_axis, data=data)
    plt.title(plot_title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    st.pyplot(plt)
    
elif viz_type == 'Histogram':
    st.write('Histogram')
    column = st.selectbox('Select Column', data.columns)
    plt.figure(figsize=(10, 6))
    sns.histplot(data[column], bins=30)
    st.pyplot(plt)
    
elif viz_type == 'Line Chart':
    st.write('Line Chart')
    column = st.selectbox('Select Column', data.columns)
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=data, x=data.index, y=column)
    st.pyplot(plt)

elif viz_type == 'Pair Plot':
    st.write('Pair Plot')
    plt.figure(figsize=(10, 6))
    sns.pairplot(data, hue='species')
    st.pyplot(plt)

# Data filtering options
st.subheader('Filter Data')
species = st.multiselect('Select Species', data['Species'].unique())
feature = st.selectbox('Select Visualization Type', ["","SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"])
if feature!="":
    measurement = st.slider(feature, min_value=float(data[feature].min()), max_value=float(data[feature].max()))
    filtered_data = data[(data['Species'].isin(species)) & (data[feature] <= measurement)]
    st.dataframe(filtered_data)

# Data download option
if st.checkbox('Enable Data Download'):
    st.write('Download Filtered Data')
    csv = filtered_data.to_csv(index=False)
    st.download_button(label="Download data as CSV", data=csv, file_name='filtered_data.csv', mime='text/csv')

# Indicate that the app is running
if __name__ == '__main__':
    st.write('Streamlit app is running!')
