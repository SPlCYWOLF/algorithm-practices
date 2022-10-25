def listen_len_finder(s, e):
    sh, sm = s.split(":")
    eh, em = e.split(":")
    if eh == sh:
        return int(em) - int(sm)
    else:
        return (int(eh) - int(sh)) * 60 + (int(em) - int(sm))


def solution(m, musicinfos):
    ans = "None"
    for info in musicinfos:
        start, end, title, melody = info.split(",")
        music_len, listen_len = len(melody), listen_len_finder(start, end)

        # 전체 재생된 음악 생성
        music = ""
        # 음악이 재생시간 보다 짧으면
        if music_len < listen_len:
            for i in range(listen_len // music_len):
                music += melody
            music += melody[:listen_len % music_len]
            # 음악이 재생시간 보다 길면
        elif music_len > listen_len:
            music = melody[:listen_len - music_len]
            # 음악이 재생시간과 같다면
        else:
            music = melody

        # 음악 일치 여부 확인
        found = False
        i, j, cnt, max_cnt = 0, 0, 0, 0
        while i < len(m) and j < len(music):

            if m[i] == music[j]:
                cnt += 1
                i += 1
                j += 1
                continue

            max_cnt = max(cnt, max_cnt)
            i = 0
            j += 1

            if max_cnt == len(m):
                found = True
                break

        if found:
            ans = title

    return ans