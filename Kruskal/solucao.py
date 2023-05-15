""" Usando Kruskal """
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


""" Usando Prim """

# import heapq

# class Edge:
#     def __init__(self, a, b, cost):
#         self.a = a
#         self.b = b
#         self.cost = cost

#     def __lt__(self, other):
#         return self.cost < other.cost

# def prim(edges, m):
#     total_cost = 0
#     visited = [False] * m
#     min_heap = []
    
#     start_node = 0  # Escolha o nó inicial arbitrariamente
    
#     visited[start_node] = True
    
#     for edge in edges[start_node]:
#         heapq.heappush(min_heap, edge)
    
#     while min_heap:
#         edge = heapq.heappop(min_heap)
#         if visited[edge.b]:
#             continue
        
#         visited[edge.b] = True
#         total_cost += edge.cost
        
#         for next_edge in edges[edge.b]:
#             if not visited[next_edge.b]:
#                 heapq.heappush(min_heap, next_edge)
    
#     return total_cost

# def solve():
#     while True:
#         m, n = map(int, input().split())
#         if m == 0 and n == 0:
#             break
        
#         edges = [[] for _ in range(m)]
        
#         for _ in range(n):
#             a, b, cost = map(int, input().split())
#             edges[a].append(Edge(a, b, cost))
#             edges[b].append(Edge(b, a, cost))
        
#         saved_cost = sum(edge.cost for edge_list in edges for edge in edge_list) // 2 - prim(edges, m)
#         print(f'\n{saved_cost}')

# def main():
#     solve()

# if __name__ == '__main__':
#     main()
