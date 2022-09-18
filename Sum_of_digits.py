T = int(input())
for i in range(T):
    num = int(input())
    sum = 0
    while(num != 0):
        sum = sum+num % 10
        num = num//10
    print(sum)
