"""
对于n批要加工的对象，这里定义一个规则，然后找到在这个规则下最优的方案。
将n个对象排成一个序列作为函数参数，最终函数输出一个n个对象的加工总时间。序列中靠前的对象将有更高的优先级，这体现在一个tank在空闲时将优先分配给优先级更高的对象占用，这样也使得一台机器尽可能地处在饱和状态工作。
对于n个对象共有n!个优先级序列，最终找到一个函数输出最小即耗时最短的序列。
"""
#试验数据
# batch_list = [[400,1000,0,0,0,900],[300,1000,100,200,400,900],[400,550,0,0,0,900]]
# batch_dict = {'a': [0, 0, 0, 0, 1281, 420], 'b': [300, 300, 348, 300, 1281, 420], 'c': [300, 600, 0, 0, 1436, 420]}
batch_dict = {'B875': [0, 0, 0, 0, 1281, 420], 'B1': [300, 300, 348, 300, 1281, 420], 'B1274': [300, 600, 0, 0, 1436, 420], 'B455': [0, 0, 0, 0, 1961, 420], 'B1085': [300, 300, 58, 300, 500, 420]}

#定义基础处理函数
def process(batch_list):
    # 定义一个记录加工全流程的列表，列表的每个元素是一个二元组，二元组的第一个元素是batch，第二个元素是tank，含义即为该步将该batch放入了该tank
    steps = []
    # 定义保存正在tank中加工的batch的列表，否则可能会出现一个batch同时出现在多个tank中的错误代码结果
    processing_batch = []
    processing_tank = []
    total_time = 0
    #每个tank被占用的剩余时间
    tank_occupy = [0,0,0,0,0,0,0]
    while len(batch_list) != 0:#每一个batch被加工完就会被移除batch列表
        for tank in range(7):
            if tank == 0:
                if tank_occupy[0] == 0:
                    for batch in range(len(batch_list)):
                        if batch not in processing_batch:
                            if batch_list[batch][0] == 0:
                                continue
                            else:
                                tank_occupy[0] = batch_list[batch][0]
                                batch_list[batch][0] = 0
                                processing_batch.append(batch)
                                processing_tank.append(0)
                                steps.append((batch,tank))
                                break

            elif tank_occupy[tank] == 0:
                for batch in range(len(batch_list)):
                    if batch not in processing_batch:
                        if tank == 5 or tank == 6:
                            temp = tank - 1
                            if batch_list[batch][temp] != 0 and sum(batch_list[batch][:temp]) == 0:
                                tank_occupy[tank] = batch_list[batch][temp]
                                batch_list[batch][temp] = 0
                                processing_batch.append(batch)
                                processing_tank.append(tank)
                                steps.append((batch, tank))
                                break

                        else:
                            if batch_list[batch][tank] != 0 and sum(batch_list[batch][:tank]) == 0:
                                tank_occupy[tank] = batch_list[batch][tank]
                                batch_list[batch][tank] = 0
                                processing_batch.append(batch)
                                processing_tank.append(tank)
                                steps.append((batch, tank))
                                break

            else:
                continue

        #在对所有的tank进行分配之后，推进一次加工步骤
        tank_occupied = [element for element in tank_occupy if element != 0]
        if len(tank_occupied) != 0:
            cost = min(tank_occupied)
        else:
            cost = 0
        total_time += cost
        for i in range(len(tank_occupy)):
            if tank_occupy[i] != 0:
                tank_occupy[i] -= cost
        for i in range(len(tank_occupy)):
            if tank_occupy[i] == 0:
                if i in processing_tank:
                    processing_batch.remove(processing_batch[processing_tank.index(i)])
                    processing_tank.remove(i)
        #更新batch_list，如果有加工玩完的batch就移除掉
        while True:
            if [0, 0, 0, 0, 0, 0] in batch_list:
                batch_list.remove([0, 0, 0, 0, 0, 0])
            else:
                break
    total_time += max(tank_occupy)

    #计算机数据结构元素下标加1为真实元素编号，方便查看
    steps_modified = [(element[0]+1,element[1]+1) for element in steps]
    return total_time,steps_modified


# print(process(batch_list))
import copy
from itertools import permutations
#定义一个调用函数
def exhaustivity(batch_dict:dict):
    result = []
    result_correlative_bathes = []
    batch_datas = list(batch_dict.values())
    batch_ids = list(batch_dict.keys())
    n = len(batch_dict)
    indexes = [i for i in range(n)]
    sequences = [list(i) for i in list(permutations(indexes))]
    for sequence in sequences:
        batch_datas_temp = []
        batch_ids_temp = []
        for i in sequence:
            batch_datas_temp.append(batch_datas[i])
            batch_ids_temp.append(batch_ids[i])

        result.append(process(copy.deepcopy(batch_datas_temp)))
        result_correlative_bathes.append(batch_ids_temp)
    result_time = [element[0] for element in result]
    return result_time,result_correlative_bathes


result_time,result_correlative_bathes = exhaustivity(batch_dict)


print(result_time,result_correlative_bathes)
min_time = min(result_time)
print('min_time=',min_time)
min_index = result_time.index(min_time)
print('min_index=',min_index)
print('min_time_list=',result_correlative_bathes[min_index])














