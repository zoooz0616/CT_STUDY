list=[]
for i in range(10):
    a = int(input())
    list.append(a%42)
num=set(list)
print(len(num))