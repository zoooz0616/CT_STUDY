def solution(my_string, overwrite_string, s):
    my_string=list(my_string)
    a = 0
    for i in range(s,s+len(overwrite_string)):
        my_string[i]=overwrite_string[a]
        a+=1
        answer = my_string
    return "".join(answer)


if __name__=="__main__":
    print(solution("Program29b8UYP","merS123",7))