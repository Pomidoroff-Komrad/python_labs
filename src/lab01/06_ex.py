N = int(input("Кол-во участников: "))
N1 = N
k = 0
while N > 0 :
    s1 = input().split()
    if s1[-1] == 'True':
        k +=1
    N = N - 1
print(k, N1-k)
