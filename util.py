def bfs_maze_solver(start, end_node, maze_array):
    queue = [(start, [])]
    visited = set()
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    while queue:
        current_node, current_path = queue.pop(0)

        if current_node == end_node:
            return current_path + [end_node]

        for dir in directions:
            neighbor_node = (current_node[0] + dir[0], current_node[1] + dir[1])

            if (0 <= neighbor_node[0] < len(maze_array)) and (0 <= neighbor_node[1] < len(maze_array[0])):
                if neighbor_node not in visited and maze_array[neighbor_node[0]][neighbor_node[1]] not in ["snake", "head of snake"]:
                    visited.add(neighbor_node)
                    queue.append((neighbor_node, current_path + [current_node]))

def pixel_to_grid(x, y):
    return x // 32, y // 32