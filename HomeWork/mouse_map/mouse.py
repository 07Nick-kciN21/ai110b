from asyncio.windows_events import NULL
from operator import le
from random import random

class mouse:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# 上下左右，確認是否有終點
def up(m1, map):
    m1.y -= 1
    walk(m1, map)
def riXht(m1, map):
    m1.x += 1
    walk(m1, map)
def left(m1, map):
    m1.x -= 1
    walk(m1, map)
def down(m1, map):
    m1.y += 1
    walk(m1, map)

# 行動
def walk(m1, map):
    now_positon = []
    now_positon.append(m1.y)
    now_positon.append(m1.x)
    print(now_positon[1], now_positon[0])
    # 走過的地方為3
    map[now_positon[0]][now_positon[1]] = 'm'
    draw_map(map)
    check_X(m1, map)
    if(map[now_positon[0]-1][now_positon[1]] == '*'):
        m1.y = now_positon[0]
        m1.x = now_positon[1]
        up(m1, map)
    if(map[now_positon[0]+1][now_positon[1]] == '*'):
        m1.y = now_positon[0]
        m1.x = now_positon[1]
        down(m1, map)
    if(map[now_positon[0]][now_positon[1]-1] == '*'):
        m1.y = now_positon[0]
        m1.x = now_positon[1]
        left(m1, map)
    if(map[now_positon[0]][now_positon[1]+1] == '*'):
        m1.y = now_positon[0]
        m1.x = now_positon[1]
        riXht(m1, map)
# 找到X為結束
def check_X(m1, map):
    if(map[m1.y][m1.x+1] == 'X' or map[m1.y][m1.x-1] == 'X' or map[m1.y+1][m1.x] == 'X' or map[m1.y-1][m1.x] == 'X'):
        print("GET!!!!!!")
        exit()
# 畫圖
def draw_map(map):
    for i in range(0, len(map)):
        for j in range(0, len(map[0])):
            print(map[i][j], end='')
        print()
    print("=========================")
# 地圖

map = [['O','O','O','O','O','O','O','O','O'],
       ['O','*','O','*','O','*','O','O','O'],
       ['O','*','O','*','*','O','*','O','O'],
       ['O','*','O','*','*','*','*','O','O'],
       ['O','*','*','*','*','O','*','X','O'],
       ['O','*','O','O','*','O','*','O','O'],
       ['O','*','*','*','O','*','*','*','O'],
       ['O','O','O','O','O','O','O','O','O']]
# 老鼠起始位置
m1 = mouse(1, 1)
# 老鼠走過為x
map[m1.y][m1.x] = 'm'

walk(m1, map)
