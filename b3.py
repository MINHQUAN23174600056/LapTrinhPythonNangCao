import pandas as pd
import numpy as np
# Input dữ liệu
ser1 = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))
# Tạo DataFrame từ hai Series
df_combined = pd.DataFrame({'Column1': ser1, 'Column2': ser2})
print("\nDataFrame từ ser1 và ser2:")
print(df_combined)
