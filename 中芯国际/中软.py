import pandas as pd
import time
import re

data = pd.read_excel(r'C:\Users\LZB\Desktop\中软.xlsx')
#删除空值
data.dropna(inplace=True)
#去掉重复值
data.drop_duplicates(subset=['b-d'],inplace=True)

data.reset_index(inplace=True)


df = data.copy()
#数据计算处理
df['start_times'] = df['lotstart_time'].apply(lambda x:time.mktime(time.strptime(str(x), "%d.%m.%Y %H:%M:%S")))
df['lotend_times'] = df['lotend_time'].apply(lambda x:time.mktime(time.strptime(str(x), "%d.%m.%Y %H:%M:%S")))
df['t2(S)'] = df['t2(S)'].apply(lambda x:int(re.findall(r'\d+',str(x))[0]))
df['t4(S)'] = df['t4(S)'].apply(lambda x:int(re.findall(r'\d+',str(x))[0]))
df['t5/t6(S)'] = df['t5/t6(S)'].apply(lambda x:int(re.findall(r'\d+',str(x))[0]))
df['times'] = df['lotend_times'] - df['start_times']
#tank不算X的加工时间和
df['t_times'] = -1

for i in range(len(df)):
    t = df.iloc[i,4:10].sum()
    df.loc[i,'t_times'] = t

#芯片加工时间 - tank不算x的时间
df['x_time'] = df['times'] - df['t_times']

#处理完的数据添加到原data中
data['times'] = df['times']
data['t_times'] = df['t_times']
data['x_time'] = df['x_time']

finall_data = df[['b-d','t1(S)','t2(S)','t3(S)','t4(S)','t5/t6(S)','t7(S)']][:10].values.tolist()
print(finall_data)
batch_dict = {}

for i in finall_data:
    batch_dict[i[0]] = i[1:]
print(batch_dict)

