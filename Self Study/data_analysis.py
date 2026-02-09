# Feb 7, 2026
# Made With <3 By Muhammad Walid
# ------------------------------

import os

# Change The Current Working Directory
os.chdir(r"C:\Users\Muhammad Walid\Python\DEPI\GIZ4_AIS2_S1_ML\Self Study")
# print(os.getcwd())

data_path = r"C:\Users\Muhammad Walid\Python\DEPI\GIZ4_AIS2_S1_ML\Self Study\train.csv"

import pandas as pd

df = pd.read_csv(data_path)

# print(df)  # Return DataFrame (All the data you have in your file)  ## [891 rows x 12 columns]
### print(df.head())  # Return The First 5 Rows in your DataFrame (like the "head" of the data)  ## [5 rows x 12 columns]
# print(df.tail())  # Return The Last 5 Rows in your DataFrame (like the "tail" of the data)  ## [5 rows x 12 columns]

# drop الشركات الكبيرة بتبقي عارفة من الأول ايه "الأعمدة" اللي هيعملولها
# Dataال Preprocessاحنا مش عايزنها او مش هنحتاجها و احنا بنـ Columns من الأخر ايه

# Very Important NOTE s:
# "axis=1" => Drop "labels" From COLUMNS, "axis=0" => Drop "labels" From ROWS
# "inplace=True" => Modifies The Original DataFrame
# "inplace=False" (Default) = Returns New DataFrame Without Modifing The Original One
not_needed_columns = ["PassengerId", "Name", "Ticket"]

# New DataFrame
# new_df = df.drop(labels=not_needed_columns, axis=1)
# print(new_df.head())

# Modified DataFrame (Modify The Original DataFrame)
df.drop(labels=not_needed_columns, axis=1, inplace=True)
# print(df.head())
# print(df.index)

# Now, First thing to do is to CHECK DataType [1]
# -----------------------------------------------
# For example, in our data we have Columns like:
# "Survived", "Pclass", "Sex", "SibSp", "Parch", "Embarked" => Should Be CATEGORICAL
# What is meant by "Categorical":
#                               - Survived: is meant to be 0 or 1
#                               - Pclass: is meant to be 1 or 2 or 3
#                               - Sex: is meant to be 'male' or 'female'
#                               - SibSp: is meant to be 0 or 1
#                               - Parch: is meant to be 0 or 1 or 2
#                               - Embarked: is meant to be 'S' or 'C' or 'Q'
# So, the point is you can "Categorize" the Column In Specific Data (0 or 1) or ('male' or 'female') and so on

# print(df.dtypes)
# print(df.nunique())  # OR (Default) => print(df.nunique(axis=0, dropna=True))

# NOTE مهمة:
# "Categorical" <= عرفنا ان الأعداد الصغيرة زي ال2 وال3 وال7 هيبقوا ،Unique Dataمن خلال عدد ال
# "Numerical" <= اما الأعداد الكبيرة زي ال147 او ال248 هيبقوا

data_type = df.dtypes
num_of_unique_data = df.nunique()

# print(pd.DataFrame({"Data Type:": data_type, "Unique Data:": num_of_unique_data}))
print(pd.DataFrame({"Data Type:": data_type, "Unique Data:": num_of_unique_data}).T)

print("=" * 30)

# Another Way to Check DataTypes
# ------------------------------
from preprocessing_data import check_data_type

print(check_data_type(df))

print("#" * 30)

# Second thing to do is to HANDLE DataType [2]
# --------------------------------------------
categorical_columns = [
    "Survived",
    "Pclass",
    "Sex",
    "SibSp",
    "Parch",
    "Embarked",
]  # Other Columns (Features) are CONTINUOUS

df[categorical_columns] = df[categorical_columns].astype("category")
print(check_data_type(df))

print("#" * 30)

# Third thing to do is to CHECK NULLS [3]
# ---------------------------------------
# null_data = df.isnull()
# print(null_data)
null_data = df.isnull().sum()
print(null_data)

print("=" * 30)

# Now, we want to See The Null PERCENTAGE

null_data = df.isnull().sum()
num_of_rows_in_data_frame = df.shape[0]
null_ratio = null_data / num_of_rows_in_data_frame
print(null_ratio)

print("=" * 30)

# print(pd.DataFrame({"Nulls:": null_data, "Null Ratio:": null_ratio}))
print(pd.DataFrame({"Nulls:": null_data, "Null Ratio:": null_ratio}).T)

print("=" * 30)

# Another Way
from preprocessing_data import check_nulls_in_data_frame

print(check_nulls_in_data_frame(df))

print("#" * 30)

# Fourth thing to do is to HANDLE NULLS [4]
# -----------------------------------------
# If Nulls is Way Too Many => DROP THE ENTIRE COLUMN (FEATURE)
# If Nulls is Way Too Small => DROP Just The NULL ROWS
# If Nulls is In Between (not too small, not too many) => FILL THE NULLS WITH The MEAN or The MEDIAN (Most Common)

