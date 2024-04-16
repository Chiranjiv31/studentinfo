import streamlit as st

st.title('This is :blue[student] data')

Name = st.text_input("Enter your name")
Id = st.text_input("Enter your college ID")
Institute = st.selectbox("Education",('select institute','BD college', 'JB college', 'KDK College','G H Raisoni'))
Year = st.selectbox("year",('select Year','1st year', '2nd year', '3rd year','4th year'))
Semester = st.selectbox("Semester",('select semester','1st sem', '2ndsem', '3rd sem','4th sem','5th sem', '6thsem', '7th sem','8th sem'))
Rollno = st.selectbox("roll no",('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'))

button = st.button("SUBMIT")
if button:
    st.markdown(f"""
    Name:{Name}        
    ID:{Id}
    select institute:{Institute}
    select year:{Year}
    select semester:{Semester}
    select rollno:{Rollno}""")

