'''
https://school.programmers.co.kr/learn/courses/30/lessons/159993
'''


def solution(maps):
    rows = len(maps)
    cols = len(maps[0])

    # Find starting point, lever location, and exit location
    start_row, start_col = None, None
    lever_row, lever_col = None, None
    exit_row, exit_col = None, None
    for r in range(rows):
        for c in range(cols):
            if maps[r][c] == 'S':
                start_row, start_col = r, c
            elif maps[r][c] == 'L':
                lever_row, lever_col = r, c
            elif maps[r][c] == 'E':
                exit_row, exit_col = r, c

    # Check if lever and exit are reachable
    if (lever_row is None or exit_row is None or
            not is_reachable(start_row, start_col, lever_row, lever_col, maps) or
            not is_reachable(lever_row, lever_col, exit_row, exit_col, maps)):
        return -1

    # Calculate minimum time
    time_to_lever = bfs(start_row, start_col, lever_row, lever_col, maps)
    time_to_exit = bfs(lever_row, lever_col, exit_row, exit_col, maps)
    return time_to_lever + time_to_exit


def is_reachable(start_row, start_col, target_row, target_col, maps):
    rows = len(maps)
    cols = len(maps[0])
    visited = [[False] * cols for _ in range(rows)]
    queue = [(start_row, start_col)]
    visited[start_row][start_col] = True
    while queue:
        row, col = queue.pop(0)
        if row == target_row and col == target_col:
            return True
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            r, c = row + dr, col + dc
            if (0 <= r < rows and 0 <= c < cols and not visited[r][c] and
                    maps[r][c] != 'X'):
                visited[r][c] = True
                queue.append((r, c))
    return False


def bfs(start_row, start_col, target_row, target_col, maps):
    rows = len(maps)
    cols = len(maps[0])
    visited = [[False] * cols for _ in range(rows)]
    queue = [(start_row, start_col, 0)]
    visited[start_row][start_col] = True
    while queue:
        row, col, time = queue.pop(0)
        if row == target_row and col == target_col:
            return time
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            r, c = row + dr, col + dc
            if (0 <= r < rows and 0 <= c < cols and not visited[r][c] and
                    maps[r][c] != 'X'):
                visited[r][c] = True
                queue.append((r, c, time + 1))
    return -1
