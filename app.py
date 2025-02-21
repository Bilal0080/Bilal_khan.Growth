#streamlit
import streamlit as st

st.set_page_config(page_title="growth mindset project", page_icon="🌠")
st.title ("Growth Mindset Challenge: Web App with Streamlit")

st.header("Welcome to your Growth Journey!")
st.write("Embrace challenges, learn from mistakes, and unlock your full potential.This AI-powered app helps you build a growth mindset with reflection,challenges, and achievements!")

#quote section
st.header("Today's first Growth Mindset Quote")
st.write("Success is not final, failure is not fatal: it is the courage to continue that counts,- Winston Churchill")

st.header("What's your Challenge Today ?")
user_input = st.text_input("Describe a Challenge you're facing:")

#condition
if user_input:
    st.success(f" you're facing: {user_input}.keep pushing forward towards the challenge")
else:
    st.warning("Tell us about your challenge to get started")

#reflection
st.header("Reflect on Your Learning✍️")
reflection = st.text_area("Write your reflection here:")

if reflection:
    st.success(f"Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflection on past Experience help you grow! share your difficulties")

#achievement
st.header("Enjoy Your Wins!")
achievement = st.text_input("Share something you;ve recently accomplished:")

if achievement:
    st.success(f"Amazing! you achieved: Amazing! you achieved:{achievement}")
else:
    st.info("Big or Small, every achievement counts!Share one now!✨💞")

    #footer
    st.write("- - -")
    st.write("You're doing amazing! Every step counts. Keep growing and shining🌟")
    st.write("Keep believing in yourself. Growths is a journey, not a destination!✍️")
    st.write("**Created by B_k**")
