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



    
