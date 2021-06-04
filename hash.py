import uuid
import hashlib
import streamlit as st

def hash_password(password):
   # uuid is used to generate a random number of the specified password
   salt = uuid.uuid4().hex
   return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

def check_password(hashed_password, user_password):
   password, salt = hashed_password.split(':')
   return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

new_pass = st.text_input('Please enter a password: ')
empty=""


hashed_password = hash_password(new_pass)

if new_pass==empty:
   st.write("")
else:
   st.write('The string to store in the db is: ' + hashed_password)
old_pass = st.text_input('Now please enter the password again to check: ')


if check_password(hashed_password, old_pass):
   st.write('You entered the right password')
else:
   st.write('Passwords do not match')






