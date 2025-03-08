import streamlit as st

st.set_page_config(page_title="Growth Mindset Project", icon="⭐")
st.title("🌱Growth Mindset Challenge: Web App with Streamlit ")

st.header("🚀Welcome to Your Growth Journey!")
st.write("Embrace challenges, learn from mistakes, and unlock your full potential. This AI-powered app helps you build a growth mindset with reflection, challenges, and achievements! 💎")

# Quotes
st.header("😇 Today's Growth Mindset Quote")
st.write("Failure is not fatal, but failing to change might be. - John Wooden")

st.header("🔧 What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:")

# Condition for the challenge input
if user_input:
    st.success(f"You're facing: {user_input}. Keep pushing forward towards your goals! 🚀")
else:
    st.warning("Tell us about your challenge to get started.")

# Reflection
st.header("✅ Reflect on Your Learning")
reflection = st.text_area("Write your outcome here:")

if reflection:
    st.success(f"⭐ Great insight! Your reflection: {reflection}")
else:
    st.info("Reflecting on past experiences helps you grow! Share your difficulties.")

# Achievements
st.header("Celebrate Your Achievements 🎉")
achievement = st.text_input("Share something you've recently accomplished:")

if achievement:
    st.success(f"🎊 Amazing! You achieved: {achievement}")
else:
    st.info("Big or small, every achievement counts! Share one now 🤩")

# Footer
st.write("- - -")
st.write("If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success.")
st.write("**💥 Created By Hafsa Sheikh**")
