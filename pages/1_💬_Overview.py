""" Display the overview of the PW Skills Projects provided in their experience portal. """

import plotly.express as px
import streamlit as st
from pandas import read_csv

# Page config
st.set_page_config('Projects Overview', '💬', 'wide')

# --- Import DataFrame --- #
df = read_csv('data/final_df.csv')

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- #
# --- Section 1 --- #
col1, col2, col3 = st.columns(3)
col1.metric('No. of Technologies', df['techTitle'].nunique())
col2.metric('No. of Domains', df['domainTitle'].nunique(),
            help='Maybe some Domain reapted.')
col3.metric('No. of Projects', df['projectTitle'].nunique(),
            help="Maybe some Project's title reapted.")

# --- Section 2 --- #
col1.metric('No. of Beginner Level Projects',
            df.query('difficulty=="beginner"').shape[0])
col2.metric('No. of Intermediate Level Projects',
            df.query('difficulty=="intermediate"').shape[0])
col3.metric('No. of Advanced Level Projects',
            df.query('difficulty=="advanced"').shape[0])

# --- Section 3 --- #
with col1.expander('All Technologies Title', True):
    for i, title in enumerate(sorted(df['techTitle'].unique())):
        st.write(f'{i+1}. {title}')

with col2.expander('All Domains Title', True):
    for i, title in enumerate(sorted(df['domainTitle'].unique())):
        st.write(f'{i+1}. {title}')

with col3.expander('All Projects Title', True):
    for i, title in enumerate(sorted(df['projectTitle'].unique())):
        st.write(f'{i+1}. {title}')

# --- Add CSS to maintain height --- #
expande_height = """ 
    <style>
        div.streamlit-expanderContent {
            overflow: scroll;
        }
        div.streamlit-expanderContent > div {
            height: 485px;
        }
    </style>
"""
st.write(expande_height, unsafe_allow_html=True)

# --- Distribution of Levels of projects - Pie Chart --- #
if st.sidebar.checkbox('Check distribution of Projects'):
    temp_df = (df['difficulty'].value_counts(normalize=True)
               .mul(100).round(2).reset_index())

    fig = (px.pie(temp_df, 'index', 'difficulty')
           .update_traces(showlegend=False))
    st.sidebar.plotly_chart(fig, use_container_width=True)
