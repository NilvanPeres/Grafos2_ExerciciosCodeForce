import heapq

INFINITY = float('inf')

def dijkstra(graph, src, dest):
    n = len(graph)
    distances = [INFINITY] * n
    visited = [False] * n
    heap = []
    
    distances[src] = 0
    heapq.heappush(heap, (0, src))
    
    while heap:
        cost, node = heapq.heappop(heap)
        
        if visited[node]:
            continue
        visited[node] = True
        
        for neighbor, edge_cost in graph[node]:
            if edge_cost + cost < distances[neighbor]:
                distances[neighbor] = edge_cost + cost
                heapq.heappush(heap, (edge_cost + cost, neighbor))
    
    return distances[dest]

def main():
    t = int(input())

    for _ in range(t):
        n, m = map(int, input().split())
        
        graph = [[] for _ in range(n)]
        
        for _ in range(m):
            v, u, c = map(int, input().split())
            v -= 1
            u -= 1
            graph[v].append((u, c))
        
        src, dest = map(int, input().split())
        src -= 1
        dest -= 1
        
        shortest_distance = dijkstra(graph, src, dest)
        
        if shortest_distance == INFINITY:
            print("NO")
        else:
            print(shortest_distance)

if __name__ == "__main__":
    main()
