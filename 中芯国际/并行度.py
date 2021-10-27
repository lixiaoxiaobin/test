import pandas as pd
import time
#查找每个机台产品加工时间段内有并集的数据，并记录并集加工的个数
df = pd.read_csv(r'E:\data\T02.csv')

df.drop_duplicates(subset=['r_c_p','batch_seq'],inplace=True)


df['start_times'] = df['lotstart_time'].apply(lambda x:time.mktime(time.strptime(str(x), "%d.%m.%Y %H:%M:%S")))
df['end_times'] = df['lotend_time'].apply(lambda x:time.mktime(time.strptime(str(x), "%d.%m.%Y %H:%M:%S")))
df.sort_values('start_times',inplace=True)  #按照lot加工时间进行排序
df.reset_index(inplace=True)
df = df.drop(columns=['level_0','index'])
# df.to_csv('t02_df.csv')

all_list = [] #存储交集时间段内并行运行的tank数
for k in range(len(df)):
    if int(k % 100) == 0:
        print("\rUpdate start: {:.2%} ".format(k / df.shape[0]), end='')
    elif k == df.shape[0] - 1:
        print("\rUpdate over: 100% ", end='')

    data = df[(df['start_times'] <= df.loc[k, 'end_times']) & (df['start_times'] >= df.loc[k, 'start_times'])]
    data.reset_index(inplace=True)

    count = 1 #时间段内并行加工的芯片数
    count_list = []
    time_begin = data.loc[0,'start_times'] #交集开始时间
    time_finish = data.loc[0,'end_times'] #交集结束时间
    if len(data) == 1:
        start_time = data.loc[0, 'lotstart_time']
        end_time = data.loc[0, 'lotend_time']
        count_list.append(f'{start_time}--{end_time}')
        count_list.append(1)

        all_list.append(count_list)
    elif len(data) > 1:
        for i in range(1,len(data)):
            if data.loc[i,'start_times'] >= time_begin and data.loc[i,'start_times'] <= time_finish: #在交集时间内 count+1
                time_begin = data.loc[i, 'start_times']
                if data.loc[i,'end_times'] <= time_finish:
                    time_finish = data.loc[i, 'end_times']

                count += 1
            else:
                break
        start_time = data.loc[0, 'lotstart_time']
        end_time = data.loc[0, 'lotend_time']
        count_list.append(f'{start_time}--{end_time}')
        count_list.append(count)

        all_list.append(count_list)



show_df = pd.DataFrame(columns=['time','count'],data=all_list)
# show_df.to_csv('T02_show_df.csv')

print(show_df['count'].max())

