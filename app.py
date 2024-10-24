import streamlit as st

st.set_page_config(page_title="Multi-Page App", layout="wide")

home_page = st.Page("pages/home.py", title="Home", icon=":material/info:", default=True)
cv_page = st.Page("pages/cv.py", title="CV", icon=":material/account_box:")
contact_page = st.Page("pages/contact.py", title="Contact", icon=":material/contact_mail:")
blog_page = st.Page("pages/blog.py", title="Blog", icon=":material/article:")

pg = st.navigation(
        {
            "Info": [home_page, cv_page, contact_page, blog_page],
        }
    )

pg.run()