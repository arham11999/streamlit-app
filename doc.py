import streamlit as st
st.header("DOCUMENTATION")
st.divider()
st.subheader("Front-end Technologies")
with st.container():
    st.subheader("1) HTML:")
    st.text("HTML (HyperText Markup Language) is used to structure and format content within the application. It helps in organizing text, headings, layouts, and other elements displayed on the web interface. In this project, HTML is used within Streamlit to enhance the structure and presentation of content. It allows better control over how information is displayed to the user.")

    st.subheader("2) CSS:")
    st.text("CSS (Cascading Style Sheets) is used to improve the visual appearance of the application. It helps in styling elements such as colors, fonts, spacing, and layout. In this project, CSS is used to create a professional and consistent design. It enhances user experience by making the interface more attractive and easy to use. CSS also helps maintain a clean and modern look throughout the application.")

    st.subheader("3) Streamlit (Python Module):")
    st.text("Streamlit is a Python-based framework used to build the web interface of the application. It allows developers to create interactive and responsive web apps without extensive frontend development. In this project, Streamlit is used to design the user interface, manage file uploads, display outputs, and organize different sections of the application. It simplifies deployment and reduces development time. Streamlit also supports real-time interaction, making the application user-friendly and efficient.")
st.divider()

st.subheader("Back-end Technologies")
with st.container():
    st.subheader("1) Python:")
    st.text("Python is the core programming language used to develop the application. It is a high-level, easy-to-learn language known for its simplicity and readability. Python enables fast development and supports multiple libraries that help in building efficient applications. In this project, Python is used to handle the backend logic, data processing, and integration with external services. Its strong community support and extensive ecosystem make it suitable for building scalable and maintainable applications. Python also helps in handling user inputs, managing workflows, and controlling the overall functionality of the system.")

    st.subheader("2) Streamlit:")
    st.text("Streamlit is used in this project as both the frontend and backend framework. It allows the creation of interactive web interfaces while also handling the application logic in Python. On the frontend side, Streamlit is used to design the user interface, including input fields, buttons, file upload options, and output display. On the backend side, it processes user inputs, manages the application workflow, and interacts with external APIs. Streamlit eliminates the need for separate frontend and backend frameworks, enabling faster development and easier maintenance. It also supports real-time updates and dynamic content rendering. Its simplicity and integration with Python make it an efficient choice for building complete web applications within a single environment.")

    st.subheader("3) API Integration:")
    st.text("API integration is used to connect the application with external services and enable advanced functionalities. In this project, APIs are used to send user data or inputs to external systems and receive processed responses. This helps in adding intelligent features without building complex models from scratch. API integration ensures smooth communication between the application and third-party services. It also improves scalability and allows the system to use powerful external resource")
with st.container():
    st.divider()
    st.subheader("Streamlit Cloud (Deployment)")
    st.text("Streamlit Cloud is used to deploy and host the application online. It allows the project to run as a live web application that can be accessed from any device through a browser. The platform provides an easy deployment process by connecting the project repository and automatically building the app. Streamlit Cloud manages the server environment, dependencies, and application runtime, eliminating the need for manual server setup. It also supports automatic updates whenever changes are pushed to the repository. This helps in maintaining the latest version of the application without redeployment. Streamlit Cloud ensures reliable performance, scalability, and secure hosting, making it a convenient solution for sharing and demonstrating the project.")
