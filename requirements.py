import streamlit as st
from streamlit_option_menu import option_menu
with st.sidebar:
    selected=option_menu(
        menu_title="Internship",
        options=["Home","About","Contact"],
        icons=["house-fill","file-person","person-lines-fill"]
        )
if selected=="Home":
        st.title("Home Page")
elif selected=="About":
        st.title("About page")
else:
        st.title("Contact page")

# st.title("Python FSD🏚️")#Title stream lit emojis in chrome(house)
# st.header("Full stack")#Heading
# st.write("### Development")#h1,h2 tags
# st.write("- _TEXT_")#italic (- space bullet symbol shown)
# st.code("""
#        #include<stdio.h>
#         int main()
#         {
#         printf("Hello world");
#         return 0;
#         }
# """, language="c")#Coding reflection in o/p screen
# col1,col2,col3=st.columns(3)
# with col1:#split into 3 columns
#     st.metric("Full stack course","tamilnadu",+20)
# with col2:
#     st.metric("Full stack course","tamilnadu",+20)
# with col3:
#     st.metric("Full stack course","tamilnadu",+20)




# #st.metric("Full stack course","tamilnadu",+20)#20 up arrow with green colour,-20 Down arrow with red
# #st.metric("Full stack course","tamilnadu",-20)
# with st.sidebar:#side bar
#     name=st.text_input("Enter your name")
#     st.button("Click")
#     st.write(name)
#     st.balloons()
