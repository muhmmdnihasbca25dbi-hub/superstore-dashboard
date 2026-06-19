""" import streamlit as st
import pandas as pd
from datetime import datetime

# ---------------------------------------------------
# PAGE TITLE + DESCRIPTION
# ---------------------------------------------------

st.set_page_config(page_title="Personal Expense Tracker", layout="wide")

st.title("🧾 Personal Expense Tracker")
st.write("Upload your expenses CSV file and analyze your spending patterns.")

# ---------------------------------------------------
# FILE UPLOADER
# ---------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload expenses.csv",
    type=["csv"]
)

if uploaded_file is not None:

    # Read CSV
    df = pd.read_csv(uploaded_file)

    # Convert Date column
    df["Date"] = pd.to_datetime(df["Date"])

    # Convert Amount column to numeric
    df["Amount"] = (
        df["Amount"]
        .astype(str)
        .str.replace(",", "")
        .str.replace("₹", "")
    )

    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")

    # ---------------------------------------------------
    # SIDEBAR FILTERS
    # ---------------------------------------------------

    st.sidebar.header("Filters")

    # ---------------------------------------------------
    # SIDEBAR FILTERS
    # ---------------------------------------------------

    st.sidebar.header("Filters")

    # Date range picker
    date_range = st.sidebar.date_input(
        "Select Date Range",
        value=(
            datetime(2024, 1, 1),
            datetime(2024, 5, 31)
        ),
        min_value=datetime(2024, 1, 1),
        max_value=datetime(2024, 5, 31)
    )

    # isinstance guard
    if isinstance(date_range, tuple) and len(date_range) == 2:
        start_date, end_date = date_range
    else:
        start_date = datetime(2024, 1, 1).date()
        end_date = datetime(2024, 5, 31).date()

    # Category options
    category_options = [
        "Food & Dining",
        "Transport",
        "Utilities",
        "Entertainment",
        "Shopping",
        "Healthcare"
    ]

    # Multiselect
    selected_categories = st.sidebar.multiselect(
        "Select Categories",
        category_options,
        default=category_options
    )

    # Guard if user deselects everything
    if not selected_categories:
        selected_categories = category_options

    # ---------------------------------------------------
    # APPLY FILTERS
    # ---------------------------------------------------

    # Date filter first
    filtered_df = df[
        (df["Date"].dt.date >= start_date) &
        (df["Date"].dt.date <= end_date)
    ]

    # Category filter second
    filtered_df = filtered_df[
        filtered_df["Category"].isin(selected_categories)
    ]

    # ---------------------------------------------------
    # KPI METRICS
    # ---------------------------------------------------

    total_spend = filtered_df["Amount"].sum()
    total_transactions = filtered_df.shape[0]
    avg_transaction = filtered_df["Amount"].mean()
    largest_expense = filtered_df["Amount"].max()

    # Four metric cards
    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Spend",
        f"₹{total_spend:,.2f}"
    )

    col2.metric(
        "Transactions",
        total_transactions
    )

    col3.metric(
        "Average Transaction",
        f"₹{avg_transaction:,.2f}"
    )

    col4.metric(
        "Largest Expense",
        f"₹{largest_expense:,.2f}"
    )

# ---------------------------------------------------
# FILTERED DATA TABLE
# ---------------------------------------------------

st.subheader("Filtered Transactions")

st.dataframe(
    filtered_df,
    hide_index=True,
    use_container_width=True
)

# Download filtered CSV
csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Filtered CSV",
    data=csv,
    file_name=f"expenses_{start_date}_{end_date}.csv",
    mime="text/csv",
    type="primary"
)

# ---------------------------------------------------
# SPEND BY CATEGORY
# ---------------------------------------------------

st.subheader("Spend by Category")

# Color picker
selected_color = st.color_picker(
    "Choose Bar Chart Color",
    "#3B82F6"
)

st.write(f"Selected Color: {selected_color}")

# Group by category
category_spend = (
    filtered_df.groupby("Category")["Amount"]
    .sum()
    .sort_values(ascending=False)
)

# Display bar chart
st.bar_chart(category_spend)


    # ---------------------------------------------------
    # SHOW FILTERED DATA
    # ---------------------------------------------------

st.subheader("Filtered Expenses")
st.dataframe(filtered_df, use_container_width=True)

else:
    st.info("Please upload expenses.csv to get started.") """