import sys

# データ量が多い場合の入力高速化
input = sys.stdin.readline

def solve():
    try:
        line1 = input().split()
        if not line1: return # 入力が空の場合の対策
        N = int(line1[0])
        H = int(line1[1])
        
        # 配列として全部読み込む（C++のコードに近い形）
        # 行ごとに処理しても良いですが、C++のロジックを忠実に再現します
        T = [0] * N
        L = [0] * N
        U = [0] * N
        
        for i in range(N):
            T[i], L[i], U[i] = map(int, input().split())

        t_prev = 0
        l = H
        u = H

        for i in range(N):
            d = T[i] - t_prev
            
            # 時間 d だけ移動できるので、到達可能範囲が広がる
            l -= d
            u += d
            
            t_prev = T[i]

            # 今回の許容範囲 [L[i], U[i]] との共通部分を取る
            l = max(l, L[i])
            u = min(u, U[i])

            # 範囲が矛盾したら到達不可能
            if l > u:
                print("No")
                return

        print("Yes")
    except ValueError:
        return

def main():
    line = input()
    if not line: return
    T_cases = int(line)
    for _ in range(T_cases):
        solve()

if __name__ == "__main__":
    main()

