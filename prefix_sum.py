import numpy as np
import timeit

# データの準備
a = np.arange(1, 10001)
b = np.arange(100,1001)
print(a)
# 累積和の構築
prefix = [0] * (len(a) + 1)
for i in range(len(a)):
    prefix[i+1] = prefix[i] + a[i]

# 計測用の関数定義
def use_sum():
    return sum(b)

def use_prefix():
    return prefix[1000] - prefix[99] #prefix[0] is 0,prefix[10000] is sum of a[0] to a[10000]
                                     #then,if you calcurate sum of 100 to 1000, ans is shown by prefix[1000]-prefix[99]

# 検証：結果が同じか確認
print(f"sum(b): {use_sum()}")
print(f"prefix diff: {use_prefix()}")
assert use_sum() == use_prefix()

# 計測 (1000回実施)
n_loops = 10 ** 3
time_sum = timeit.timeit(use_sum, number=n_loops)
time_prefix = timeit.timeit(use_prefix, number=n_loops)

# 結果出力
print(f"\n--- {n_loops} loops ---")
print(f"sum(b) time:        {time_sum:.6f} sec")
print(f"prefix lookup time: {time_prefix:.6f} sec")
print(f"Speedup:            {time_sum / time_prefix:.2f}x faster")