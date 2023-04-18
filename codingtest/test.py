# 장기판에서 포가 먹을 수 있는 알의 수를 구하여라 바둑판은 8<=N<= 100 이다 .
# 이동이 가능한포는 X 로 표기된다 .
# 이동이 불가능한 다른 포는 Y 로 표기된다 일반 알은 H 로 표기되며 , 빈칸은 L 로 표기된다.
# 포 X 는 다른 포 Y 를 넘을 수 없으며 , 한 알을 넘어야 다른 알을 먹을 수 있다.
# 빈칸은 넘어간다 테스트케이스는 10 개가 주어지며 , 모두 통과해야 PASS 이고 , 일부 혹은 전부 오답일 경우 FAIL 이다.
import sys

def main():
    t = int(sys.stdin.readline())
    for i in range(t): #testcase 수
        n = int(sys.stdin.readline())
        list = []
        for j in range(n): #바둑판 nxn
            st=sys.stdin.readline().split()
            list.append(st)

        px=-1
        py=-1

        for j in range(n):
            for k in range(n):
                if list[j][k]=='X':
                    px=j
                    py=k

        result=0

        isJumped = False
        #오른쪽
        for j in range(py+1, n):
            if list[px][j]=='L':
                continue
            elif list[px][j]=='Y':
                break
            elif list[px][j]=='H':
                if(isJumped):
                    result+=1
                    break
                else: isJumped=True

        #왼쪽
        isJumped = False
        for j in range(py-1, -1, -1):
            if list[px][j]=='L':
                continue
            elif list[px][j]=='Y':
                break
            elif list[px][j]=='H':
                if(isJumped):
                    result+=1
                    break
                else: isJumped=True

        #아래쪽
        isJumped = False
        for j in range(px+1,n):
            if list[j][py] == 'L':
                continue
            elif list[j][py] == 'Y':
                break
            elif list[j][py] == 'H':
                if (isJumped):
                    result+=1
                    break
                else:
                    isJumped = True
        #아래쪽
        isJumped = False
        for j in range(px-1,-1,-1):
            if list[j][py] == 'L':
                continue
            elif list[j][py] == 'Y':
                break
            elif list[j][py] == 'H':
                if (isJumped):
                    result+=1
                    break
                else:
                    isJumped = True
        print("#{} {}".format(i+1,result))

if __name__=='__main__':
    main()