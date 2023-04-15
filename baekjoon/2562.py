max=0
for i in range(9):
    a = int(input())
    if a > max:
        max = a
        index=i
print("{}\n{}".format(max,index+1))