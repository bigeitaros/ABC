#kuso deka list tukurudakedemo osoikara,hoka no data structure wo tukau koto
# wo kangaeru,set toka, queue toka
import sys

# 高速化のため sys.stdin.readline を使用
input = sys.stdin.readline

N, M = map(int, input().split())

# 2次元配列の代わりに set を使う
# ここには "値が1である座標のタプル (r, c)" だけを保存する
occupied = set()

ans = 0

for _ in range(M):
    R, C = map(int, input().split())
    R -= 1
    C -= 1
    
    # チェック対象の4マス
    # タプル (r, c) にしないと set に入れられないため注意
    target_cells = [
        (R, C), (R + 1, C), (R, C + 1), (R + 1, C + 1)
    ]
    
    can_place = True
    
    for r, c in target_cells:
        # 1. 配列外参照のチェック (N x N の外側には置けない場合)
        if not (0 <= r < N and 0 <= c < N):
            can_place = False
            break
        
        # 2. すでに塗られているかチェック (setに入っているか)
        if (r, c) in occupied:
            can_place = False
            break
    
    # 4マスとも空いていて、範囲内なら塗る
    if can_place:
        ans += 1
        for cell in target_cells:
            occupied.add(cell)

print(ans)