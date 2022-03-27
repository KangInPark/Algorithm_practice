import sys


def func(ileft, iright, pleft, pright):
    parent = Post[pright]
    print(parent, "", end="")
    idx = dic[parent]
    lsize = idx - ileft
    rsize = iright - idx
    if lsize > 0:
        func(ileft, idx - 1, pleft, pleft + lsize - 1)
    if rsize > 0:
        func(idx + 1, iright, pright - rsize, pright - 1)


sys.setrecursionlimit(10**6)
n = int(input())
In = list(map(int, input().split(" ")))
Post = list(map(int, input().split(" ")))
dic = {}
for idx in range(n):
    dic[In[idx]] = idx
func(0, n - 1, 0, n - 1)
