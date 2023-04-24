def solution(n):
    if n%2==1:
        sum =0
        for i in range(1,n+1,+2):
            sum += i
        return sum
    else:
        sum = 0
        for i in range(2, n+1,+2):
            sum+= i*i
        return sum

print(solution(10))