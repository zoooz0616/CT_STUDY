from datetime import datetime


def solution(today, terms, privacies):
    tt,pp=[],[]
    #리스트로 바꾸기
    for a in terms:
        tt.append(list(map(str,a.split())))
    for a in privacies:
        pp.append(list(map(str, a.split())))
    #맞는 약관 종류의 유효기간 찾기
    for i in range(len(pp)):
        for j in range(len(tt)):
            if pp[i][1]==tt[j][0]:
                #pp[i][0]을 숫자 값 3개로 바꾸고 tt[j][1]을 숫자로 바꿔서
                # 달에 더해줌. 달이 12개월 넘어가면 년도를 올려줌.
                array=list(map(int,pp[i][0].split('.')))
                array[1]+=int(tt[j][1]) #달끼리 더해줌
                if array[1]>12 :
                    array[1]-=12
                    array[0]+=1
                #날짜 -1하기
                if array[2]<=1:
                    array[1]-=1
                    array[2]=array[2]+28-1
                else :
                    array[2]-=1
                #결과를 string으로 바꿔서 다시 pp에 넣어주기
                pp[i][0]=str(array[0])+'.'+str(array[1])+'.'+str(array[2])
    l=list(map(int,today.split(".")))
    second=datetime(l[0],l[1],l[2])
    answer = []
    for j in range(len(pp)):
        l=list(map(int,pp[j][0].split(".")))
        first=datetime(l[0], l[1], l[2])
        ss=(second-first).total_seconds()
        if ss>0:
            answer.append(j+1)
    return answer

if __name__=='__main__':
    a = solution("2020.01.01",["Z 3", "D 5"],
             ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"])
    print(a)