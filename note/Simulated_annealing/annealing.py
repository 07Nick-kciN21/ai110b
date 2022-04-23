import math
import random

def P(e, enew, T): 
    # 鄰居小於目前
    if (enew < e):
        # 保持不變
        return 1
    else:
        return math.exp((e-enew)/T)

def annealing(s, maxGens) : 
    # sbest為最佳解
    sbest = s              
    # ebest為最佳解能量
    ebest = s.energy() 
    # 起始溫度                    
    T = 100                                
    for gens in range(maxGens):   
        # 找出鄰居         
        snew = s.neighbor()                
        # 目前能量
        e    = s.energy()
        # 鄰居能量                
        enew = snew.energy()           
        # 降低溫度
        T  = T * 0.995                     
        # 決定是否移動，狀況越遭移動機機率越低
        if P(e, enew, T)>random.random():  
            s = snew                      
            print("{} T={:.5f} {}".format(gens, T, s.str()))
        # 如果新解優於目前，則改變
        if enew < ebest:                 
            sbest = snew
            ebest = enew
    
    print("solution: {}", sbest.str())     
    return sbest                          
