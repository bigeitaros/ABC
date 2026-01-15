import math
N = int(input())

ansli = []
for i in range(1,N+1):
    print(i,"times")
    ifmul = []
    for j in range(1,3163):
        target = i - j**2
        if(target <= 0):
            break
        if(math.sqrt(target).is_integer() == True and int(math.sqrt(target)) < j):
            print(j,"append")
            ifmul.append(i)
            print(i)
        else:
            pass
    print(ifmul)
    if(len(ifmul) == 1):
        ansli.append(ifmul[0])
        
print(ansli)


if(len(ansli) == 0):
    print("0")
else:
    for index,element in enumerate(ansli):
        if(index != len(ansli)):
            print(element,end=" ")
        else:
            print(element)

            
            
ans


import math

# 入力
N = int(input())

# 1. カウント用の配列を用意 (indexが数値、valueが出現回数)
# N以下の数字が「何通りの平方数の和で表せるか」を数える
memo = [0] * (N + 1)

# 2. x^2 + y^2 を計算して埋めていく
# x を 1 から回す (x^2 が N を超えたら終了)
x = 1
while x * x < N:
    y = 1
    # y は x より小さい範囲で回す (条件: x > y >= 1)
    # これにより重複や0を含まないユニークな組み合わせだけ見れる
    while y < x:
        val = x * x + y * y
        if val <= N:
            memo[val] += 1
        else:
            # これ以上 y を増やしても N を超えるだけなので break
            break
        y += 1
    x += 1

# 3. ちょうど1通り (len(ifmul) == 1 だったもの) を探す
ansli = []
for i in range(1, N + 1):
    if memo[i] == 1:
        ansli.append(i)

# 4. 出力
if len(ansli) == 0:
    print(0)
else:
    # 最後の空白対策 (*リスト で展開してsep=" "を使うと楽です)
    print(*ansli)