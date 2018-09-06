import json

def solve(elm):
    limit = elm['truck']
    n = len(elm['pipes'])
    pipes = sorted(elm['pipes'], key=lambda p: p['litres'])

    table = knapsack(limit, n, pipes)
    i, cost = find_last_value(table[n])
    route = trace(table, i, n, pipes)
    res = {'Pipes': route, 'Cost': cost}
    return res

def knapsack(limit, n, pipes):
    table = [[0 for i in range(limit+1)] for j in range(n+1)]

    for i in range(limit + 1):
        table[0][i] = float('inf')

    for i in range(1, n+1):
        cost = pipes[i-1]['cost']
        litres = pipes[i-1]['litres']
        for j in range (1, limit+1):
            if (litres > j):
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = min(table[i-1][j], table[i-1][j-litres] + cost)

    return table

def find_last_value(table):
    index = 0
    cost = 0
    for i in range(len(table)-1, -1, -1):
        if (table[i] != float('inf')):
            index = i
            cost = table[i]
            break

    return index, cost

def trace(table, index, n, pipes):
    route = []
    j = index
    for i in range (n, 0, -1):
        if (table[i][j] != table[i-1][j]):
            route.append(pipes[i-1]['name'])
            j -= pipes[i-1]['litres']
        if (j <= 0):
            break

    return route

if __name__ == "__main__":
    txt = { 'truck': 10, 'pipes': [{ 'name': 'pipe 1', 'cost': 1, 'litres': 4 }, { 'name': 'pipe 2', 'cost': 15, 'litres': 6}] }
    print(solve(txt))
