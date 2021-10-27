import pandas as pd
import numpy as np
import time

data = pd.read_csv(r'C:\Users\LZB\Desktop\POC_20210901_Raw.CSV')

data['pod_times'] = -1
data['track_times'] = -1
data['load_times'] = -1
data['lot_times'] = -1
data.dropna(inplace=True)
data.reset_index(inplace=True)
#计算四段时间差
for i in range(len(data)):
    arrive_timeArray = time.strptime(str(data.loc[i]['pod_arrive']), "%d.%m.%Y %H:%M:%S")
    remove_timeArray = time.strptime(str(data.loc[i]['pod_remove']), "%d.%m.%Y %H:%M:%S")

    in_timeArray = time.strptime(str(data.loc[i]['trackin_time']), "%d.%m.%Y %H:%M:%S")
    out_timeArray = time.strptime(str(data.loc[i]['trackout_time']), "%d.%m.%Y %H:%M:%S")

    load_timeArray = time.strptime(str(data.loc[i]['load_time']), "%d.%m.%Y %H:%M:%S")
    unload_timeArray = time.strptime(str(data.loc[i]['unload_time']), "%d.%m.%Y %H:%M:%S")

    start_timeArray = time.strptime(str(data.loc[i]['lotstart_time']), "%d.%m.%Y %H:%M:%S")
    end_timeArray = time.strptime(str(data.loc[i]['lotend_time']), "%d.%m.%Y %H:%M:%S")

    m1 = int(time.mktime(remove_timeArray)-time.mktime(arrive_timeArray))
    m2 = int(time.mktime(out_timeArray)-time.mktime(in_timeArray))
    m3 = int(time.mktime(end_timeArray)-time.mktime(start_timeArray))
    m4 = int(time.mktime(end_timeArray)-time.mktime(start_timeArray))
    data.loc[i,'pod_times'] = m1
    data.loc[i,'track_times'] = m2
    data.loc[i,'时间load_times差'] = m3
    data.loc[i,'时间差'] = m4


# data.to_csv('./poc.csv')