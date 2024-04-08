import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
@st.cache
def load_data():
    df = pd.read_csv('ds_salaries.csv')  # Load your dataset here
    return df

df = load_data()

# Sidebar for navigation
analysis_option = st.sidebar.selectbox(
    'Select Analysis',
    ('Salary Distribution by Job Title', 'Geographic Salary Disparities', 'Experience Level Analysis')
)

# Main content based on selected analysis
if analysis_option == 'Salary Distribution by Job Title':
    st.header('Salary Distribution by Job Title')
    
    # Filter jobs
    selected_jobs = st.multiselect('Select Job Titles', df['job_title'].unique())
    filtered_df = df[df['job_title'].isin(selected_jobs)] if selected_jobs else df
    
    # Plot salary distribution by job title
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='job_title', y='salary', data=filtered_df)
    plt.xticks(rotation=45)
    st.pyplot()

elif analysis_option == 'Geographic Salary Disparities':
    st.header('Geographic Salary Disparities')
    
    # Choose countries to show
    selected_countries = st.multiselect('Select Countries', df['company_location'].unique())
    filtered_df = df[df['company_location'].isin(selected_countries)] if selected_countries else df
    
    # Plot geographic salary disparities
    plt.figure(figsize=(10, 6))
    sns.barplot(x='company_location', y='salary_in_usd', data=filtered_df)
    plt.xticks(rotation=45)
    st.pyplot()

elif analysis_option == 'Experience Level Analysis':
    st.header('Experience Level Analysis')
    
    # Plot salary distribution by experience level
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='job_title', y='salary', data=df)
    plt.xticks(rotation=45)
    st.pyplot()