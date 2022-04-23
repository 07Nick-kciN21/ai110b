now_map = []

#計算路線
def cost():
    return 

#交換函數
def exchange(a, b):
    x = a
    a = b
    b = x
    return 
    
#是否交換
def if_change():
    next_map = exchange(a,b)
    next_cost = cost(next_map)
    if(next_cost > now_cost):
        now_map = next_map
        now_cost = next_cost