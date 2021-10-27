import pandas as pd
import numpy as np
import time
import datetime
#数据预处理
finall_data = pd.DataFrame()

data = pd.read_csv(r'E:\data\poc_2021_9.10.csv')

data.dropna(inplace=True)


tool_ids = [i[0] for i in data.groupby('tool')]

#计算时间差的均值、最小值、最大值、标准差
for tool_id in tool_ids:
    df = data[data['tool']==tool_id]
    rcp_ids = [i[0] for i in df.groupby('r_c_p')]
    for rcp_id in rcp_ids:
        mean_df = pd.DataFrame()
        df_data = df[df['r_c_p']==rcp_id]
        columns_df = [i for i in df_data.columns[14:]]
        for column in columns_df:
            mean = df_data[column].describe()['mean']
            std = df_data[column].describe()['std']

            min = df_data[column].describe()['min']
            max = df_data[column].describe()['max']

            mean_df.loc[0, 'tool'] = tool_id
            mean_df.loc[0, 'r_c_p'] = rcp_id
            mean_df.loc[0,column+'_mean'] = mean
            mean_df.loc[0,column+'_std'] = std
            mean_df.loc[0,column+'_min'] = min
            mean_df.loc[0,column+'_max'] = max

        finall_data = finall_data.append(mean_df)

# finall_data.to_csv('数据分析.csv')
print(finall_data)
print("处理完毕")

