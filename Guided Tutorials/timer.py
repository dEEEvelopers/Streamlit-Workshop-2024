# Importing required modules
import streamlit as st
import time

# Title, markdown and divider
st.title('Pomodoro Timer')
st.markdown('#### This application is a Streamlit dashboard that helps you keep track of time! ⏰')
st.divider()


# Sliders
work_time = st.slider('Work time (in minutes)', 1, 90, 30)
break_time = st.slider('Break time (in minutes)', 1, 30, 5)

# Define timer function
def pomodoro_timer(work_time, break_time):
    work_seconds = work_time * 60
    break_seconds = break_time * 60

    work_placeholder = st.empty()
    break_placeholder = st.empty()

    work_placeholder.write('Work!')
    for i in range(work_seconds - 59):
        time.sleep(1)
        work_placeholder.write(f'{int((work_seconds - i) / 60)} minute(s) left')
    for i in range(60):
        time.sleep(1)
        work_placeholder.write(f'{(59 - i)} second(s) left')
    work_placeholder.write('Stop working!')

    break_placeholder.write('Break!')
    for i in range(break_seconds - 59):
        time.sleep(1)
        break_placeholder.write(f'{int((break_seconds - i) / 60)} minute(s) left')
    for i in range(60):
        time.sleep(1)
        break_placeholder.write(f'{(59 - i)} second(s) left')
    break_placeholder.write('Stop taking a break!')

# Button
if st.button('Start timer!'):
    pomodoro_timer(work_time, break_time)
