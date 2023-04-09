n = int(input())
start_index=1
end_index=1
sum = 1
count = 1 #자기 자신 하나만 더한다고 가정.

while end_index != n :
    if sum == n : #정답일 때
        count += 1
        end_index += 1
        sum += end_index

    if sum > n:
        sum -= start_index
        start_index += 1

    if sum < n:
        sum += end_index
        end_index += 1

print(count)
