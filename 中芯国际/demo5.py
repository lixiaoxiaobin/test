import pandas as pd
import numpy as np
import time
#找到pod_arrive-pod_remove这一时间段内没有加工交集的数据，将表存成csv格式
data = pd.read_csv(r'C:\Users\LZB\Desktop\T02.csv')

data.drop_duplicates(subset=['r_c_p','batch_seq'],keep='last',inplace=True)
data.reset_index(inplace=True)
data = data.drop(columns=['level_0','index'])
# data['arrive_tims'] = data['pod_arrive'].apply(lambda x:time.mktime(time.strptime(str(x), "%d.%m.%Y %H:%M:%S")))
# data['remove_tims'] = data['pod_remove'].apply(lambda x:time.mktime(time.strptime(str(x), "%d.%m.%Y %H:%M:%S")))
# data = data[data['tool'] == 'T01']
# data.reset_index(inplace=True)
# data.to_csv('T01.csv')

count = [] #记录时间段内有交集的数据数量
for k in range(1,len(data)):
    if int(k % 100) == 0:
        print("\rUpdate start: {:.2%} ".format(k / data.shape[0]), end='')
    elif k == data.shape[0] - 1:
        print("\rUpdate over: 100% ", end='')
    #逐个取数据中的元素
    df = data.copy().iloc[k-1:k,:]
    df.reset_index(drop=True,inplace=True)
    #找到与df第一个元素有时间交集的数据
    m = data[(data['arrive_tims'] <= df.loc[0, 'remove_tims']) & (data['arrive_tims'] >= df.loc[0, 'arrive_tims'])]
    count.append(len(m))
    # 找到与df第一个元素没有时间交集的数据fill_data
    fill_data = data[data['arrive_tims'] > df.loc[0,'remove_tims']]
    while len(fill_data) >0:
        fill_data.reset_index(inplace=True)
        df = df.append(fill_data.loc[0])

        m = data[(data['arrive_tims'] <= fill_data.loc[0, 'remove_tims']) & (
                data['arrive_tims'] >= fill_data.loc[0, 'arrive_tims'])]
        count.append(len(m))

        fill_data = data[data['arrive_tims'] > fill_data.loc[0,'remove_tims']]


    # if len(df) >= 2:
    #     df = df.drop(columns=['index'])
    #     df.reset_index(inplace=True)
    #     df = df.drop(columns=['index'])
    #     df['times'] = 0
    #     for i in range(1,len(df)):
    #         df.loc[i,'times'] = df.loc[i, 'arrive_tims'] - df.loc[i-1, 'remove_tims']


        # rcp = data.copy().iloc[k-1:k,:]['r_c_p'][k-1]
        # l_ot = data.copy().iloc[k-1:k,:]['l_ot'][k-1]

        # df.to_csv(f'../T01/T01_{rcp}_{l_ot}.csv')


print(max(count))
