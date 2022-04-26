class Solution: # 解答的物件模版 (類別)
    def __init__(self, v, step = 0.01):
        self.v = v       # 參數 v 為解答的資料結構
        self.step = step # 每一小步預設走的距離
        f= open('data/gr17_d.txt')
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
        self.map = arrays
    # 以下兩個函數至少需要覆蓋掉一個，否則會無窮遞迴
    def height(self): # 爬山演算法的高度函數
        return -1*self.energy()               # 高度 = -1 * 能量

    def energy(self): # 尋找最低點的能量函數
        return -1*self.height()               # 能量 = -1 * 高度
    

