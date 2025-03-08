#streamlit
import streamlit as st

st.set_page_config(page_title= "growth mindset project", project_icon="★")
st.title("🌱Growth Mindset challenge: web App with Streamlit ")

st.header("🚀Welcome to your Growth Gourney!")
st.write("Embrace Challenges, learn from mistakes, and unlock your full potential. this AI-powered app helps you build a growth mindset with reflection, challenges and achievements!💎 ")

#quotes
st.header("😇 Todays Grwoth Mindset Quote")
st.write("Failure is not fatal, but failing to change might be. - John Wooden ")

st.header("🔧What's Your Challenge Today?")
user_input = st.text_input("Describe a Challenge You're Facing:")

#condition
if user_input:
    st.success(f" you're facing: {user_input}. keep pushing forward towards your goals!🚀")

else:
    st.warning("tell us about your challenge to get started")

#Reflexing
st.header("✅ Reflect on your learning")
reflection = st.text_area("write your outcome here:")

if reflection:
    st.sucess(f"⭐ Great Insight! your reflection: {reflection}")

else:
    st.info("Reflecting on past experience help you grow! share your difficulties")

#achievements
st.header("Celebrate Your Achievements🎉")
achievement = st.text_input("share something you've recently accopmlished")

if achievement:
    st.suucess(f"🎊Amazing you achieved {achievement}")
else:
    st.info("Big or Small, every achivement counts! Share One Now🤩")

#footer
st.write("- - -")
st.write("If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success")
st.write("**💥Created By Hafsa Sheikh**")