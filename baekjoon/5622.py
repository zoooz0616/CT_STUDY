alph=list(input().upper())
k = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
time=0
for i in range(len(alph)):
    if alph[i] in k[0:3]: time+=3 #ABC
    elif alph[i] in k[3:6]: time+=4 #DEF
    elif alph[i] in k[6:9]: time +=5 #GHI
    elif alph[i] in k[9:12]: time+=6 #JKL
    elif alph[i] in k[12:15]: time+=7 #MNO
    elif alph[i] in k[15:19]: time+=8 #PQRS
    elif alph[i] in k[19:22]: time+=9 #TUV
    elif alph[i] in k[22:26]: time+=10 #WXYZ

print(time)