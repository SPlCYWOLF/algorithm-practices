import sys
import pandas as pd
sys.stdin = open('input.txt')

# 소요시간 약 4시간 ㅇㅅㅇ;
# 백준 출력초과로 통과 x

# 라인 인 경우 처리
# text인 경우 처리
# 클리어 인 경우 처리
# 포인트인 경우 처리
# print 인 경우 처리

# 겹치는 경우 처리
# 그림판 처리

def handle_line(x1, y1, x2, y2):
    mark = "/"
    if (x1 < x2 and y1 < y2) or (x1 > x2 and y1 > y2):
        mark = "\\"
        bx, by, sx, sy = max(x1, x2), max(y1, y2), min(x1, x2), min(y1, y2)
        while bx != sx and by != sy:
            if canvas[sy][sx] == "/":
                canvas[sy][sx] = "x"
            elif canvas[sy][sx] == mark:
                pass
            elif canvas[sy][sx]:
                canvas[sy][sx] = "*"
            else:
                canvas[sy][sx] = mark
            sx = sx + 1
            sy = sy + 1
        canvas[sy][sx] = mark
    elif x1 == x2 and y1 != y2:
        mark = "|"
        by, sy = max(y1, y2), min(y1, y2)
        while by != sy:
            if canvas[sy][x1] == "-":
                canvas[sy][x1] = "+"
            elif canvas[sy][x1] == mark:
                pass
            elif canvas[sy][x1]:
                canvas[sy][x1] = "*"
            else:
                canvas[sy][x1] = mark
            sy = sy + 1
        canvas[sy][x1] = mark
    elif x1 != x2 and y1 == y2:
        mark = "-"
        bx, sx = max(x1, x2), min(x1, x2)
        while bx != sx:
            if canvas[y1][sx] == "|":
                canvas[y1][sx] = "+"
            elif canvas[y1][sx] == mark:
                pass
            elif canvas[y1][sx]:
                canvas[y1][sx] = "*"
            else:
                canvas[y1][sx] = mark
            sx = sx + 1
        canvas[y1][sx] = mark
    else:
        bx, by, sx, sy = max(x1, x2), max(y1, y2), min(x1, x2), min(y1, y2)
        while bx != sx and by != sy:
            if canvas[sy][bx] == "\\":
                canvas[sy][bx] = "x"
            elif canvas[sy][bx] == mark:
                pass
            elif canvas[sy][bx]:
                canvas[sy][bx] = "*"
            else:
                canvas[sy][bx] = mark
            bx = bx - 1
            sy = sy + 1
        canvas[sy][bx] = mark

def handle_text(x, y, txt):
    txt = list(txt)
    for i in range(len(txt)):
        if x + i <= W:
            if canvas[y][x+i]:
                canvas[y][x+i] = "*"
            else:
                canvas[y][x+i] = txt[i]

def handle_clear(x1, y1, x2, y2):
    bx, by, sx, sy = max(x1, x2), max(y1, y2), min(x1, x2), min(y1, y2)
    for i in range(sy, by+1):
        for j in range(sx, bx+1):
            canvas[i][j] = ""

def handle_point(x, y):
    if canvas[y][x] == "o":
        pass
    elif canvas[y][x]:
        canvas[y][x] = "*"
    else:
        canvas[y][x] = "o"

def draw_frame():
    canvas[0][0], canvas[-1][-1], canvas[0][-1], canvas[-1][0] = "+", "+", "+", "+"
    for i in range(1, H+1):
        canvas[i][0], canvas[i][-1] = "|", "|"
    for j in range(1, W+1):
        canvas[0][j], canvas[-1][j] = "-", "-"

def handle_print():
    draw_frame()
    df = pd.DataFrame(canvas)
    print(df)
    print()


while True:
    W, H = map(int, input().split())

    if W == 0 and H == 0:
        break

    canvas = list([""] * (W+2) for _ in range(H+2))

    printed = False
    while not printed:
        command = list(map(str, input().split()))
        if command[0] == "LINE":
            handle_line(int(command[1]), int(command[2]), int(command[3]), int(command[4]))
        elif command[0] == "TEXT":
            handle_text(int(command[1]), int(command[2]), command[3])
        elif command[0] == "CLEAR":
            handle_clear(int(command[1]), int(command[2]), int(command[3]), int(command[4]))
            pass
        elif command[0] == "POINT":
            handle_point(int(command[1]), int(command[2]))
        else:
            handle_print()
            printed = True
