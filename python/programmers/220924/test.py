from typing import List


# 1. '.' 이 없으면 dic에 있는지 확인 후 처리
# 1. '.' 이 있으면 '.' 기준으로 단어를 나눔

# 1-5. '.' 을 포함한 단어의 길이보다 같거나 큰게 dic에 있는지 확인
# 1-5. 있다면 ↓

# 2-1. 첫번째 부분의 단어가 dic에 일치하는게 있는지 확인, 일치하는 단어들 전부 리스트에 추가
# 2-2. 앞으로 리스트 활용
# 2-3. 남은 비속어의 길이가 '.' 을 포함한 단어의 길이보다 같거나 큰지 확인
# 2. 해당된다면, 확인한 단어 이후로 2-1 ~ 2-3 반복

dic = ["slang", "badword"]
k = 2
chat = "badword ab.cd bad.ord .word sl.. bad.word"

def myFunc(x):
    if x == '.':
        return False
    else:
        return True

def solution(k: int, dic: List[str], chat: str) -> str:
    candidates = []

    chat = list(chat.split())
    for c in chat:
        if c in dic:
            i = chat.index(c)
            chat[i] = '#' * len(c)
            continue

        if '.' in c:
            for slang in dic:
                if len(slang) >= len(c):
                    candidates.append([c, slang])


    for candidate, slang in candidates:
        if candidate not in chat:
            continue

        if "".join(set(candidate)) == ".":
            if len(candidate) * k >= len(slang):
                i = chat.index(candidate)
                chat[i] = '#' * len(candidate)
            continue

        pieces = candidate.split('.')
        start = 0
        for i in range(len(pieces)):
            p = pieces[i]
            if p not in slang:
                break

            ok = False
            if len(p) > len(candidate) - start:
                break

            if p == '':
                start += 1
                ok = True
            else:
                for t in range(k):
                    start += t

                    if p == slang[start:start+len(p)]:
                        start += len(p)
                        ok = True
                        break

            if i == len(pieces)-1 and ok:
                i = chat.index(candidate)
                chat[i] = '#' * len(candidate)
                break

    chat = " ".join(chat)

    return chat

print(solution(k, dic, chat))




# TC1 : chat = "badword ab.cd bad.ord .word sl.. bad.word"
#       dic = ["slang", "badword"]
#       k = 2
# TC2 : chat = ".. ab. cdefgh .gi. .z."
#       dic = ["abcde", "cdefg", "efgij"]
#       k = 3

# 정답 : "####### ab.cd ####### .word #### bad.word"
# 정답 : "## ### cdefgh #### .z."