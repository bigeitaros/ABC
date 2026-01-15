st = input()
stl = len(st)


def happy(st):
    st = str(st)
    st_len = len(st)
    ret = 0
    for i in range(st_len):
        ret += int(st[i]) ** 2
    return ret

ret = st
for i in range(1000):
    ret = happy(ret)

if(ret == 1):
    print("Yes")
else:
    print("No")