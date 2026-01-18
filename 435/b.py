N = int(input())
A = list(map(int,input().split()))
ans = 0
for l in range(N):
    for r in range(l,N):
        S = sum(A[l:r+1])
        flag = True
        for a in A[l:r+1]:
            if(S % a == 0):
                flag = False
                break
            else:
                pass
        if(flag):
            ans +=1

print(ans)
