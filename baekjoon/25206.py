scores= {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5,"C0":2.0,"D+":1.5
        , "D0":1.0, "F":0.0}
sum=0
nanugi=0
for i in range(20):
    s =list(input().split())
    if s[2]=='P':
        continue
    else:
        level = float(s[1])
        score = scores[s[2]]
        nanugi+=level
        sum+=level*score

if sum==0:
    print(f"{sum:.6f}")
else:
    result= sum/nanugi
    print(f"{result:.6f}")
