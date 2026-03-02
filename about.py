import streamlit as st
st.set_page_config(layout="wide")
st.markdown("""
<style>

.main {
    background: linear-gradient(to right, #0E1117, #1C1F26);
}

h1 {
    text-align: center;
    font-size: 50px;
    font-weight: bold;
}

.stTextInput > div > div > input {
    background-color: #1C1F26;
    color: white;
    border-radius: 12px;
    border: 1px solid #6C63FF;
    padding: 12px;
}

.stButton > button {
    background-color: #6C63FF;
    color: white;
    border-radius: 12px;
    height: 45px;
    width: 100%;
    font-size: 16px;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #5848e5;
    color: white;
}

.stFileUploader {
    background-color: #1C1F26;
    border-radius: 12px;
    padding: 10px;
    border: 1px solid #6C63FF;
}

</style>
""", unsafe_allow_html=True)
st.header("ABOUT US")
arham="""
Name:Shaik Murtuza Arham

Roll no:645

Description:
Enthusiastic and curious developer with a strong interest in building practical applications and learning modern technologies. Passionate about coding, problem-solving, and continuously improving through exploration and questions. Experienced in developing Python-based applications, especially using Streamlit, API integration (including AI services), and working on real-world mini projects. Actively learning backend concepts, databases like SQLite, and deployment tools. A quick learner who enjoys experimenting, refining code, and turning ideas into functional products. Focused on growing into a skilled full-stack/AI developer by building, testing, and improving consistently.

Role:Backend(Python,Streamlit)


"""
srinath="""
Name:Kashabiona Srinath

Roll no:617

Description:
He is a motivated and enthusiastic developer with a strong interest in software and web development. He has a solid understanding of HTML and CSS to design structured and responsive web pages. He is proficient in Python for developing logic-based applications and handling data. He enjoys working on projects that improve his practical coding skills. He focuses on writing efficient, organized, and scalable code. He has experience in academic and personal development projects. He is a quick learner who continuously improves his technical knowledge. He has strong analytical thinking and debugging skills. He works effectively in team environments and supports project implementation and testing. 

Role:Front-end(HTML,CSS,Python)
"""
Dhanya_shree="""
Name:Gopinigari Dhanyasree

Roll no:614

Description: 
An undergrad Computer Science student and an aspiring AI developer with a strong passion for Artificial Intelligence and modern software development.An enthusiastic coder who loves exploring concepts in languages like python, java and building practical solutions. I strengthened my skills in Python, Java, HTML, CSS, and the basics of React, while applying core concepts such as OOPs, Data Structures and DBMS. I have hands-on experience with tools like Streamlit, VS Code, Git, and MySQL. My key interests include Artificial Intelligence, NLP fundamentals, machine learning concepts, and application development. I am committed to continuous learning, improving my technical expertise

Role:Backend(Python,API Integration ,Deployment)

"""
swasthvika='''
Name:Shanigarapu Swathvika

Roll no:647

Description:
She is a passionate and dedicated Computer Science student with a strong interest in web development and programming. She has good knowledge of HTML and CSS for creating clean, responsive, and user-friendly interfaces. She is also skilled in Python for handling backend logic and data processing. She enjoys building practical applications that solve real-world problems. She focuses on writing clean, structured, and maintainable code. She has experience working on academic and mini development projects. She is a quick learner who actively explores new technologies and tools. She has good problem-solving skills and attention to detail. She works well in team environments and contributes effectively to project development.

Role:Front-end(HTML,CSS,Python)


'''
st.set_page_config(layout="wide")
st.subheader("TEAM MEMBERS")
st.divider()
col1,col2,col3,col4=st.columns(4)
with col1:
    st.subheader("ARHAM")
    with st.container(border=True):
        st.text(arham)
with col2:
    st.subheader("SRINATH")
    with st.container(border=True):
        st.text(srinath)
with col3:
    st.subheader("DHANYASREE")
    with st.container(border=True):
        st.text(Dhanya_shree)
with col4:
    st.subheader("Swasthvika")
    with st.container(border=True):

        st.text(swasthvika)

