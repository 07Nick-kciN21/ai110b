from solution import Solution
from random import random, randint

class SolutionArray(Solution):
    # 隨機選一個維度，進行移動
    def neighbor(self):           
        nv = self.v.copy()        
        i = randint(0, len(nv)-1) 
        if (random() > 0.5):      
            nv[i] += self.step
        else:
            nv[i] -= self.step
        return SolutionArray(nv)  
    # 能量計算
    def energy(self): 
        x, y, z =self.v
        return x*x+3*y*y+z*z-4*x-3*y-5*z+8 
    # 顯示
    def str(self):    
        return "energy({:s})={:f}".format(str(self.v), self.energy())


