import pandas as pd

def check_data_type(df):
    data_type = df.dtypes
    num_of_unique_data = df.nunique()
    return pd.DataFrame({"Data Type:": data_type, "Unique Data:": num_of_unique_data}).T


def check_nulls_in_data_frame(df):
    null_data = df.isnull().sum()
    num_of_rows_in_data_frame = df.shape[0]
    null_ratio = null_data / num_of_rows_in_data_frame
    return pd.DataFrame({"Nulls:": null_data, "Null Ratio:": null_ratio}).T
