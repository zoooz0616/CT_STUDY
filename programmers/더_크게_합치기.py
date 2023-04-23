def solution(a, b):
    answer = 0
    result1 = int(str(a)+str(b))
    result2 = int(str(b)+str(a))
    return max(result1, result2)


print(solution(9,91))