croatia = input()
clist=["c=","c-","dz=","d-","lj","nj","s=","z="]
num=0
real_croatia=croatia
for c in clist:
    if c in real_croatia:
        while True:
            if c in croatia:
                croatia = croatia.replace(c, " ", 1)
                num += 1
            else: break

croatia=croatia.replace(" ","")
print(num + len(croatia))