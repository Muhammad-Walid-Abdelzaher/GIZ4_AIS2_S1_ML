import pandas as pd


def chk(data_frame):

    dtype = data_frame.dtypes
    n_unique = data_frame.nunique()
    return pd.DataFrame({"Dtypes": dtype, "Num_Unique": n_unique}).T


def chk_nulls(data_frame):

    nul = data_frame.isnull().sum()
    ratio = nul / data_frame.shape[0]
    return pd.DataFrame({"Null": nul, "Ratio": ratio}).T
