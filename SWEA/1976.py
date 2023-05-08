T = int(input())
for i in range(1, T+1):
    h, m = 0, 0
    h1, m1, h2, m2 = map(int, input().split())
    m = m1 + m2
    h = h1 + h2 + (m // 60)
    if m >= 60 :
        m %= 60
    if h >= 13:
        h %= 12
    print("#{} {} {}".format(i, h, m))