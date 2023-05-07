T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    array = []
    for j in range(N):
        jul = list(map(int, input().split()))
        array.append(jul)
    m = 0
    for z in range(N - (M - 1)):
        for k in range(N - (M - 1)):
            score = 0
            for a in range(z, z+M):
                for b in range(k,k+M):
                    score += array[a][b]
            m = max(m, score)
    print("#{} {}".format(i+1,m))
