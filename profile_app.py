import streamlit as st

st.title("Begin Profile Page")



intro, overview, pro_work, per_work, contact  = st.tabs([
                            "Introduction", 
                            "Overview of Experience and Skills", 
                            "Professional Work", 
                            "Personal Projects",
                            "Contact Information"])


with st.expander("See explanation", expanded = True):
     st.write("""
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    """)