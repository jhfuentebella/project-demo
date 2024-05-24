import streamlit as st

st.title("Results")
st.write("Here you can put each of your key results.")

c1,c2 = st.columns((0.25,1))

with c1:
  st.write("hello")
with c2:
  st.write("bye")

st.markdown("---")

st.metric(label="Cluster 0 Age", value = "75 years old", delta="+15")
