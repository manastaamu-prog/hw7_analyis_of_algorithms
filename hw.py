import heapq
from math import inf



graph = {
    1: [(2,1),(11,1)],
    2: [(1,1),(3,1),(12,1)],
    3: [(2,1),(4,1)],
    4: [(3,1),(5,1),(10,1)],
    5: [(4,1),(6,1),(21,2),(22,2)],
    6: [(5,1),(8,1)],
    7: [(8,1),(9,1),(17,1)],
    8: [(6,1),(7,1),(9,1)],
    9: [(7,1),(8,1),(10,1)],
    10: [(4,1),(9,1),(11,1),(18,1)],
    11: [(1,1),(10,1),(12,1)],
    12: [(2,1),(11,1),(13,1)],
    13: [(12,1),(14,1),(21,1)],
    14: [(13,1),(15,1),(16,1)],
    15: [(14,1),(16,1),(20,1)],
    16: [(14,1),(15,1),(17,1)],
    17: [(7,1),(16,1),(18,1)],
    18: [(10,1),(17,1),(19,1)],
    19: [(18,1)],
    20: [(15,1),(21,1)],
    21: [(5,2),(13,1),(20,1),(22,1)],
    22: [(5,2),(21,1)],
}

START = 1
SUSPECTS = [6, 8, 9, 15, 16, 22]

def initialize_single_source(V,s):
    d = {v: inf for v in V}
    p = {v: None for v in V}
    d[s] = 0
    return d, p

def relax(u,v,w,d,p):
    if d[v] > d[u] + w:
        d[v] = d[u] + w
        p[v] = u
        return True
    return False


def dijkstra(graph, start, suspects):
    V = list(graph.keys())
    d, p = initialize_single_source(V, start)
    pq = [(0, start)]
    visited = set()
    
    while pq:
        du, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        
        for v, w in graph[u]:
            if relax(u, v, w, d, p):
                heapq.heappush(pq, (d[v], v))
    
 
    suspect_distances = {s: d[s] for s in suspects}
    return suspect_distances



def main():
    d = dijkstra(graph, START, SUSPECTS)
    print(d)

if __name__ == "__main__":
    main()

