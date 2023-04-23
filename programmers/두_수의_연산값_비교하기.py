def solution(a, b):
    answer = 0
    result1 = int(str(a)+str(b))
    result2 = 2*a*b
    return max(result1,result2)


print(solution(2,91))