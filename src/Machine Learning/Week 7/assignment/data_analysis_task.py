# DEPI AI & ML Round 4
# Data Analysis Task
# --------------------
# Made With <3 By Muhammad Walid
# Feb 15, 2026
# ------------------------------

import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Change the current working directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# print(os.getcwd())

# Part 1: Data Understanding
# --------------------------

# Load Data
bank_data = pd.read_csv("bank.csv")

# Display:
print(bank_data.head())

print("#" * 30)  # Separator

print(bank_data.shape)  # (11162, 15)

print("#" * 30)  # Separator

print(bank_data.columns)

print("#" * 30)  # Separator

# print(bank_data.describe())
bank_data.info()

print("#" * 50)  # Separator

# Part 2: Data Type Checking & Handling
# -------------------------------------

# print(bank_data.dtypes)
# print(bank_data.nunique())


def check_data_type(data_frame: pd.DataFrame):
    data_type = data_frame.dtypes
    num_unique_data = data_frame.nunique()

    return pd.DataFrame(
        {"Data Type:": data_type, "No. of Unique Data:": num_unique_data}
    )
    # return pd.DataFrame({"Data Type:": data_type, "No. of Unique Data:": num_unique_data}).T


print(check_data_type(bank_data))

print("#" * 30)  # Separator

categorical_features = [
    "job",
    "marital",
    "education",
    "housing",
    "loan",
    "contact",
    "month",
    "deposit",
]

bank_data[categorical_features] = bank_data[categorical_features].astype("category")

print(check_data_type(bank_data))

print("#" * 50)  # Separator

# Part 3: Missing Value Analysis
# ------------------------------

# print(bank_data.isnull().sum())
# print((bank_data == "unknown").sum())
# print(bank_data.shape[0])


def check_data_nulls(data_frame: pd.DataFrame):
    # bank_data.isnull().sum()
    null_data = (bank_data == "unknown").sum()
    num_rows = data_frame.shape[0]
    null_ratio = null_data / num_rows

    return pd.DataFrame({"No. of Null Data:": null_data, "Null Ratio:": null_ratio})
    return pd.DataFrame({"No. of Null Data:": null_data, "Null Ratio:": null_ratio}).T


print(check_data_nulls(bank_data))

print("#" * 50)  # Separator

# Part 4: Handling Missing Values
# -------------------------------

# Method 1: Drop Columns
# ----------------------
# Max. column contains nulls: 'contact', with null ratio: 21.0177 %
# No columns contains more than 40% nulls => No Columns Are Dropped

# Method 2: Drop Rows
# -------------------

unknown_rows = bank_data[(bank_data == "unknown").any(axis=1)].index
# print(unknown_rows)
bank_data.drop(unknown_rows, inplace=True)

print(check_data_nulls(bank_data))
# print(check_data_type(bank_data))

# Method 3: Drop Imputation
# -------------------------
# No Missing Values Found

# Part 5: Basic Data Visualization
# --------------------------------

# 1. Histogram of age
plt.figure(figsize=(10, 6))
plt.hist(bank_data["age"], bins=20, color="skyblue", edgecolor="black")
plt.title("Distribution of Customer Ages")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
# Interpretation: Most customers are between 30-50 years old (Normal Distribution)

# 2. Boxplot of balance
plt.figure(figsize=(10, 6))
plt.boxplot(bank_data["balance"])
plt.title("Distribution of Account Balance")
plt.xlabel("Balance")
plt.ylabel("Amount")
plt.show()
# Interpretation: The balance has many outliers on the higher end

# 3. Distribution of duration
plt.figure(figsize=(10, 6))
plt.hist(bank_data["duration"], bins=30, color="lightcoral", edgecolor="black")
plt.title("Distribution of Call Duration")
plt.xlabel("Duration (seconds)")
plt.ylabel("Frequency")
plt.show()
# Interpretation: Most calls are short (under 500 seconds) (Right-Skewed)

# 4. Bar chart of job
plt.figure(figsize=(12, 6))
job_counts = bank_data["job"].value_counts()
plt.bar(job_counts.index, job_counts.values, color="lightgreen")
plt.title("Customer Jobs Distribution")
plt.xlabel("Job Type")
plt.ylabel("Count")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
# Interpretation: Management and blue-collar are the most common jobs

# 5. Bar chart of deposit (yes/no)
plt.figure(figsize=(8, 6))
deposit_counts = bank_data["deposit"].value_counts()
plt.bar(deposit_counts.index, deposit_counts.values, color=["lightblue", "lightcoral"])
plt.title("Deposit Subscription")
plt.xlabel("Subscribed to Deposit?")
plt.ylabel("Count")
plt.show()
# Interpretation: More customers did NOT subscribe to deposits

# 6. Count plot of deposit vs housing
plt.figure(figsize=(10, 6))
pd.crosstab(bank_data["housing"], bank_data["deposit"]).plot(kind="bar")
plt.title("Deposit Subscription by Housing Loan Status")
plt.xlabel("Has Housing Loan?")
plt.ylabel("Count")
plt.legend(title="Deposit")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
# Interpretation: Customers without housing loans are more likely to subscribe

# Part 6: Final Questions
# -----------------------

# Q1. Which preprocessing method was most effective for this dataset?
# => In my opinion, I believe that handling the "unknown" values was the most efficient method we've done

# Q2. Which feature seems most related to deposit subscription?
# => Based on the visualizations, duration (call duration) feature is the most related;
# => as longer call durations typically indicate more engaged conversations and higher chances of subscription

# Q3. What problems could appear if preprocessing is skipped?
# => Inaccurate visualizations: as the 'unknown' values was going to be treated as a valid value
