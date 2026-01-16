#first,all reindeer pull sleigh
#power is sum of power
#if one of reindeer transfer to sleigh,
#lose power of one of reindeer, and get weight of one of reindeer.
#so,consider diffrence of sum of power and after transfer power and weight,
#correct direction is donyoku(ascending). like this below.

def solve():
    n = int(input())
    wp = [list(map(int, input().split())) for i in range(n)]
    wp.sort(key=lambda x: x[0] + x[1]) # w_i + p_i でソート
    sum_p = 0
    for w, p in wp:
        sum_p += p
    res = 0
    for i in range(n):
        w, p = wp[i]
        res += w + p
        if sum_p < res:
            print(i)
            return


for _ in range(int(input())):
    solve()
