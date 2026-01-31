import pandas as pd

s = pd.Series([1, 2, 3, 4])
print(s)

print("#" * 30)

s = pd.Series([1, 2, 3, 4], index=["a", "b", "c", "d"])
print(s)

print("#" * 30)

data = [[1, 444, "abc"], [2, 555, "def"], [3, 666, "ghi"], [4, 444, "xyz"]]

df = pd.DataFrame(data)
print(df)

print("#" * 30)

data_dic = {
    "id": [1, 2, 3, 4],
    "salary": [444, 555, 666, 444],
    "dept": ["abc", "def", "ghi", "xyz"],
}

df_1 = pd.DataFrame(data_dic)
print(df_1)

print("#" * 30)

df = pd.DataFrame(data, columns=["id", "salary", "dept"])
print(df)

print("=" * 30)

x = df.columns
index = ["R1", "R2", "R3", "R4"]
df.index = index
print(df)

print("=" * 30)

print(df.dtypes)

print("=" * 30)

print(df["dept"].dtypes)

print("=" * 30)


def chk(df, ty):

    return df[ty].dtype


print(chk(df, "dept"))
print(chk(df, "salary"))

print("=" * 30)

df["dept"] = df["dept"].astype("category")
print(df.dtypes)
print(df["dept"].dtype)

print("#" * 30)

print(df.head(2))

print("=" * 30)

print(df.tail(2))

print("#" * 30)

print(df.describe())

print("#" * 30)

print(df.columns)
print(df.index)

print("#" * 30)

print(df["salary"].unique())
print(df["salary"].nunique())

print("#" * 30)

print(df["salary"].min())
print(df["salary"].max())
print(df["salary"].idxmin())
print(df["salary"].idxmax())

print("#" * 30)

df.info()

print("#" * 30)

print(df["salary"].sum())

print("#" * 30)

print(df["salary"].values)

print("=" * 30)

print(df.values)

print("#" * 30)

print(df.replace(444, "Ali"))

print("#" * 30)

print(df["dept"].iloc[2])
print(df.values)

print("#" * 30)

print(df.iloc[2, 1])  # Row, Column

print("#" * 30)

print(df["salary"].iloc[:])

print("#" * 30)

print(df["salary"].iloc[0:2])

print("#" * 30)

print(df.iloc[:, 0:2])  # All Rows, Specific Columns (مهمة جدا)

print("#" * 30)
