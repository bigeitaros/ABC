S_len,T_len = map(int,input().split())
S = input()
T = input()

def howmanychange(st,subst):
    subst_len = len(subst)
    ret = 0
    for i in range(subst_len):
        if(subst[i] > st[i]):
            if(st[i] == '0'):
                ret += 10 - int(subst[i])
            else:
                ret += (10 - int(subst[i]) + int(st[i]))
        else:
            ret += int(st[i]) - int(subst[i])
    
    return ret
    
ans = 100000
for i in range(S_len - T_len +1):
    ans = min(ans,howmanychange(S[i:i+T_len],T))
    
print(ans)