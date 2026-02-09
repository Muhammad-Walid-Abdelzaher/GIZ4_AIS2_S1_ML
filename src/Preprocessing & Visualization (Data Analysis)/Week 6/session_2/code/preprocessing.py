# Data Analysis Process:
# ----------------------
# 01- Check DataType
# 02- Handle dtypes
# 03- Check Nulls
# 04- Handle Nulls
# 05- Check Outliers
# 06- Handle Outliers
# 07- Check Duplication
# 08- Handle Duplication
# 09- Data Visualization
# 10- Spliting (Data)
# 11- Normalization
# 12- Encoding

# Handling Nulls
# --------------

import pandas as pd

file_path = r"C:\Users\Muhammad Walid\Python\DEPI\GIZ4_AIS2_S1_ML\GIZ4_AIS2_S1_ML\src\Preprocessing & Visualization (Data Analysis)\Week 6\session_2\materials\train.csv"
df = pd.read_csv(file_path)
print(df.head())

print("#" * 30)

df.drop(["PassengerId", "Name", "Ticket"], axis=1, inplace=True)
print(df.head())

print("#" * 30)

dtype = df.dtypes
n_unique = df.nunique()
print(pd.DataFrame({"Dtypes": dtype, "Num_Unique": n_unique}).T)

print("-" * 30)

from pp import chk

print(chk(df))

print("-" * 30)

cols = ["Survived", "Pclass", "Sex", "SibSp", "Parch", "Embarked"]
df[cols] = df[cols].astype("category")

print(chk(df))

print("#" * 30)

print(df.shape)
print(df.shape[0])
print(df.shape[1])

print("#" * 30)

nul = df.isnull().sum()
ratio = nul / df.shape[0]
print(nul)

print("=" * 30)

print(ratio)

print("#" * 30)

print(pd.DataFrame({"Null": nul, "Ratio": ratio}).T)

print("#" * 30)

from pp import chk_nulls

print(chk_nulls(df))

print("#" * 30)

df = df.dropna(subset=["Embarked"])
df = df.drop("Cabin", axis=1)

median = df["Age"].median()
# df['Age'].fillna(median, inplace=True)  # Work in Juptyer Notebook
df.fillna({"Age": median}, inplace=True)

print(chk_nulls(df))

print("#" * 50)

# Handling Outliers
# - IQR Technique -
# -----------------
#  -1    |  20 25 30 40 55 ... |  90  120
#  OL   IQR       Data        IQR   OL
# ---------------------------------------

print(df.describe())

print("#" * 30)

import matplotlib.pyplot as plt
import seaborn as sns

# num_cols = df.select_dtypes('number')
num_cols = df.select_dtypes("number").columns
print(num_cols)

print("#" * 30)

plt.figure(figsize=(8, 1))
for i, col in enumerate(num_cols):

    plt.subplot(1, 2, i + 1)
    sns.boxplot(df[col], orient="h")

print("=" * 30)

for col in num_cols:

    Q1 = df[col].quantile(0.25)
    print(Q1)

    Q3 = df[col].quantile(0.75)
    print(Q3)

    IQR = Q3 - Q1
    print(IQR)

    lower_fence = Q1 - 1.5 * IQR
    print(lower_fence)

    upper_fence = Q3 + 1.5 * IQR
    print(upper_fence)

    lower_outliers = df[df[col] < lower_fence][col].values
    print(lower_outliers)

    upper_outliers = df[df[col] > upper_fence][col].values
    print(upper_outliers)

    df[col].replace(lower_outliers, lower_fence, inplace=True)
    print(lower_outliers)
    print("=" * 30)

    df[col].replace(upper_outliers, upper_fence, inplace=True)
    print(upper_outliers)

    print("-" * 30)

print("#" * 30)

for i, col in enumerate(num_cols):

    plt.subplot(1, 2, i + 1)
    sns.boxplot(df[col], orient="h")

print("#" * 30)

print(df.duplicated().sum())

df.drop_duplicates(inplace=True)

print(df.duplicated().sum())  # Duplicates are now REMOVED
