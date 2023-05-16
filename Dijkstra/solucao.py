import heapq
from typing import List, Tuple

class E:
    def __init__(self, to: int, nxt: int, w: int):
        self.to = to
        self.nxt = nxt
        self.w = w

class Node:
    def __init__(self, x: int, r: int):
        self.x = x
        self.r = r

    def __lt__(self, other: 'Node') -> bool:
        return not cmp(self.r, other.r)

class Edge:
    def __init__(self, x: int, y: int, w: int):
        self.x = x
        self.y = y
        self.w = w

N = 100005
P = N * 100
M = 200005
p = 5557
mod = 1000000007

mem = [E(0, 0, 0) for _ in range(M)]
head = [0] * M
ls = [0] * P
rs = [0] * P
rt = [0] * (N + 2)
b = [0] * (N + 31)
c = [0] * (N + 31)
vis = [0] * M
pre = [0] * M
a = [0] * N
hs = [0] * P
pw = [0] * (N + 31)
num = tot = ans = cnt = 0

def add(x: int, y: int, w: int) -> None:
    global num
    num += 1
    mem[num].to = y
    mem[num].nxt = head[x]
    mem[num].w = w
    head[x] = num

def cmp(x: int, y: int) -> bool:
    l, r = 1, bit
    while l < r:
        mid = (l + r) >> 1
        if hs[ls[x]] != hs[ls[y]]:
            x, y = ls[x], ls[y]
            r = mid
        else:
            x, y = rs[x], rs[y]
            l = mid + 1
    return hs[x] < hs[y]

def update(k: int, l: int, r: int) -> None:
    mid = (l + r) >> 1
    hs[k] = hs[ls[k]] * pw[r - mid] + hs[rs[k]]

def build(k: List[int], l: int, r: int, c: int) -> None:
    if not k:
        k.append(0)
        k.append(tot + 1)
        tot += 1
    if l == r:
        hs[k[-1]] = c
        return
    mid = (l + r) >> 1
    build(k, l, mid, c)
    build(k, mid + 1, r, c)
    k.append(0)
    ls[k[-1]] = ls[k[-2]]
    rs[k[-1]] = rs[k[-2]]
    update(k[-1], l, r)

def insert(last: int, l: int, r: int, p: int) -> int:
    now = tot + 1
    tot += 1
    if l == r:
        if hs[last]:
            hs[now] = 0
            p -= 1
        else:
            hs[now] = 1
        return now
    mid = (l + r) >> 1
    k.append(0)
    ls[now] = ls[last]
    rs[now] = rs[last]
    if p > mid:
        rs[now] = insert(rs[last], mid + 1, r, p)
    if p <= mid:
        ls[now] = insert(ls[last], l, mid, p)
    update(now, l, r)
    return now

def init() -> None:
    pw[0] = 1
    for i in range(1, bit + 1):
        pw[i] = pw[i - 1] * p

def dfs(k: int, l: int, r: int) -> None:
    if not k:
        return
    if l == r:
        c[l] = int(hs[k])
        return
    mid = (l + r) >> 1
    dfs(ls[k], l, mid)
    dfs(rs[k], mid + 1, r)

def quickpow(x: int, y: int) -> int:
    s = 1
    while y:
        if y & 1:
            s = 1ll * s * x % mod
        x = 1ll * x * x % mod
        y >>= 1
    return s

def dij() -> None:
    global tot
    q = []
    heapq.heappush(q, Node(s, rt[s]))
    while q:
        k = heapq.heappop(q)
        if vis[k.x]:
            continue
        vis[k.x] = 1
        for j in range(head[k.x]):
            u = mem[j].to
            now = insert(rt[k.x], 1, bit, mem[j].w)
            if cmp(now, rt[u]):
                rt[u] = now
                pre[u] = k.x
                heapq.heappush(q, Node(u, rt[u]))

n, m = map(int, input().split())
bit = N + 30
for i in range(bit + 1):
    b[i] = bit - i
edges = []
for _ in range(m):
    x, y, w = map(int, input().split())
    edges.append(Edge(x, y, bit - w))
    edges.append(Edge(y, x, bit - w))
s, t = map(int, input().split())
init()
build(rt[0], 1, bit, 0)
build(rt[n + 1], 1, bit, 1)
for e in edges:
    add(e.x, e.y, e.w)
dij()
if rt[t] == rt[n + 1]:
    print("-1")
else:
    dfs(rt[t], 1, bit)
    for i in range(1, bit + 1):
        ans = (ans + 1ll * quickpow(2, b[i]) * c[i] % mod) % mod
    print(ans)
    while t != s:
        cnt += 1
        a[cnt] = t
        t = pre[t]
    cnt += 1
    a[cnt] = s
    print(cnt)
    for i in range(cnt, 0, -1):
        print(a[i], end=" ")

