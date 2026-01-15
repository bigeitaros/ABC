N = int(input())
lis = list(map(int,input().split()))

sorted_lis = sorted(lis)

for k, i in enumerate(sorted_lis[:3]):
    for j in range(N):
        if(i == lis[j]):
            if k == 2:
                print(j+1)
            else:
                print(j+1, end=" ")
            break
