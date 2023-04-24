n=int(input()) #단어의 개수
count = 0  # 그룹단어 개수
for i in range(n): #단어 개수만큼 테스트
    alphalist = [] #한단어의 알파벳 리스트
    word=list(input())
    for j in range(len(word)):
        boo = True
        if word[j] in alphalist:
            if word[j]==word[j-1]:
                continue
            else:
                boo = False
                break
        else:
            alphalist.append(word[j])
    if(boo):
        count+=1
print(count)