import streamlit as st
import time
from typeing import Wpm


def gui():
    st.title("Typing Test Game")

    st.write("Welcome to the Typing Test Game! Type the following text as fast as you can within 30 seconds:")

    text_to_type = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    st.write(text_to_type)

    user_input = st.text_area("Type here:", height=200)

    start_time = time.time()
    timer_placeholder = st.empty()  # Placeholder for timer
    timer = 30
    while timer > 0:
        timer = 30 - int(time.time() - start_time)
        timer_placeholder.write("Time remaining: {} seconds".format(timer))
        time.sleep(1)

    time_taken = time.time() - start_time
    wpm = Wpm.calculate_wpm(user_input, time_taken)

    st.write("Time's up!")
    st.write("Your typing speed is: {} WPM".format(wpm))

