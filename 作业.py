import random
randint = random.randint(1,100)
for i in range(0,5,1):
    num = eval(input())
    if num == randint:
        print("等于")
    elif num > randint:
        print("大了")
    else:
        print("小了")