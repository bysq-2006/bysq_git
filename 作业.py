def num_pd(number:int) -> bool:
    sum:int = 0
    for i in range(1,number,1):
        if number % i == 0:
            sum += i
    if sum == number:
        return True
    else:
        return False

num = eval(input())
print(f"{num} is {num_pd(num)}")