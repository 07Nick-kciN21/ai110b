from solution import Solution
from random import random, randint

# 改成二維矩陣
class SolutionArray(Solution):
    # 隨機選一個維度，進行移動
    def neighbor(self):           #  多變數解答的鄰居函數。
        nv = self.v.copy()        #  nv=v.clone()=目前解答的複製品
        # 隨機選擇要交換的兩點
        i = randint(0, len(nv)-1) 
        j = randint(0, len(nv)-1) 
        x =  nv[i]
        nv[i] = nv[j]
        nv[j] = x
        return SolutionArray(nv)  #  傳回新建的鄰居解答。
    # 能量計算
    def energy(self): #  能量函數
        maps = [[100,5,6,3],
                [5,100,8,2],
                [6,8,100,1],
                [3,2,1,100]]
        paths = self.v
        cost = 0
        for i in range(0, len(paths)-1):
            cost += maps[paths[i]][paths[i+1]]
        cost += maps[paths[len(paths)-1]][paths[0]]
        return cost
    # 顯示
    def str(self):    #  將解答轉為字串的函數，以供列印用。
        return "energy({:s})={:f}".format(str(self.v), self.energy())


