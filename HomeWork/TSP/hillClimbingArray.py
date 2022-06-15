from hillClimbing import hillClimbing # 引入爬山演算法類別
from solutionArray2 import SolutionArray # 引入平方根解答類別
import random

def getlen(data):
    path = 'data/' + data
    f= open(path)
    lines = []
    for line in f.readlines():
        l = line.split(' ')
        lines.append(l)

    arrays = []
    for line in lines:
        array = [] 
        for l in line:
            if(l != '' and l!=' '):
                array.append(int(l))
        arrays.append(array)
    return arrays, len(arrays)

# print(x)
# map, l = getlen(data)
x = random.sample(range(l),l)
hillClimbing(SolutionArray(x), 10000, 1000, map)

