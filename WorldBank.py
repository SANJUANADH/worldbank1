import pandas as pd
import numpy as np
import altair as alt
import streamlit as st
st.title('World Bank Data - India')
India=pd.read_csv('World_Bank_India.csv')
style = df.style.hide_index(India)
st.write(styler.to_htm1(India), unsafe_allow_htm1=True)
st.table(India)                  

