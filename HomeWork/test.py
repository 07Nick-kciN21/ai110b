def x():
    a=0
    print(a)
    a += 1
    if(a > 5):
        exit()
    x()

x()