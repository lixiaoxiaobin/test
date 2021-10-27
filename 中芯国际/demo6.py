import pandas as pd
import time
#对start_times和load_times分别进行排序，分析未按照排队顺序加工的工件
df = pd.read_csv(r'E:\data\T01.csv')

df.drop_duplicates(subset=['r_c_p','batch_seq'],inplace=True)



df['start_times'] = df['lotstart_time'].apply(lambda x:time.mktime(time.strptime(str(x), "%d.%m.%Y %H:%M:%S")))
df['load_times'] = df['load_time'].apply(lambda x:time.mktime(time.strptime(str(x), "%d.%m.%Y %H:%M:%S")))
lot_sort = df.sort_values('start_times')  #按照lot加工时间进行排序
load_sort = df.sort_values('load_times')  #按照load加工时间进行排序
lot_sort.reset_index(inplace=True)
load_sort.reset_index(inplace=True)
lot_sort = lot_sort.drop(columns=['level_0','index'])
load_sort = load_sort.drop(columns=['level_0','index'])

#将两个表拼接
lot_sort_c = lot_sort[['r_c_p','batch_seq','lotstart_time']].copy()
lot_sort_c['l_r_c_p'] = load_sort['r_c_p']
lot_sort_c['l_batch_seq'] = load_sort['batch_seq']
lot_sort_c['load_time'] = load_sort['load_time']

#未按照load顺序加工工件的个数
count = 0
for i in range(len(lot_sort_c)):
    if lot_sort_c.loc[i,'r_c_p'] != lot_sort_c.loc[i,'l_r_c_p']:
        count += 1

print(count)