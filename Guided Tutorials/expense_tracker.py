import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# App Title
st.title("Simple Expense Tracker")

# File Uploader
uploaded_file = st.file_uploader("Upload your expense CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    # Display the DataFrame
    st.subheader("Expense Data")
    st.dataframe(df)

    # Adding New Expense Form
    st.subheader("Add a New Expense")
    date = st.date_input("Date")
    category = st.selectbox("Category", ["Food", "Travel", "Utilities", "Entertainment", "Other"])
    amount = st.number_input("Amount", min_value=0.0, format="%.2f")

    if st.button("Add Expense"):
        new_row = {"Date": date, "Category": category, "Amount": amount}
        new_df = pd.DataFrame([new_row])  # Create DataFrame for the new row
        df = pd.concat([df, new_df], ignore_index=True)  # Concatenate the new row to the existing DataFrame
        df.to_csv(uploaded_file, index=False)  # Save the updated DataFrame to CSV
        st.success(f"Expense of {amount} added to {category} on {date}")

    # Analyzing Expenses by Category
    st.subheader("Expense by Category")
    if not df.empty:
        expense_by_category = df.groupby("Category")["Amount"].sum()
        st.write(expense_by_category)

        # Pie Chart Visualization
        fig, ax = plt.subplots()
        ax.pie(expense_by_category, labels=expense_by_category.index, autopct='%1.1f%%')
        st.pyplot(fig)

    # Download Updated CSV
    st.subheader("Download Updated Expense Data")
    st.download_button(
        label="Download CSV",
        data=df.to_csv(index=False),
        mime="text/csv")
else:
    st.error("CSV file not found. Please upload the 'expense_data.csv' file.")