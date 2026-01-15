import sys

# 高速入力
input = sys.stdin.readline

N = int(input())
# puyo = list(map(int,input().split())) # メモリ節約のためイテレータでも可

# スタックを用意 (値, 連続回数) のペアを保存すると楽です
# しかし、単純なリストでも十分解けます
stack = [] 

for x in map(int, input().split()):
    stack.append(x)
    
    # 末尾をチェックして条件を満たすなら削除
    # 例: 同じものが2つ続いたら削除の場合
    # ABC 438 C は "2つ" で消える問題のはずなので注意！
    # コードに合わせて "4つ" で書くならこうなります
    if len(stack) >= 4:
        if stack[-1] == stack[-2] == stack[-3] == stack[-4]:
           for _ in range(4):
               stack.pop()

print(len(stack))