import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# App Title
st.title("Simple Study Scheduler")

# File Uploader
uploaded_file = st.file_uploader("Upload your study scheduler CSV file", type="csv")

if uploaded_file:
    # Load the uploaded file
    if "df" not in st.session_state:
        st.session_state.df = pd.read_csv(uploaded_file)
    
    # Ensure that the CSV has the required columns
    if list(st.session_state.df.columns) != ["Date", "Module", "Time Allocated"]:
        st.error("Invalid CSV format. Please ensure your CSV has columns: Date, Module, Time Allocated")
    else:
        # Display the DataFrame loaded from CSV file
        st.subheader("Study Schedule")
        st.dataframe(st.session_state.df)

        # Extract unique modules from the CSV file
        unique_modules = st.session_state.df['Module'].unique().tolist()

        # Adding New Entry
        st.subheader("Add a New Entry")
        date = st.date_input("Date")
        mod = st.selectbox("Mod", unique_modules + ["Add New Module"])
        
        # Allow user to add a new module if "Add New Module" is selected
        if mod == "Add New Module":
            new_module = st.text_input("Enter new module name")
            if new_module:
                mod = new_module
        
        minutes = st.number_input("Minutes", min_value=0, value=60)

        # Button to add new entry
        if st.button("Add Entry"):
            new_row = {"Date": date, "Module": mod, "Time Allocated": minutes}
            new_df = pd.DataFrame([new_row])  # Create DataFrame for the new row
            st.session_state.df = pd.concat([st.session_state.df, new_df], ignore_index=True)  # Concatenate the new row to the existing DataFrame
            
            # Show success message
            st.success(f"{minutes} minutes added to {mod} on {date}")

        
            # Display updated DataFrame
            st.dataframe(st.session_state.df)


        # Time allocated by module 
        st.subheader("Time Allocated by Module")
        if not st.session_state.df.empty:
            time_df = st.session_state.df.groupby("Module")["Time Allocated"].sum()
            modules = time_df.index  # This will be the y-axis (Module labels)
            time_allocated = time_df.values  # This will be the x-axis (Time allocated)
            fig = plt.figure(figsize=(10, 6))  # Set the figure size
            plt.barh(modules, time_allocated, color='blue')  
            # Adding labels
            plt.xlabel('Time Allocated (hours)', fontsize=12)
            plt.ylabel('Modules', fontsize=12)
            plt.title('Time Allocated per Module', fontsize=14)

            # Adding grid for better readability
            plt.grid(axis='x', linestyle='--', alpha=0.7)
            st.pyplot(fig)

        # Download Updated CSV
        st.subheader("Download Updated Schedule")
        st.download_button(
            label="Download CSV",
            data=st.session_state.df.to_csv(index=False),
            mime="text/csv"
        )
else:
    st.error("CSV file not found. Please upload a csv file.")
    