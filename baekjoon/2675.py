t=int(input())
for i in range(t):
    r, s =input().split()
    # s=list(s)
    a = []
    for j in range(len(s)):
        for k in range(int(r)):
            a.append(s[j])
    for i in a:
        print(i, end='')
    print()
