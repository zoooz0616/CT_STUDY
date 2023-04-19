alph="abcdefghijklmnopqrstuvwxyz"
arrays=[-1]*26
s=list(input().rstrip())
for i in range(len(s)):
    for j in range(len(alph)):
        if s[i]==alph[j]:
            if arrays[j]!=-1:
                continue
            arrays[j]=i

for i in arrays:
    print(i, end=' ')