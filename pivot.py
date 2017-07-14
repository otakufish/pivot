#encoding=UTF-8

import sys
import pandas as pd
import numpy as np

try:    #檢查有無輸入檔名
    InputFile = sys.argv[1]    #有輸入的話就用輸入檔執行
    df = pd.read_excel(InputFile)
except IndexError:
    df = pd.read_excel(r'C:\Users\fishwang\Downloads\充值订单.xls')    #無輸入則使用預設位置與檔案
df.head()

values = pd.pivot_table(df,index = ["充入游戏区","支付平台"],values = ["充值卡面值"],aggfunc = np.sum,fill_value = 0)
print(values)

#自動產出csv檔
values.to_csv('output_file.csv')