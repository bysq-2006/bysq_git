import random
randint = random.randint(1,100)
i = 5
while i:
    i-=1
    num = eval(input())
    if num == randint:
        print("等于")
    elif num > randint:
        print("大了")
    else:
        print("小了")