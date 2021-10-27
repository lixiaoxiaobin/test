import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv(r'E:\data\poc_2021_9.10.csv')


dic_tool = {}
dic_rcp = {}
dic_lot = {}

tools = sorted(set(data['tool'].tolist()))
rcps = sorted(set(data['r_c_p'].tolist()))
lots = sorted(set(data['l_ot'].tolist()))
for i,tool in enumerate(tools):
    dic_tool[tool] = i

for i,rcp in enumerate(rcps):
    dic_rcp[rcp] = i

for i,lot in enumerate(lots):
    dic_lot[lot] = i

df = pd.DataFrame()
df['tool'] = data['tool'].apply(lambda x:dic_tool[x])
df['r_c_p'] = data['r_c_p'].apply(lambda x:dic_rcp[x])
df['l_ot'] = data['l_ot'].apply(lambda x:dic_lot[x])
df['pod_interval'] = data['pod_interval']
# print(df)

model = LinearRegression()

X_train, X_test, y_train, y_test = train_test_split(df.iloc[:,:-1].values, df.iloc[:,-1].values, random_state=42)


model.fit(X_train,y_train)
# y_train_pred = model.predict(X_train)  #训练数据的预测值

y_train_pred = model.predict(X_train)  #训练数据的预测值
y_test_pred = model.predict(X_test)    #测试数据的预测值


# 计算均方误差MSE、决定系数R2
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
# print(y_train,type(y_train))
# print(y_train_pred,type(y_train_pred))
print("MSE of train: %.2f, test, %.2f" % (
                    mean_squared_error(y_train, y_train_pred),
                    mean_squared_error(y_test, y_test_pred)))

print("R^2 of train: %.2f, test, %.2f" % (
                    r2_score(y_train, y_train_pred),
                    r2_score(y_test, y_test_pred)))
