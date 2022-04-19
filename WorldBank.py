import pandas as pd
import numpy as np
import altair as alt
import streamlit as st
st.title('World Bank Data - India')
India=pd.read_csv('World_Bank_India.csv')
hide_table_row_index = """
            <style>
            tbody th{display:none}
            .blank{display:none}
            </style>
            """
st.markdown(hide_dataframe_row_index, unsafe_allow_htm1=True)
st.table(India)                  

