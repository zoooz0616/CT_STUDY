def solution(my_string, overwrite_string, s):
    w = my_string[s:s+len(overwrite_string)]
    answer = my_string.replace(w, overwrite_string)
    return answer


if __name__=="__main__":
    print(solution("Program29b8UYP","merS123",7))