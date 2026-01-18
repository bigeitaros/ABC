X,Y,Z = map(int,input().split())

for i in range(1000):
    if(X == Y*Z):
        print("Yes")
        exit()
    X += 1
    Y += 1

    
print("No")