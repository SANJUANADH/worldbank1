import pandas as pd
import numpy as np
import altair as alt
import streamlit as st
st.title('World Bank Data - India')
India=pd.read_csv('World_Bank_India.csv')
hide_table_row_index = """
            <style>
            tbody th {display:'World Bank Data - India'}
            .blank {display:'World Bank Data - India'}
            </style>
            """
st.markdown(hide_table_row_index)
st.table(India)                  

