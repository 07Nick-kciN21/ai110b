## 老鼠走迷宮
使用遞迴每當遇到岔路時，便會分頭向下搜尋，直到盡頭或找到終點  
O為牆壁，*為道路，m為老鼠足跡  
[程式碼](mouse.py)由本人完全原創  
```
map = [['O','O','O','O','O','O','O','O','O'],
       ['O','*','O','*','O','*','O','O','O'],
       ['O','*','O','*','*','O','*','O','O'],
       ['O','*','O','*','*','*','*','O','O'],
       ['O','*','*','*','*','O','*','X','O'],
       ['O','*','O','O','*','O','*','O','O'],
       ['O','*','*','*','O','*','*','*','O'],
       ['O','O','O','O','O','O','O','O','O']]  
```
```
PS C:\Users\maybu\Desktop\cccrouse\ai110b\HomeWork\mouse_map> python .\mouse.py
1 1
OOOOOOOOO
OmO*O*OOO
O*O**O*OO
O*O****OO
O****O*XO
O*OO*O*OO
O***O***O
OOOOOOOOO
=========================
1 2
OOOOOOOOO
OmO*O*OOO
OmO**O*OO
O*O****OO
O****O*XO
O*OO*O*OO
O***O***O
OOOOOOOOO
=========================
1 3
OOOOOOOOO
OmO*O*OOO
OmO**O*OO
OmO****OO
O****O*XO
O*OO*O*OO
O***O***O
OOOOOOOOO
=========================
1 4
OOOOOOOOO
OmO*O*OOO
OmO**O*OO
OmO****OO
Om***O*XO
O*OO*O*OO
O***O***O
OOOOOOOOO
=========================
1 5
OOOOOOOOO
OmO*O*OOO
OmO**O*OO
OmO****OO
Om***O*XO
OmOO*O*OO
O***O***O
OOOOOOOOO
=========================
1 6
OOOOOOOOO
OmO*O*OOO
OmO**O*OO
OmO****OO
Om***O*XO
OmOO*O*OO
Om**O***O
OOOOOOOOO
=========================
2 6
OOOOOOOOO
OmO*O*OOO
OmO**O*OO
OmO****OO
Om***O*XO
OmOO*O*OO
Omm*O***O
OOOOOOOOO
=========================
3 6
OOOOOOOOO
OmO*O*OOO
OmO**O*OO
OmO****OO
Om***O*XO
OmOO*O*OO
OmmmO***O
OOOOOOOOO
=========================
2 4
OOOOOOOOO
OmO*O*OOO
OmO**O*OO
OmO****OO
Omm**O*XO
OmOO*O*OO
OmmmO***O
OOOOOOOOO
=========================
3 4
OOOOOOOOO
OmO*O*OOO
OmO**O*OO
OmO****OO
Ommm*O*XO
OmOO*O*OO
OmmmO***O
OOOOOOOOO
=========================
3 3
OOOOOOOOO
OmO*O*OOO
OmO**O*OO
OmOm***OO
Ommm*O*XO
OmOO*O*OO
OmmmO***O
OOOOOOOOO
=========================
3 2
OOOOOOOOO
OmO*O*OOO
OmOm*O*OO
OmOm***OO
Ommm*O*XO
OmOO*O*OO
OmmmO***O
OOOOOOOOO
=========================
3 1
OOOOOOOOO
OmOmO*OOO
OmOm*O*OO
OmOm***OO
Ommm*O*XO
OmOO*O*OO
OmmmO***O
OOOOOOOOO
=========================
4 2
OOOOOOOOO
OmOmO*OOO
OmOmmO*OO
OmOm***OO
Ommm*O*XO
OmOO*O*OO
OmmmO***O
OOOOOOOOO
=========================
4 3
OOOOOOOOO
OmOmO*OOO
OmOmmO*OO
OmOmm**OO
Ommm*O*XO
OmOO*O*OO
OmmmO***O
OOOOOOOOO
=========================
4 4
OOOOOOOOO
OmOmO*OOO
OmOmmO*OO
OmOmm**OO
OmmmmO*XO
OmOO*O*OO
OmmmO***O
OOOOOOOOO
=========================
4 5
OOOOOOOOO
OmOmO*OOO
OmOmmO*OO
OmOmm**OO
OmmmmO*XO
OmOOmO*OO
OmmmO***O
OOOOOOOOO
=========================
5 3
OOOOOOOOO
OmOmO*OOO
OmOmmO*OO
OmOmmm*OO
OmmmmO*XO
OmOOmO*OO
OmmmO***O
OOOOOOOOO
=========================
6 3
OOOOOOOOO
OmOmO*OOO
OmOmmO*OO
OmOmmmmOO
OmmmmO*XO
OmOOmO*OO
OmmmO***O
OOOOOOOOO
=========================
6 2
OOOOOOOOO
OmOmO*OOO
OmOmmOmOO
OmOmmmmOO
OmmmmO*XO
OmOOmO*OO
OmmmO***O
OOOOOOOOO
=========================
6 4
OOOOOOOOO
OmOmO*OOO
OmOmmOmOO
OmOmmmmOO
OmmmmOmXO
OmOOmO*OO
OmmmO***O
OOOOOOOOO
=========================
GET!!!!!!
``