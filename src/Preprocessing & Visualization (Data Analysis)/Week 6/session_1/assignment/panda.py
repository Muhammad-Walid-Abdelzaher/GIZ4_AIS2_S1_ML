# DEPI AI & ML Round 4
# Data Analysis - Pandas Assignment
# ---------------------------------
# Made With <3 By Muhammad Walid
# Jan 31, 2026
# --------------------------------

import numpy as np
import pandas as pd

# Task 1
# ------

import pandas as pd
import numpy as np

# Create a synthetic Company Sales Dataset
data = {
    "Transaction_ID": range(1, 11),
    "Product_Category": [
        "Electronics",
        "Home",
        "Electronics",
        "Sports",
        "Home",
        "Electronics",
        "Home",
        "Sports",
        "Electronics",
        "Electronics",
    ],
    "Sales_Amount": [
        150,
        200,
        155,
        300,
        210,
        180,
        205,
        1000,
        190,
        160,
    ],  # 1000 is an Outlier
    "Customer_Age": [
        25,
        34,
        np.nan,
        45,
        23,
        31,
        29,
        np.nan,
        38,
        40,
    ],  # Contains Nulls (NaN)
    "Rating": [5, 4, 3, 5, 2, 4, 5, 2, 4, 3],
}

df_test = pd.DataFrame(data)

# Save to CSV for students to practice loading files [cite: 74]
df_test.to_csv("company_sales_test.csv", index=False)
print("Test dataset created successfully!")

# print(df_test.head())
# print(df_test.tail())
# print(df_test)

print("#" * 30)

import pandas as pd


def automated_stat_analyzer(df, column_name):
    """
    Company Task: Provide a summary report of a specific data variable.

    Instructions:
    1. Check if the column is numerical or categorical.
    2. For numerical: Calculate Mean, Median, and Standard Deviation.
    3. For categorical: Calculate the Mode.
    4. Return a dictionary with these statistical measures.
    """

    col = df[column_name]

    if pd.api.types.is_numeric_dtype(col):

        stats = {
            "Type": "Numerical",
            "Mean": float(col.mean()),
            "Mmedian": float(col.median()),
            "Standard Deviation": float(col.std()),
        }

    else:

        stats = {"Type": "Categorical", "Mode": col.mode()}

    return stats


data_path = r"C:\Users\Muhammad Walid\Python\DEPI\GIZ4_AIS2_S1_ML\GIZ4_AIS2_S1_ML\src\Preprocessing & Visualization (Data Analysis)\Week 6\session_1\assignment\company_sales_test.csv"
df = pd.read_csv(data_path)
print("Product Category: ", automated_stat_analyzer(df, "Product_Category"))
print("Sales Amount: ", automated_stat_analyzer(df, "Sales_Amount"))
print("Customer Age: ", automated_stat_analyzer(df, "Customer_Age"))
print("Rating: ", automated_stat_analyzer(df, "Rating"))

print("#" * 30)

# Task 2
# ------


def null_handling_strategy(df, strategy="fill_mean"):
    """
    Company Task: Clean a dataset by resolving missing (NaN) values.
    """
    # TODO: Implement using .isnull(), .dropna(), or .fillna() you can used Customer_Age for your test case
    copy_df = df.copy()

    null_counts = copy_df.isnull().sum()
    total_nulls = null_counts.sum()

    if total_nulls == 0:

        print("No Null Values Found.")
        return copy_df

    else:

        print(f"Total Null Values: {total_nulls}")

    if strategy == "drop_rows":

        cleaned_df = copy_df.dropna()

    elif strategy == "fill_mean":

        num_cols = copy_df.select_dtypes(include=[np.number]).columns
        for col in num_cols:

            if copy_df[col].isnull().any():

                copy_df[col] = copy_df[col].fillna(copy_df[col].mean())

    elif strategy == "fill_median":

        num_cols = copy_df.select_dtypes(include=[np.number]).columns
        for col in num_cols:

            if copy_df[col].isnull().any():

                copy_df[col] = copy_df[col].fillna(copy_df[col].median())

    else:

        raise ValueError(
            "Invalid Strategy, Make sure to choose: drop_rows, fill_mean or fill_median"
        )

    return copy_df


data_path = r"C:\Users\Muhammad Walid\Python\DEPI\GIZ4_AIS2_S1_ML\GIZ4_AIS2_S1_ML\src\Preprocessing & Visualization (Data Analysis)\Week 6\session_1\assignment\company_sales_test.csv"
df = pd.read_csv(data_path)
# print(df)

df_dropped = null_handling_strategy(df, "drop_rows")
print(df_dropped["Customer_Age"])

print("=" * 30)

df_mean = null_handling_strategy(df, "fill_mean")
print(df_mean["Customer_Age"])

print("=" * 30)

df_median = null_handling_strategy(df, "fill_median")
print(df_median["Customer_Age"])
