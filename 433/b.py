N = int(input())
A = list(map(int,input().split()))

for i in range(N):
    h = A[i]
    pos = -1
    for j in range(0,i):
        if(h < A[j]):
            pos = j+1
    print(pos)    