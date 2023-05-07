T=int(input())
for i in range(T):
    N = int(input())
    array=[]
    for j in range(1,N+1):
        array.append([1]*j)
        if j > 2:
            for k in range(1,j-1):
                array[j-1][k] = array[j-2][k-1]+array[j-2][k]
    print("#{}".format(i+1))
    for a in array:
        for b in a:
           print(b,end=' ')
        print()