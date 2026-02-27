import streamlit as st

home_page = st.Page("home.py", title="HOME")
quiz_page=   st.Page("quiz.py",title="QUIZ")
about_page = st.Page("about.py", title="ABOUT US")
doc_page= st.Page("doc.py", title="DOCUMENTATION")



pg = st.navigation(
    [home_page,quiz_page,doc_page,about_page],
    position="sidebar"
)

        
        



pg.run()