# Assignment 4: Drone Flight Navigation with A* (Navigasi Drone dengan A*)
def drone_a_star(grid, start, goal):
    from queue import PriorityQueue
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    pq = PriorityQueue()
    pq.put((0, 0, start, [start]))
    visited = set()

    def heuristic(a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])

    while not pq.empty():
        f, g, current, path = pq.get()
        if current == goal:
            return path

        if current in visited:
            continue

        visited.add(current)
        for dx, dy in directions:
            nx, ny = current[0]+dx, current[1]+dy
            if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny] != '#':
                elevation = int(grid[nx][ny]) if grid[nx][ny].isdigit() else 1
                new_g = g + elevation
                new_f = new_g + heuristic((nx, ny), goal)
                pq.put((new_f, new_g, (nx, ny), path + [(nx, ny)]))
    return None

# Contoh peta drone
terrain = [
    ['S', '1', '2', '3', 'G'],
    ['1', '#', '2', '#', '2'],
    ['2', '3', '4', '1', '1']
]

start = (0, 0)
goal = (0, 4)
print("Drone A* Path:", drone_a_star(terrain, start, goal))
