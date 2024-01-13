import streamlit as st
from PIL import Image


ims = Image.open('20221209_003244_0001~3.png')
def main():
    st.set_page_config(page_title="bookbuddies AI", page_icon="🤠🤓")

    st.header("bookbuddies 🤠🤓")
    st.text_input("Ask a question about your textbook")


    with st.sidebar:
        st.subheader("Your Textbook")
        st.file_uploader("Upload your Textbook")
        st.button("Process")



if __name__ == '__main__':
    main()

