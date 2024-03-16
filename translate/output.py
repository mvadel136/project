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

current_round = 0
while current_round < rounds:
    grid_جديدة = [[0 for _ in range(8)] for _ in range(8)]
    for س in range(8):
        for ص in range(8):
            living_neighbors = 0

            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = س + dx, ص + dy
                    if 0 <= nx < 8 and 0 <= ny < 8 and grid[nx][ny] == 1:
                        living_neighbors += 1

            if grid[س][ص] == 1 and (living_neighbors == 2 or living_neighbors == 3):
                grid_جديدة[س][ص] = 1
            elif grid[س][ص] == 0 and living_neighbors == 3:
                grid_جديدة[س][ص] = 1

    grid = grid_جديدة
    current_round += 1

    print(f'Round {round}:')
    for صف in grid:
        for خلية in صف:
            if خلية == 1:
                print('◼', end=' ')
            else:
                print('◻', end=' ')
        print()
    print()