# For example, the "Cabin" Column (Feature) has too many nulls => Drop the Entire Column (Feature)
# "Embarked" Column (Feature) has only two null rows => Just Drop these Two Rows (Null Rows)
# "Age" Column (Feature) has average nulls (not too small, not too many) => FILL THE NULL WITH MEDIAN

df.dropna(
    subset=["Embarked"], inplace=True
)  # OR => df.dropna(subset="Embarked", inplace=True) (Since It Is One Feature)
df.drop(labels=["Cabin"], axis=1, inplace=True)

# Fill "Age" Column (Feature) With The Median
age_median = df["Age"].median()
# print(age_median)
# df["Age"].fillna(age_median, inplace=True)  # Work in Jupyter Notebook
df.fillna({"Age": age_median}, inplace=True)

# print(df.head())
print(check_nulls_in_data_frame(df))

print("#" * 30)


# Fifth thing to do is to CHECK OUTLIERS [5]
# ------------------------------------------
# - IQR Technique (Interquartile Range) -
# ---------------------------------------
#  -1    |  20 25 30 40 55 ... |  90  120
#  OL   IQR       Data        IQR   OL
# ---------------------------------------
# [1] - Sorting => Median (Medianيبقي علطول يجيي في دماغك سيرة ال ،Sorting مادام قولنا)
# [2] - Calculate "Q2" <= Medianبسمِّي ال
# [3] - Take The Left Part (Lower Part) and Get The Median For It (Name It "Q1")
# [4] - Take The Right Part (Higher Part) and Get The Median For It (Name It "Q3")
# [5] - Calculate IQR = Q3 - Q1
# [6] - Calculate Lower Fence = Q1 - 1.5 * IQR
# [7] - Calculate Upper Fence = Q3 + 1.5 * IQR

print(df.describe())
# 25% => Q1
# 50% => Q2
# 75% => Q3

print("#" * 30)

import matplotlib.pyplot as plt
import seaborn as sns

# num_cols = df.select_dtypes("number")
num_cols = df.select_dtypes("number").columns
print(num_cols)

plt.figure(figsize=(8, 1))
for i, col in enumerate(num_cols):
    plt.subplot(1, 2, i + 1)
    sns.boxplot(df[col], orient="h")

print("#" * 30)

# print(df["Age"])  # Check "Age" Data

for col in num_cols:
    Q1 = df[col].quantile(0.25)
    # print(Q1)

    # Q2 = df[col].quantile(.50)
    # print(Q2)

    Q3 = df[col].quantile(0.75)
    # print(Q3)

    # IQR = Q3 - Q1 => اصلا Outliers وراني مين فيهم اللي عنده IQRوبالتالي ال .. Q1 & Q3 جابلي المسافة بين IQRلما طرحتهم، ال
    IQR = Q3 - Q1  # "لما طرحتهم، عرفت الداتا بتاعتي "متركزة فين
    # print(IQR)

    lower_fence = Q1 - 1.5 * IQR
    # print(lower_fence)

    lower_fence = Q1 - 1.5 * IQR
    # print(lower_fence)

    upper_fence = Q3 + 1.5 * IQR
    # print(upper_fence)

    lower_outliers = df[df[col] < lower_fence][col].values
    # print(lower_outliers)

    upper_outliers = df[df[col] > upper_fence][col].values
    # print(upper_outliers)
    # print("-" * 30)

    # Sixth thing to do is to HANDLE OUTLIERS [6]
    # -------------------------------------------
    # df[col].replace(lower_outliers, lower_fence, inplace=True)  # Work on Jupyter Notebook
    # df[col].replace(upper_outliers, upper_fence, inplace=True)  # Work on Jupyter Notebook

    df.replace({col: lower_outliers}, value=lower_fence, inplace=True)
    df.replace({col: upper_outliers}, value=upper_fence, inplace=True)
    print(df[col])

    # Checking The Outliers One More Time
    lower_outliers = df[df[col] < lower_fence][col].values
    # print(lower_outliers)

    upper_outliers = df[df[col] > upper_fence][col].values
    # print(upper_outliers)

# You will see that the outliers are gone by now
plt.figure(figsize=(8, 1))
for i, col in enumerate(num_cols):
    plt.subplot(1, 2, i + 1)
    sns.boxplot(df[col], orient="h")

print("#" * 30)

# Seventh thing to do is to CHECK DUPLICATES [7] (Very Easy)
# ----------------------------------------------

# print(df.duplicated())
print(df.duplicated().sum())

df.drop_duplicates(inplace=True)

print("#" * 30)

# Eighth thing to do is to HANDLE DUPLICATES [8] (Very Easy)
# ----------------------------------------------

print(df.duplicated().sum())
