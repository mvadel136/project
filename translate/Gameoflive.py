grid = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 1, 0]
]
rounds = 3

round = 0
while round < rounds:
    new_grid = [[0 for _ in range(8)] for _ in range(8)]
    for x in range(8):
        for y in range(8):
            live_neighbors = 0
            
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 8 and 0 <= ny < 8 and grid[nx][ny] == 1:
                        live_neighbors += 1
            
            if grid[x][y] == 1 and (live_neighbors == 2 or live_neighbors == 3):
                new_grid[x][y] = 1
            elif grid[x][y] == 0 and live_neighbors == 3:
                new_grid[x][y] = 1

    grid = new_grid
    round += 1
    
    print(f'Round {round}:')
    for row in grid:
        for cell in row:
            if cell == 1:
                print('◼', end=' ')
            else:
                print('◻', end=' ')
        print()
    print()
