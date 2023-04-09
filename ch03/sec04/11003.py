from collections import deque
n, l = map(int, input().split())
mydeque = deque()
now = list(map(int, input().split()))

#새 값이 들어올 때마다 정렬 대신 현재 수보다 큰 값을 덱에서 제거해 시간 복잡도 줄임
for i in range(n):
    while mydeque and mydeque[-1][0] > now[i]:
        mydeque.pop()
    mydeque.append((now[i], i))
    if mydeque[0][1] <= i- l:
        mydeque.popleft()
    print(mydeque[0][0], end=' ')
