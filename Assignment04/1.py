import heapq


def a_star():
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

    q, explored = [(h["A"], "A", ["A"], 0)], []
    visited_g = {"A": 0}

    while q:
        f, curr, path, g = heapq.heappop(q)
        explored.append(curr)

        if curr == "G":
            print(f"1. Search Tree Trace: {explored}")
            print(f"2. Best Path Found: {' -> '.join(path)}")
            print(f"3. Total Cost: {g}")
            return

        for nxt in graph[curr]:
            cost = 1 if lv[nxt] > lv[curr] else (2 if lv[nxt] == lv[curr] else 3)
            new_g = g + cost

            if new_g < visited_g.get(nxt, float("inf")):
                visited_g[nxt] = new_g
                heapq.heappush(q, (new_g + h[nxt], nxt, path + [nxt], new_g))


if __name__ == "__main__":
    a_star()