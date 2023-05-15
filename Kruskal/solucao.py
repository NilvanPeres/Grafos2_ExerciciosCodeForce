class Edge:
    def __init__(self, a, b, cost):
        self.a = a
        self.b = b
        self.cost = cost

def comp(e1, e2):
    return e1.cost < e2.cost

class Subset:
    def __init__(self, parent, rank):
        self.parent = parent
        self.rank = rank

def find(i, subsets):
    if subsets[i].parent != i:
        subsets[i].parent = find(subsets[i].parent, subsets)
    return subsets[i].parent

def union(x, y, subsets):
    xroot = find(x, subsets)
    yroot = find(y, subsets)

    if subsets[xroot].rank < subsets[yroot].rank:
        subsets[xroot].parent = yroot
    elif subsets[xroot].rank > subsets[yroot].rank:
        subsets[yroot].parent = xroot
    else:
        subsets[yroot].parent = xroot
        subsets[xroot].rank += 1

def kruskal(edges, m):
    total_cost = 0
    e = 0

    subsets = [Subset(i, 0) for i in range(m)]
    edges.sort(key=lambda x: x.cost)

    for edge in edges:
        x = find(edge.a, subsets)
        y = find(edge.b, subsets)
        if x != y:
            e += 1
            total_cost += edge.cost
            union(x, y, subsets)
        
        if e == m - 1:
            break

    return total_cost

def solve():
    while True:
        m, n = map(int, input().split())
        if m == 0 and n == 0:
            break
        
        edges = []
        for _ in range(n):
            a, b, cost = map(int, input().split())
            edges.append(Edge(a, b, cost))
        
        saved_cost = sum(edge.cost for edge in edges) - kruskal(edges, m)
        print(f'\n{saved_cost}')

def main():
    solve()

if __name__ == '__main__':
    main()
