import random 
import sys
import time
from torch import rand




# 棋盤
class Board:
    def __init__(self, rMax, cMax):
        self.m = [None] * rMax
        self.rMax = rMax
        self.cMax = cMax
        for r in range(rMax):
            self.m[r] = [None] *cMax
            for c in range(cMax):
                self.m[r][c] = '-'

    def __str__(self):
        b = []
        b.append('  0 1 2 3 4 5 6 7 8 9 a b c d e f')
        for r in range(self.rMax):
            b.append('{:x} {:s} {:x}'.format(r, ' '.join(self.m[r]), r))
            b.append('  0 1 2 3 4 5 6 7 8 9 a b c d e f')
            return '\n'.join(b)
    def show(self):
        print(str(self))

shape_score = [(60, (1, 1, 0, 0, 0))
               (60, (0, 1, 1, 0, 0)),
               (60, (0, 0, 1, 1, 0)),
               (60, (0, 0, 0, 1, 1)),
               (100, (1, 1, 0, 1, 0)),
               (100, (0, 0, 1, 1, 1)),
               (100, (1, 1, 1, 0, 0)),
               (3000, (0, 1, 1, 1, 0)),
               (3000, (0, 1, 0, 1, 1, 0)),
               (3000, (0, 1, 1, 0, 1, 0)),
               (3000, (1, 1, 1, 0, 1)),
               (3000, (1, 1, 0, 1, 1)),
               (3000, (1, 0, 1, 1, 1)),
               (3000, (1, 1, 1, 1, 0)),
               (3000, (0, 1, 1, 1, 1)),
               (40000, (0, 1, 1, 1, 1, 0)),
               (99999999, (1, 1, 1, 1, 1))]

listAI = []
listHuman = []
listAllStep = []

listBoard = []

next_point = [0,0]

ratio = 1
DEPTH = 3
        
for i in range(16):
    for j in range(16):
        listBoard.append((i,j))

# 電腦棋路計算
def ai():
    global cut_count 
    cut_count = 0
    global search_count
    search_count = 0
    first_count = 0
    # 先手AI第一步
    firstPoint = (8,8)
    if not listAllStep: 
        listAllStep.append(firstPoint)
        listAI.append(firstPoint)

        return firstPoint[0],firstPoint[1]
    else:
        negamax(True, DEPTH, -99999999, 99999999)

# 
def negamax(is_ai, depth, alpha, beta):
    if depth==0:
        return evaluation(is_ai)
    # 去掉已經下過的位置
    blank_list = list(set(listBoard).difference(set(listAllStep)))
    # 排序
    order(blank_list)
    # 對每個空位做檢查
    for next_step in blank_list:
        global search_count
        search_count += 1
        # 如果這位周圍沒有棋子，就跳過
        if not has_heightnor(next_step):
            continue
        if is_ai:
            listAI.append(next_step)
        else:
            listHuman.append(next_step)
        listAllStep.append(next_step)
        value = -negamax(not is_ai, depth-1, -beta, -alpha)
        if is_ai:
            listAI.remove(next_step)
        else:
            listHuman.remove(next_step)
        listAllStep.remove(next_step)
        if value > alpha:
            if depth == DEPTH:
                next_point[0] = next_step[0]
                next_point[1] = next_step[1]
            if value >= beta:
                global cut_count
                cut_count += 1
                return beta
            alpha = value
        return alpha

def order(blank_list):
    last_pt = listAllStep[-1]
    for item in blank_list:
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i==0 and j==0:
                    continue
                if(last_pt[0]+i, last_pt[1]+j) in blank_list:
                    blank_list.remove((last_pt[0]+i, last_pt[1]+j))
                    blank_list.insert(0,(last_pt[0]+i,last_pt[1]+j))


def has_heightnor(pt):
    for i in range(-1,2):
        for j in range(-1,2):
            if i==0 and j==0:
                continue
            if (pt[0]+i, pt[1]+j) in listAllStep:
                return True

def evaluation(is_ai):
    total_score = 0
    if is_ai:
        my_list=listAI
        enemy_list = listHuman
    else:
        my_list=listHuman
        enemy_list = listAI
    score_all_arr = []
    my_score = 0
    for pt in my_list:
        m = pt[0]
        n = pt[1]
        muy_score += cal_score(m,n,0,1,enemy_list,my_list,score_all_arr)
        muy_score += cal_score(m,n,1,0,enemy_list,my_list,score_all_arr)
        muy_score += cal_score(m,n,1,1,enemy_list,my_list,score_all_arr)
        muy_score += cal_score(m,n,-1,1,enemy_list,my_list,score_all_arr)

    score_all_arr_enemy = []
    enemy_score = 0
    for pt in enemy_list:
        m = pt[0]
        n = pt[1]
        muy_score += cal_score(m,n,0,1,my_list,enemy_list,score_all_arr)
        muy_score += cal_score(m,n,1,0,my_list,enemy_list,score_all_arr)
        muy_score += cal_score(m,n,1,1,my_list,enemy_list,score_all_arr)
        muy_score += cal_score(m,n,-1,1,my_list,enemy_list,score_all_arr)
    total_score = my_score-enemy_score*ratio*0.1
    return total_score

