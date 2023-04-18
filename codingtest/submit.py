import sys
def main():
    t = int(sys.stdin.readline())
    for i in range(t):  # testcase 수
        n = int(sys.stdin.readline())
        list = []
        for j in range(n):  # 바둑판 nxn
            st = sys.stdin.readline().split()
            list.append(st)

        px = -1
        py = -1

        for j in range(n):
            for k in range(n):
                if list[j][k] == 'X':
                    px = k
                    py = j

        result = 0
        isjumped = False
        # 오른쪽
        for j in range(px+1, n):
            if list[py][j] == "L":
                continue
            elif list[py][j] == "Y":
                break
            elif list[py][j] == "H":
                if (isjumped):
                    result += 1
                    break
                else:
                    isjumped = True
        # 왼쪽
        isjumped = False
        for j in range(px-1, -1, -1):
            if list[py][j] == 'L':
                continue
            elif list[py][j] == 'Y':
                break
            elif list[py][j] == 'H':
                if (isjumped):
                    result += 1
                    break
                else:
                    isjumped = True
        # 아래쪽
        isjumped = False
        for j in range(py+1, n):
            if list[j][px] == 'L':
                continue
            elif list[j][px] == 'Y':
                break
            elif list[j][px] == 'H':
                if (isjumped):
                    result += 1
                    break
                else:
                    isjumped = True
        # 위쪽
        isjumped = False
        for j in range(py-1, -1, -1):
            if list[j][px] == 'L':
                continue
            elif list[j][px] == 'Y':
                break
            elif list[j][px] == 'H':
                if (isjumped):
                    result += 1
                    break
                else:
                    isjumped = True
        print("#{} {}".format(i + 1, result))


if __name__ == '__main__':
    main()