from collections import Counter
cups,sakecups,X = map(int,input().split())
A = list(map(int,input().split()))

sortedA = sorted(A,reverse=True)

index = 0
ans = 0
ans += (cups-sakecups)


drink = 0
while(1):
    if(len(sortedA) == (ans + index)):
        break
    
    drink += sortedA[ans + index]
    index += 1

    if(drink >= X):
        print(ans + index)
        exit()
        
print("-1")