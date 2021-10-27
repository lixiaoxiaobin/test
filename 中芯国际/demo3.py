import pandas as pd
import numpy as np
import time

data = pd.read_csv(r'C:\Users\LZB\Desktop\POC_20210901_Raw.CSV')

data['track_in-pod_arrive'] = -1
data['load-track_in'] = -1
data['lot_start-load'] = -1
data['lot_end-lot_start'] = -1
data['unload-lot_end'] = -1
data['track_out-unload'] = -1
data['pod_remove-track_out'] = -1
data['pod_interval'] = -1
data.dropna(inplace=True)
data.reset_index(inplace=True)
#计算八个时间段的差
for i in range(len(data)):
    if int(i % 100) == 0:
        print("\rUpdate start: {:.2%} ".format(i / data.shape[0]), end='')
    elif i == data.shape[0] - 1:
        print("\rUpdate over: 100% ", end='')

    pod_arrive_timeArray = time.strptime(str(data.loc[i]['pod_arrive']), "%d.%m.%Y %H:%M:%S")
    trackin_timeArray = time.strptime(str(data.loc[i]['trackin_time']), "%d.%m.%Y %H:%M:%S")
    load_timeArray = time.strptime(str(data.loc[i]['load_time']), "%d.%m.%Y %H:%M:%S")
    lotstart_timeArray = time.strptime(str(data.loc[i]['lotstart_time']), "%d.%m.%Y %H:%M:%S")
    lotend_timeArray = time.strptime(str(data.loc[i]['lotend_time']), "%d.%m.%Y %H:%M:%S")
    unload_timeArray = time.strptime(str(data.loc[i]['unload_time']), "%d.%m.%Y %H:%M:%S")
    trackout_timeArray = time.strptime(str(data.loc[i]['trackout_time']), "%d.%m.%Y %H:%M:%S")
    pod_remove_timeArray = time.strptime(str(data.loc[i]['pod_remove']), "%d.%m.%Y %H:%M:%S")

    m1 = int(time.mktime(trackin_timeArray) - time.mktime(pod_arrive_timeArray))
    m2 = int(time.mktime(load_timeArray) - time.mktime(trackin_timeArray))
    m3 = int(time.mktime(lotstart_timeArray) - time.mktime(load_timeArray))
    m4 = int(time.mktime(lotend_timeArray) - time.mktime(lotstart_timeArray))
    m5 = int(time.mktime(unload_timeArray) - time.mktime(lotend_timeArray))
    m6 = int(time.mktime(trackout_timeArray) - time.mktime(unload_timeArray))
    m7 = int(time.mktime(pod_remove_timeArray) - time.mktime(trackout_timeArray))
    m8 = int(time.mktime(pod_remove_timeArray) - time.mktime(pod_arrive_timeArray))
    data.loc[i, 'track_in-pod_arrive'] = m1
    data.loc[i, 'load-track_in'] = m2
    data.loc[i, 'lot_start-load'] = m3
    data.loc[i, 'lot_end-lot_start'] = m4
    data.loc[i, 'unload-lot_end'] = m5
    data.loc[i, 'track_out-unload'] = m6
    data.loc[i, 'pod_remove-track_out'] = m7
    data.loc[i, 'pod_interval'] = m8

# data.to_csv('./poc_2021_9.10.csv')
