N = int(input("in_1: "))
N1 = N
k = 0
while N > 0 :
    s1 = input(f'in_{N1-N+2}: ').split()
    if s1[-1] == 'True':
        k +=1
    N = N - 1
print("out:", k, N1-k)
