t_len,a_len = map(int,input().split())
T = input()
A = input()
query = int(input())

for i in range(query):
    st = input()
    t_flag = True
    a_flag = True
    for j in range(len(st)):
        if(st[j] in T and t_flag != False):
            pass
        else:
            t_flag = False

        if(st[j] in A and a_flag != False):
            pass
        else:
            a_flag = False
        
    if(t_flag == True and a_flag == True):
        print("Unknown")
    elif(t_flag == True):
        print("Takahashi")
    elif(a_flag == True):
        print("Aoki")
    else:
        print("Unknown")
        
            