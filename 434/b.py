N,M = map(int,input().split())
weight = [0] * M
birds = [0] * M

for i in range(N):
    A,B = map(int,input().split())
    weight[A-1] += B
    birds[A-1] += 1
    

for i in range(M):
    print(weight[i] / birds[i])