def cal_score(m, n, x_decrict, y_derice, enemy_list, my_list, score_all_arr):
    add_score = 0
    max_score_shape = (0,None)

    for item in score_all_arr:
        for pt in item[1]:
            if m == pt[0] and n == pt[1] and x_decrict == item[2][0] and y_derice == item[2][1]:
                return 0

    for offset in range(-5,1):
        pos=[]
        for i in range(0,6):
            if(m+(i+offset)*x_decrict, n+(i+offset)*y_derice) in  enemy_list:
                pos.append(2)
            elif (m + (i + offset) * x_decrict, n + (i + offset) * y_derice) in my_list:
                pos.append(1)
            else:
                pos.append(0)
        tmp_shap5 = (pos[0], pos[1], pos[2], pos[3], pos[4])
        tmp_shap6 = (pos[0], pos[1], pos[2], pos[3], pos[4], pos[5])

        for (score, shape) in shape_score:
            if tmp_shap5 == shape or tmp_shap6 == shape:
                if score > max_score_shape[0]:
                    max_score_shape = (score, ((m + (0+offset) * x_decrict, n + (0+offset) * y_derice),
                                               (m + (1+offset) * x_decrict, n + (1+offset) * y_derice),
                                               (m + (2+offset) * x_decrict, n + (2+offset) * y_derice),
                                               (m + (3+offset) * x_decrict, n + (3+offset) * y_derice),
                                               (m + (4+offset) * x_decrict, n + (4+offset) * y_derice)), (x_decrict, y_derice))
def now_human(board, turn):
    global listAllStep
    try:
        xy = input(f"將{turn}下在?")
        r = int(xy[0], 16)
        c = int(xy[1], 16)
        # 要下在邊界裡
        if r < 0 or r > board.rMax or c < 0 or c > board.cMax:
            raise Exception (f"{r}, {c} is out of border")
        # Not empty
        if board.m[r][c] != "-":
            raise Exception (f"{r}, {c} is occupied.")
        board.m[r][c] = turn
        listHuman.append((r, c))
        listAllStep.append((r, c))
    except Exception as e:
        print("!!!!!!!!!!!!!! Attention !!!!!!!!!!!!!!\n")
        print(f"Got Error {e}")
        print("\n!!!!!!!!!!!!!! Attention !!!!!!!!!!!!!!")
        now_human(board, turn)
# ai下棋
def now_computer(board, turn):
    print("Computer's Turn")
    # 計算
    aiStep = ai()
    board.m[aiStep[0]][aiStep[1]]=turn
    listAllStep.append(aiStep)
    listAI.append(aiStep)

z9 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
i9 = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
d9 = [4, 3, 2, 1, 0, -1, -2, -3, -4]
z5 = [0, 0, 0, 0, 0]
i2 = i9[2:-2]
d2 = d9[2:-2]

def patternCheck(board, turn, r, c, dr, dc):
    for i in range(len(dr)):
        tr = round(r+dr[i])
        tc = round(c + dc[i])
        if tr<0 or tr>=board.rMax or tc<0 or tc>=board.cMax:
            return False
        v = board.m[tr][tc]
        if(v != turn):
            return False
    return True

def chess(o,x):
    # 棋盤
    b = Board(16,16)
    b.show()
    while True:
        print(o)
        if o=='p':
            now_human(b,'o')
        else:
            now_computer(b,'o')
        winCheck(b,'o')
        if x=='p':
            now_human(b, 'x')
        else:
            now_computer(b, 'x')
        b.show()
        winCheck(b, 'x')

def winCheck(board, turn):
    win = False
    tie = True
    # 搜尋棋局
    for r in range(board.rMax):
        for c in range(board.cMax):
            tie = False if board.m[r][c] == '-' else tie
            win = True if patternCheck(board, turn, r, c, z5, i2) else win #  水平 -
            win = True if patternCheck(board, turn, r, c, i2, z5) else win #  垂直 |
            win = True if patternCheck(board, turn, r, c, i2, i2) else win #  下斜 \
            win = True if patternCheck(board, turn, r, c, i2, d2) else win #  上斜 /
    if(win):
        print('{} 贏了！'.format(turn))  #  如果贏了就印出贏了
        sys.exit() #  然後離開。
    if(tie):
        print('平手')
        sys.exit(0) #  然後離開。

    return win
user1 = input("user1:").lower()
user2 = input("user2:").lower()
o,x = user1, user2
user1 = "Computer" if user1=="c" else "Human"
user2 = "Computer" if user2=="c" else "Human"
print(f"User1 : {user1}, User2 : {user2}")
# 進入遊戲
chess(o, x)
