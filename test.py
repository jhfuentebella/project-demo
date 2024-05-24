import streamlit as st
st.write("Hello, let's learn how to build a streamlit app together")
st.header("hello")
st.markdown("--")
st.subheader("hello again")


import pandas as pd

df = pd.read_csv('cc_rfm.csv')
st.dataframe(df) 

# Display plot (on-call)

# add these lines in requirements.in
# matplotlib
# numpy

import matplotlib.pyplot as plt
import numpy as np

rand=np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()ax.hist(rand, bins=15)st.pyplot(fig)
