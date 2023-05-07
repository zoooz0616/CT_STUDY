array=[]
for i in range(9):
    array.append(list(map(int,input().split())))

max=0
x=0
y=0
for i in range(9):
    for j in range(9):
        if array[i][j]>=max:
            max=array[i][j]
            x=i+1
            y=j+1
print(max)
print(x,y)