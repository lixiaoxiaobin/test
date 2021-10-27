from matplotlib import pyplot as plt
import pandas as pd
import os
#将csv文件数据画成折线图
files = [i[2] for i in os.walk('../T01')][0]
plt.figure(figsize=(100,15))
for file in files:

    name = file.split('.')[0]
    data = pd.read_csv(f'../T01/{file}')
    # print(data)

    plt.scatter(data['pod_arrive'] , data['times'])
    plt.plot(data['pod_arrive'] , data['times'])
    plt.xticks(data['pod_arrive'],rotation=30,fontsize='small')

    plt.savefig(f'../T01_picters/{name}.jpg')
    plt.clf()
    # plt.show()
