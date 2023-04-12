from collections import deque

n = int(input())
myQue = deque()

for i in range(1,n+1):
    myQue.append(i)

while len(myQue) >1:
    myQue.popleft()
    myQue.append(myQue.popleft())

print(myQue[0]);