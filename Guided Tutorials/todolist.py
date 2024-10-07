import streamlit as st

st.title("TO-DO LIST")

# Input task
task = st.text_input('Enter your tasks:', '')

# Add task button functionality
if st.button('Add Task'): 
    if task:
        st.session_state['task_list'].append(task)

# Initialize the task list if it doesn't exist
if "task_list" not in st.session_state:
    st.session_state['task_list'] = []

# A temporary list to hold tasks that are not checked off
remaining_tasks = []

# Show task list with checkboxes and handle removal
for i, t in enumerate(st.session_state['task_list']):
    if not st.checkbox(f'{i + 1}. {t}'):
        remaining_tasks.append(t)
    else:
        st.balloons()  # Trigger balloons on task completion

# Update the task list with only the remaining tasks
st.session_state['task_list'] = remaining_tasks