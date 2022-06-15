from hillClimbing import hillClimbing # 引入爬山演算法類別
from solutionArray2 import SolutionArray # 引入平方根解答類別
import random

x = random.sample(range(17),17)
# print(x)
for i in range(10):
    # x = random.sample(range(17),17)
    hillClimbing(SolutionArray(x), 10000, 1000)