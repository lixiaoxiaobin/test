import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import time
#将每个机台每天arrive-remove时间段的折线图
df = pd.read_csv(r'C:\Users\LZB\Desktop\T09.csv')
df.drop_duplicates(subset=['r_c_p','batch_seq'],keep='last',inplace=True)
df.reset_index(inplace=True)
df = df.drop(columns=['level_0','index'])

plt.figure(figsize=(20,30))

for j in range(1,32):
    # 86399----->一天的秒数，1627747200---->01.08.2021 00:00:00
    data = df[(df['arrive_tims'] <= (1627747200 + (j*86399)) ) & (df['arrive_tims'] > (1627747200 + ((j-1)*86399)))]

    data.reset_index(inplace=True)

    for i in range(len(data)):
        plt.scatter(data.loc[i,['arrive_tims','remove_tims']],data.loc[i,['pod_arrive','pod_arrive']],marker='*')
        plt.plot(data.loc[i,['arrive_tims','remove_tims']],data.loc[i,['pod_arrive','pod_arrive']])
        plt.ylabel('T09')

    # plt.savefig(f'../T09_2021_8.1-9.1/{j}.jpg')
    plt.clf()
    plt.show()


