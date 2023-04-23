word = input()
result = 1
for i in range(len(word)//2):
    if word[i] == word[-1 * i -1]:
        continue
    else:
        result=0
print(result)