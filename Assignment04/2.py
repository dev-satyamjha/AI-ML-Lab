import heapq


def greedy_bfs():
    h = {"A": 2, "B": 2, "C": 1, "G": 0, "D": 3, "E": 2, "F": 1, "H": 3}
    lv = {"A": 0, "B": 1, "C": 1, "G": 1, "D": 2, "E": 2, "F": 2, "H": 3}
    graph = {
        "A": ["B", "C"],
        "B": ["A", "C", "D", "E"],
        "C": ["A", "B", "E", "F"],
        "D": ["B", "E", "H"],
        "E": ["B", "C", "D", "F", "H"],
        "F": ["C", "E", "H", "G"],
        "G": [],
        "H": ["D", "E", "F"],
    }

    q, explored = [(h["A"], "A", ["A"])], []
    visited = {"A"}

    while q:
        h_val, curr, path = heapq.heappop(q)
        explored.append(curr)

        if curr == "G":
            total_cost = 0
            for i in range(len(path) - 1):
                c, n = path[i], path[i + 1]
                total_cost += 1 if lv[n] > lv[c] else (2 if lv[n] == lv[c] else 3)

            print(f"1. Search Tree Trace: {explored}")
            print(f"2. Final Path Found: {' -> '.join(path)}")
            print(f"3. Total Cost of Path: {total_cost}")
            return

        for nxt in graph[curr]:
            if nxt not in visited:
                visited.add(nxt)
                heapq.heappush(q, (h[nxt], nxt, path + [nxt]))


if __name__ == "__main__":
    greedy_bfs()