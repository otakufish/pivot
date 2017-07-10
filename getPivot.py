#encoding=UTF-8

import pandas as pd
import numpy as np

#InExcel = input()
df = pd.read_excel('C:/Users/fish/Downloads/a.xls')
df.head()

#df["Status"] = df["Status"].astype("category")
#df["Status"].cat.set_categories(["won","pending","presented","declined"],inplace=True)

values = pd.pivot_table(df,index = ["充入游戏区","支付平台"],values = ["充值卡面值"],aggfunc = np.sum,fill_value = 0)

print(values)
