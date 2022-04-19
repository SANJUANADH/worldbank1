import pandas as pd
import numpy as np
import altair as alt
import streamlit as st
st.title('World Bank Data - India')
India=pd.read_csv('World_Bank_India.csv')
df = pd.DataFrame(
  np.random.randn(10,5),
  columns=("col%d"% i for i in range(5)))
st.table(df)
                  

