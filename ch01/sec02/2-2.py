# 배열의 주어진 범위의 합을 2로 나눈 몫을 구하세요.
import random

testcase = int(input('몇번 테스트? : '))
answer = 0
A = [0] * (100001)

for i in range(0, 10001):
    A[i] = random.randrange(1, 101)

for t in range(1, testcase + 1):
    start, end = map(int, input('숫자 두개 입력: ').split())

    for i in range(start, end + 1):
        answer = answer + A[i]

    print(str(testcase) + " " + str(answer / 2))
