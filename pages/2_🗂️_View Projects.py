""" Display all the projects details present in their experience portal. """

from typing import Literal

import pandas as pd
import streamlit as st

# Page config
st.set_page_config('View Projects', '🗂️', 'wide')

# --- Import DataFrame --- #
df = pd.read_csv('data/final_df.csv')

df['difficulty'] = df['difficulty'].str.title()


def get_options(df: pd.DataFrame, what: Literal['tech', 'domain'] = 'tech'):
    """ Generate the options for techs and domains. """
    techCount = df['techTitle'].value_counts().to_dict().items()
    domainCount = df['domainTitle'].value_counts().to_dict().items()

    if what == 'tech':
        return [f'{i} ({j:02})' for i, j in techCount]
    else:
        return [f'{i} ({j:02})' for i, j in domainCount]


# --- Sidebar --- #
st.sidebar.title('Experience Portal')
st.sidebar.subheader('By PW Skills')

filter_by = st.sidebar.selectbox('Filter By',
                                 ['Project', 'Domain', 'Technology'])

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- #
sl_diff = st.sidebar.selectbox('Filter By Difficulty',
                               ['-- None --', 'Beginner', 'Intermediate', 'Advanced'])

# Add filter by difficulty of projects
temp_df = df if sl_diff == '-- None --' else df.query('difficulty==@sl_diff')

match filter_by:
    case 'Project':
        sl_tech = str(st.sidebar.selectbox('Select Technology',
                                           get_options(temp_df)))[:-5]
        temp_df = temp_df.query('techTitle==@sl_tech')

        sl_domain = str(st.sidebar.selectbox('Select Domain',
                                             get_options(temp_df, 'domain')))[:-5]
        temp_df = temp_df.query('domainTitle==@sl_domain')

        sl_project = st.sidebar.selectbox('Select Project',
                                          temp_df['projectTitle'].unique())
        temp_df = temp_df.query('projectTitle==@sl_project')

    case 'Domain':
        sl_tech = str(st.sidebar.selectbox('Select Technology',
                                           get_options(temp_df)))[:-5]
        temp_df = temp_df.query('techTitle==@sl_tech')

        sl_domain = str(st.sidebar.selectbox('Select Domain',
                                             get_options(temp_df, 'domain')))[:-5]
        temp_df = temp_df.query('domainTitle==@sl_domain')

    case 'Technology':
        sl_tech = str(st.sidebar.selectbox('Select Technology',
                                           get_options(temp_df)))[:-5]
        temp_df = temp_df.query('techTitle==@sl_tech')

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- #
sl_data = temp_df.to_dict(orient='index').values()
expand = True if len(sl_data) == 1 else False
i = 0

for item in sl_data:
    i += 1
    with st.expander(fr"{i}\. {item['projectTitle']}", expand):
        col1, col2, col3 = st.columns(3)
        col1.metric('Technology', item['techTitle'])
        col2.metric('Domain', item['domainTitle'])
        col3.metric('Difficulty', item['difficulty'])

        st.write(f"## :red[{item['projectTitle']}]")
        st.write(f"#### 📌 [Project Documentaion]({item['link']})")
