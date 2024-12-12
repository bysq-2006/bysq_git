nums = []
num = 16546555# int(input())


def cout(num:int):
    return "0123456789abcdef"[num]

while num > 0:
    nums.insert(0,cout(num % 16))
    num //= 16

for i in nums:
    print(i,end='')