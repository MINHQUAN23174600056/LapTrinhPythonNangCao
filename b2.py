import pandas as pd
import numpy as np
mylist = list('abcdefghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
series_from_list = pd.Series(mylist)
series_from_array = pd.Series(myarr)
series_from_dict = pd.Series(mydict)
ser = pd.Series(mydict)
# Chuyển Series thành DataFrame
df = ser.reset_index()
df.columns = ['Character', 'Number']  # Đặt tên cột
print("\nDataFrame từ Series:")
print(df)
