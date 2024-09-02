import streamlit as st
import joblib

model=joblib.load("depression.pkl")

label = {1:'depression ', 0:'not depressed'}

st.title("depression test ")

user_input = st.text_area("Enter your comant here:")

if st.button("analyse"):
    prediction=model.predict([user_input])[0]
    print(user_input)
    predicted_label=label[prediction]
    print("Predicted label:"+str(predicted_label))
    st.info(f"{str(predicted_label)}")