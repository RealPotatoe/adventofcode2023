import re
from typing import Dict, List, Tuple


class Node:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.neighbors = []

    def __repr__(self):
        return f"Node({self.value}, {self.x}, {self.y})"


def create_graph(map_data: List[str]) -> Tuple[Dict[Tuple[int, int], Node], Node]:
    rows = len(map_data)
    cols = len(map_data[0])
    graph = {}
    start = None

    for i in range(rows):
        for j in range(cols):
            value = map_data[i][j]
            if value != ".":
                node = Node(j, i, value)
                graph[(j, i)] = node
                if value == "S":
                    start = node

    directions = {
        "|": [(0, 1), (0, -1)],
        "-": [(1, 0), (-1, 0)],
        "L": [(1, 0), (0, -1)],
        "J": [(-1, 0), (0, -1)],
        "7": [(-1, 0), (0, 1)],
        "F": [(1, 0), (0, 1)],
        "S": [(1, 0), (0, 1), (-1, 0), (0, -1)],
    }

    for node_pos, node in graph.items():
        x, y = node_pos
        value = node.value
        if value in directions:
            for dx, dy in directions[value]:
                new_x, new_y = x + dx, y + dy
                if (
                    0 <= new_x <= rows
                    and 0 <= new_y <= cols
                    and map_data[new_y][new_x] != "."
                ):
                    node.neighbors.append(graph[(new_x, new_y)])

    for node_pos, node in graph.items():
        nodes_to_remove = []
        for neighbor in node.neighbors:
            if not node in neighbor.neighbors:
                nodes_to_remove.append(neighbor)
        node.neighbors = [
            neighbor for neighbor in node.neighbors if neighbor not in nodes_to_remove
        ]

    return graph, start


def find_furthest_node(start_node: Node):
    visited = set()
    queue = [(start_node, 0)]
    max_steps = 0

    while queue:
        node, steps = queue.pop(0)
        if node in visited:
            continue
        visited.add(node)
        max_steps = max(max_steps, steps)
        for neighbor in node.neighbors:
            queue.append((neighbor, steps + 1))

    return max_steps


def main():
    with open("day10/test_input.txt") as f:
        input_data = f.read().splitlines()

    graph, start_node = create_graph(input_data)

    # print("Graph:")
    # for node in graph.values():
    #     print(f"{node} -> {node.neighbors}")
    # print("Start node:", start_node)

    max_steps = find_furthest_node(start_node)
    print("Part one:", max_steps)

    # Part two: Get number of tiles that are enclosed by the loop. (The path of start_node is guaranteed to be a loop.)

    my_map: List[List[str]] = [
        ["."] * (len(input_data[0]) + 2) for _ in range(len(input_data) + 2)
    ]

    visited = set()
    queue = [start_node]
    while queue:
        node = queue.pop(0)
        if node in visited:
            continue
        visited.add(node)
        my_map[node.y + 1][node.x + 1] = node.value
        for neighbor in node.neighbors:
            queue.append(neighbor)

    for row in my_map:
        print("".join(row))

    tiles_enclosed = 0
    tiles_outside = 0

    for y, row in enumerate(my_map):
        inside = False
        last_tiles = ""
        for x, tile in enumerate(row):
            if tile == ".":
                last_tiles = ""
                if inside:
                    tiles_enclosed += 1
                    # print(f"({x}, {y})")
                else:
                    tiles_outside += 1
            else:
                last_tiles += tile

                if re.match(r".*[SFL].*[S7J].*", last_tiles):
                    # print(f"({x}, {y})")
                    pass
                elif re.match(r".*[SFL].*", last_tiles):
                    inside = not inside

    print("Part two:", tiles_enclosed)


if __name__ == "__main__":
    main()
