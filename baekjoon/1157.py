word=input().upper()
list=[]
count=[]

def alpha(word):
    global list, count
    for i in word:
        if i in list:
            continue
        list.append(i)

    for i in list:
        count.append(word.count(i))

    for i in range(len(count)):
        if count[i]==max(count):
            if i != count.index(max(count)):
                return "?"
    return list[count.index(max(count))]

if __name__ =="__main__":
    print(alpha(word))

