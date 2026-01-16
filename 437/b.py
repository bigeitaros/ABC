height,width,n = map(int,input().split())
number = []
for i in range(height):
    number.append(list(map(int,input().split())))
    

search_n = []
for i in range(n):
    search_n.append(int(input()))
count = [0 for i in range(height)]

for i in range(height):
    for j in search_n:
        if(j in number[i]):
            count[i] += 1
            
print(max(count))