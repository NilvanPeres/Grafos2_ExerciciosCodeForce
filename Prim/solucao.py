import heapq
import math

def log2(x):
    return math.floor(math.log2(x))

def solve(n, m, roads):
    graph = [[] for _ in range(n + 1)]
    for a, b, c in roads:
        graph[a].append((b, c))
        graph[b].append((a, c))

    visited = [False] * (n + 1)
    min_cost = 0

    pq = [(0, 1)] 
    while pq:
        cost, vertex = heapq.heappop(pq)
        if visited[vertex]:
            continue
        visited[vertex] = True
        min_cost += cost
        for neighbor, neighbor_cost in graph[vertex]:
            if not visited[neighbor]:
                heapq.heappush(pq, (neighbor_cost, neighbor))

    return min_cost + 1

def main():
    T = int(input())
    results = []
    for _ in range(T):
        n, m = map(int, input().split())
        roads = []
        for _ in range(m):
            a, b, c = map(int, input().split())
            roads.append((a, b, log2(c)))
        result = solve(n, m, roads)
        results.append(result)

    for result in results:
        print(result)

if __name__ == "__main__":
  main()

# class Subset:
#     def __init__(self, parent, rank):
#         self.parent = parent
#         self.rank = rank

# class Edge:
#     def __init__(self, a, b, cost):
#         self.a = a
#         self.b = b
#         self.cost = cost

# def log2(x):
#     return math.floor(math.log2(x))

# def find(subsets, e):
#     if subsets[e].parent != e:
#         subsets[e].parent = find(subsets, subsets[e].parent)
#     return subsets[e].parent

# def union(subsets, x, y):
#     rx = find(subsets, x)
#     ry = find(subsets, y)
#     if subsets[rx].rank < subsets[ry].rank:
#         subsets[rx].parent = ry
#     elif subsets[ry].rank < subsets[rx].rank:
#         subsets[ry].parent = rx
#     else:
#         subsets[ry].parent = rx
#         subsets[rx].rank += 1

# def solve(n, m, roads):
#     subsets = [Subset(i, 0) for i in range(n + 1)]
#     edges = [Edge(a, b, log2(c)) for a, b, c in roads]
#     edges.sort(key=lambda x: x.cost)

#     min_cost = 0
#     heap = []
#     heapq.heapify(heap)
#     for i in range(m):
#         heapq.heappush(heap, (edges[i].cost, edges[i].a, edges[i].b))

#     while heap:
#         cost, a, b = heapq.heappop(heap)
#         x = find(subsets, a)
#         y = find(subsets, b)
#         if x != y:
#             min_cost += cost
#             union(subsets, x, y)

#     return min_cost + 1

# def main():
#     T = int(input())
#     results = []
#     for _ in range(T):
#         n, m = map(int, input().split())
#         roads = []
#         for _ in range(m):
#             a, b, c = map(int, input().split())
#             roads.append((a, b, c))
#         result = solve(n, m, roads)
#         results.append(result)

#     for result in results:
#         print(result)

# if __name__ == "__main__":
#   main()



    
