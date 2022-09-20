import streamlit as st

st.title("Begin Profile Page")

intro, overview, pro_work, per_work, contact  = st.tabs([
                            "Introduction", 
                            "Overview of Experience and Skills", 
                            "Professional Work", 
                            "Personal Projects",
                            "Contact Information"])