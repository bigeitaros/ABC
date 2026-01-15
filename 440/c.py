import sys

def solve():
    input = sys.stdin.readline
    T = int(input().strip())

    results = []
    for _ in range(T):
        N, W = map(int, input().split())
        C = list(map(int, input().split()))

        period = 2 * W
        cost = [0] * period

        # 2W ごとにまとめる
        for i in range(N):
            cost[i % period] += C[i]

        # 円環対策で2倍
        cost *= 2

        # prefix sum
        P = [0] * (len(cost) + 1)
        for i in range(len(cost)):
            P[i + 1] = P[i] + cost[i]

        # 連続 W 個の最小和
        ans = min(P[i + W] - P[i] for i in range(period))
        results.append(str(ans))

    # 出力はこれだけ
    print("\n".join(results))


if __name__ == "__main__":
    solve()
