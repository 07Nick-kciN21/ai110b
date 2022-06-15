def hillClimbing(s, maxGens, maxFails, map):   # 爬山演算法的主體函數
    print("start: ", s.str(map))             # 印出初始解
    fails = 0                             # 失敗次數設為 0
    sheight = 0
    
    for gens in range(maxGens):
        snew = s.neighbor()               #  取得鄰近的解
        senrgy = s.energy(map)              #  sheight=目前解的高度
        nenergy = snew.energy(map)           #  nheight=鄰近解的高度
        if (nenergy < senrgy):          #  如果鄰近解比目前解更好
            s = snew                      #    就移動過去
            fails = 0                     #    移動成功，將連續失敗次數歸零
        else:                             #  否則
            fails = fails + 1             #    將連續失敗次數加一
        if (fails >= maxFails):
            break
    
    print("solution: ", s.str(map))          #  印出最後找到的那個解
    return s                              #    然後傳回。
