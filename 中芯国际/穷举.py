data = [[0, 0, 0, 0, 1281, 420], [ 300, 300, 348, 300, 1281, 420], [ 300, 600, 0, 0, 1436, 420], [ 0, 0, 0, 0, 1961, 420], [300, 300, 58, 300, 500, 420]]

from demo.test import process
import itertools
sort_list = list(itertools.permutations(data,len(data)))

import copy
pro_time = []
for i in sort_list:
    a = copy.deepcopy(list(i))
    # print(process(a))

    pro_time.append(process(a)[0])


print(min(pro_time))
print(sort_list[pro_time.index(min(pro_time))])
print(process(list(sort_list[pro_time.index(min(pro_time))])))