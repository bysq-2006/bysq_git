num:int = int(input())
i:int = 0

while num > 0:
    num //= 10
    i += 1

print(i)