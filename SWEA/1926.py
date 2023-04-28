N=int(input())

for i in range(1,N+1):
    if i==3 or i==6 or i==9:
        print('-', end=' ')
        continue
    elif i>10:
        array=list(str(i).strip())
        if '3' in array or '6' in array or '9' in array:
            count=0
            for j in array:
                if j=='3' or j=='6' or j=='9':
                    count+=1
            print('-'*count, end=' ')
            continue
        else:
            print(i,end=' ')
            continue
    else:
        print(i,end=' ')