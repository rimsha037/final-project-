import streamlit as st
import re
import hashlib
from PIL import Image


def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()


def check_hashes(password, hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False


def main():
    st.header("-------------------Password Checker-------------------")
    st.info("This APP will generate SHA256 Hashes ")
    image = Image.open('download (1).jpg')
    st.image(image, width=750)
    st.subheader("This app will check the password is strong or not")

    if st.checkbox("Check Your Password"):
        image = Image.open('OIP (1).jpg')
        st.image(image, width=750)
        password = st.text_input("Password", type='password')
        if st.button("submit"):
            if (len(password) >= 8):
                if bool(re.match('((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,30})', password)) == True:
                    st.success("You entered Strong password")
                    hashed_pswd = make_hashes(password)
                    st.success("Hashes of your password is: ")
                    st.info(hashed_pswd)


                elif bool(re.match('((\d*)([a-z]*)([A-Z]*)([!@#$%^&*]*).{8,30})', password)) == True:
                    st.warning("The password is weak!")
                    st.warning("Your Password must contain Uppercase, Lowercase, Number and Special Characters")
            else:
                st.error("Password must contain at least 8 characters.")


if __name__ == '__main__':
    main()
