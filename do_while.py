sum =0
n = 99
while n>0 :
    sum = sum + n
    n = n-2
print(sum)
print('=============================================')
n=1
while n<=100:
    if n>10:
        break
    print(n)
    n= n+1
print('End')
print('=============================================')

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)