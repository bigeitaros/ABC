N = int(input())
A = list(map(int,input().split()))
index = 0
life = A[0]
for i in range(N):
    if(life < A[i]):
        life = A[i]
    if(life == 1):
        print(i+1)
        exit()
    life -= 1

print(N)