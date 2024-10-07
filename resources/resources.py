import streamlit as st

# Title of the Streamlit app
st.title("Basic Streamlit Components")

# Text elements
st.header("Streamlit Components Demo")
st.subheader("This app demonstrates basic components in Streamlit")
st.text("Below are various Streamlit widgets and their usage:")
st.divider()

# Sidebar navigation
st.sidebar.header("This is the sidebar with navigation functionality")
st.sidebar.write("In order to add navigation pages, make sure to add a pages folder in the root directory and add the non homepages there.")
st.sidebar.write("**You can add widgets here too.**")
st.sidebar.button("Such as this button")

# Button
st.markdown("_Button_: A clickable button that triggers an action.")
if st.button('Click me!'):
    st.write("Button clicked!")
    st.balloons()

st.divider()

# Radio buttons
st.markdown("_Radio button_: A group of options from which only one can be selected.")
choice = st.radio("Choose an option:", ('Option 1', 'Option 2', 'Option 3'))
st.write(f"You selected: {choice}")

st.divider()

# Checkbox
st.markdown("_Checkbox_: A simple toggle to capture selected inputs.")
check = st.checkbox('Check this box')
if check:
    st.write("Checkbox is checked!")
else:
    st.write("Checkbox is unchecked.")

st.divider()

# Selectbox
st.markdown("_Selectbox_: A dropdown menu for selecting one option from a list.")
selectbox_option = st.selectbox("Select a value from the dropdown:", ['Apple', 'Banana', 'Cherry'])
st.write(f"Selected value: {selectbox_option}")

st.divider()

# Multi-select
st.markdown("Display a multiselect widget. The multiselect widget starts as empty.")
options = st.multiselect(
    "What are your favorite colors",
    ["Green", "Yellow", "Red", "Blue"],
    ["Yellow", "Red"],
)

st.write("You selected:", options)

st.divider()

# Displaying data in a table from previous input
import pandas as pd
if options:
    data = pd.DataFrame({
        'Column A': options  # Selected options
    })
    st.markdown("_Table_: Displaying selected options in a table.")
    st.table(data)
else:
    st.write("Please select at least one option to display the table.")

st.divider()

# Slider
st.markdown("_Slider_: A draggable control for selecting a numerical range.")
slider_val = st.slider("Select a value", 10, 100, 50)
st.write(f"Selected value: {slider_val}")
slider_val = st.slider("Select a range of values", 0, 100, (20, 80))
st.write(f"Selected range: {slider_val}")

st.divider()

# Number input
st.markdown("_Number input_: A widget to allow users to input a number within a given range.")
number = st.number_input("Insert a number", min_value=0, max_value=100, value=50)
st.write(f"Number: {number}")

st.divider()

# Text input
st.markdown("_Text input_: Allows the user to input text.")
text = st.text_input("Enter your name:")
if text:
    st.write(f"Hello, {text}!")
else:
    st.write("Enter something.")

user_input = st.text_area("Enter your thoughts here:", height=150)
if user_input:
    st.write(f"You wrote: {user_input}")
else:
    st.write("Write something.")

st.divider()

# Dataframe
st.markdown("_Dataframe_: Create and display an editable dataframe")
df = pd.DataFrame(
    [
       {"command": "Selectbox", "rating": 4, "is_widget": True},
       {"command": "Radio buttons", "rating": 5, "is_widget": False},
       {"command": "text input", "rating": 3, "is_widget": True},
   ]
)
edited_df = st.data_editor(df) # st.dataframe is the non-editable version

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

st.bar_chart(edited_df, x="command", y="rating")

st.divider()

# Chat interface simulation
st.markdown("_Chat Interface_: A simple text input where you can simulate a chat interaction.")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = [{"role": "assistant", "content": "Let's chat!"}]

# Main container for chat messages
with st.container():
    if prompt := st.chat_input("Say something"):
        # Add user message to the chat history
        st.session_state["chat_history"].append({"role": "user", "content": prompt})

        # Add assistant's echo response to the chat history
        response = f"Echo: {prompt}"
        st.session_state["chat_history"].append({"role": "assistant", "content": response})

with st.container(height=300):
    # Display all messages in the chat history
    for message in st.session_state["chat_history"]:
        role = message["role"]
        content = message["content"]
        if role == "user":
            st.chat_message("user").write(content)
        else:
            st.chat_message("assistant").write(content)

st.divider()

# File upload and Download button
st.markdown("_File upload and download button_: Allows the user to upload a file and download a duplicate of it.")
uploaded_file = st.file_uploader("Upload a file")
if uploaded_file is not None:
    # Display uploaded file name
    st.write(f"Uploaded file: {uploaded_file.name}")

    # Use the uploaded file's content as it is for download
    st.download_button(
        label="Download the same file",
        data=uploaded_file.getvalue(),  # Get the raw file content
        file_name=uploaded_file.name,  # Keep the original file name
        mime=uploaded_file.type  # Use the MIME type of the uploaded file
    )
else:
    st.button("Upload a file before downloading.")

st.divider()

# Tabs
st.markdown("_Tabs_: Organize content in different tabs to improve user experience.")
tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
with tab1:
    st.write("1. You can add widgets here too.")
with tab2:
    st.write("2. You can add widgets here too.")

st.divider()

# Date input
st.markdown("_Date input_: Widget to pick a date.")
date = st.date_input("Select a date")
st.write(f"Selected date: {date}")

st.divider()

# Displaying and running code
st.markdown("_Echo_: Displaying and running code")
with st.echo():
    def get_user_name():
        return 'John'

    def get_punctuation():
        return '!!!'

    greeting = "Hi there, "
    user_name = get_user_name()
    punctuation = get_punctuation()

    st.write(greeting, user_name, punctuation)

st.divider()

# Displaying an image
st.markdown("_Image_: Display an image within the app.")
st.image("https://floralife.com/wp-content/uploads/2022/04/Iris_2560x1790-1280x895.png", caption="Sample image")
