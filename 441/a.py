P,Q = map(int,input().split())
X,Y = map(int,input().split())

if(P + 100 > X and Q + 100 > Y and P <= X and Q <= Y):
    print("Yes")
else:
    print("No")