import pandas as pd
import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import minmax_scale
from sklearn.model_selection import train_test_split



data = pd.read_csv(r'E:\data\poc_2021_9.10.csv')
data.drop_duplicates(subset=['r_c_p','batch_seq'],keep='last',inplace=True)
data = data[data['l_ot_type']=='Prod']
data.reset_index(inplace=True)
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
# df['l_ot'] = data['l_ot'].apply(lambda x:dic_lot[x])
df['batch_seq'] = data['batch_seq']
df['lot_end-lot_start'] = data['lot_end-lot_start']

# print(minmax_scale(df.iloc[:,:-1].values))
# df.to_csv('df.csv')
model = MLPRegressor(hidden_layer_sizes=(100,),random_state=1,learning_rate_init=0.01)
model.fit(minmax_scale(df.iloc[:,:-1].values), df.iloc[:,-1].values)

pre = model.predict(minmax_scale(df.iloc[:,:-1].values))


print(np.abs(df.iloc[:,-1]-pre).mean())
# print(df.iloc[:,-1]-pre)

from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error

print("均方误差MSE: %.2f" % (
                    mean_squared_error(df.iloc[:,-1].values, pre)))

print("r2: %.2f" % (
                    r2_score(df.iloc[:,-1].values, pre)))