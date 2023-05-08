T = int(input())
for i in range(1, T+1):
    result = 0
    N, K = map(int, input().split())
    pp = '0'+'1'*K+'0'
    puzzle = [[0 for a in range(N+2)] for b in range(N+2)]

    for j in range(1, N+1):
        array = list(map(int, input().split()))
        for k in range(1, N+1):
            puzzle[j][k] = array[k-1]
        row = ''.join(str(s) for s in puzzle[j])
        if pp in row:
            result += 1
    print(puzzle)
    puzzle2 = list(zip(*puzzle))
    print(puzzle2)
    for j in range(1, N+1):
        row = ''.join(str(s) for s in puzzle2[j])
        if pp in row:
            result += 1
    print("#{} {}".format(i, result))