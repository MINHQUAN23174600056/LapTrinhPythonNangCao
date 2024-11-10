import numpy as np
import pandas as pd
# Input dữ liệu
mylist = list('abcdefghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
# Tạo Series từ danh sách, mảng numpy, và từ điển
series_from_list = pd.Series(mylist)
series_from_array = pd.Series(myarr)
series_from_dict = pd.Series(mydict)
print("Series từ danh sách:")
print(series_from_list)
print("\nSeries từ mảng numpy:")
print(series_from_array)
print("\nSeries từ từ điển:")
print(series_from_dict)