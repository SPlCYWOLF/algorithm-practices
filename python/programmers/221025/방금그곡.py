from collections import deque

def listen_len_finder(s, e):
    sh, sm = s.split(":")
    eh, em = e.split(":")
    if eh == sh:
        return int(em) - int(sm)
    else:
        return (int(eh) - int(sh)) * 60 + (int(em) - int(sm))


def melody_convert(mel):
    new_melody = ""
    for i in range(len(mel)):
        if mel[i] == "#":
            new_melody = new_melody[:-1]
            new_melody += mel[i - 1].lower()
        else:
            new_melody += mel[i]

    return new_melody


def played_melody_finder(mel, t):
    # 전체 재생된 음악 생성
    played_mel = ""
    melody_len = len(mel)

    if melody_len < t:      # 전체 음악이 라디오 재생시간 보다 짧으면
        for i in range(t // melody_len):
            played_mel += mel
        played_mel += mel[:t % melody_len]

    elif melody_len > t:    # 전체 음악이 라디오 재생시간 보다 길면
        played_mel = mel[:t - melody_len]

    else:                   # 전체 음악이 라디오 재생시간과 같다면
        played_mel = mel

    return played_mel


# 2차 시도 90% 성공
def solution(m, musicinfos):

    # 샵 구분 지어 기억하는 멜로디 재구성
    m = melody_convert(m)

    music_dict = dict()
    music_order = deque()
    for info in musicinfos:
        start, end, title, melody = info.split(",")

        # 라디오에서 재생 시간 계산
        time = listen_len_finder(start, end)

        # 샵 구분지어서 멜로디 재구성
        melody = melody_convert(melody)

        # 딕셔너리에 각 음악 정보 저장
        music_dict[title] = {"time": time, "melody": melody}

        # 음악 순서 매기기
        if music_order:
            if time > music_dict[music_order[0]]["time"]:
                music_order.appendleft(title)
            elif time == music_dict[music_order[0]]["time"]:
                music_order.insert(1, title)
            else:
                music_order.append(title)
        else:
            music_order.append(title)


    # 부분 문자열 비교 (찾는 즉시 루프 종료)
    for music in music_order:

        # 라디오에서 재생된 멜로디 복원
        played_melody = played_melody_finder(music_dict[music]["melody"], music_dict[music]["time"])

        # 부분 문자열 비교 시작
        i, j, cnt = 0, 0, 0
        while i < len(m) and j < len(played_melody):
            if m[i] == played_melody[j]:
                cnt += 1
                i += 1
                j += 1
                if cnt == len(m):
                    return music
                continue

            cnt = 0
            i = 0
            j += 1

    return "(None)"






# 1차 시도 70% 성공
# def solution(m, musicinfos):
#     ans = "None"
#     longest_song = 0
#     m = melody_convert(m)
#     for info in musicinfos:
#         start, end, title, melody = info.split(",")
#
#         # 샵(멜로디) 구분 시키기
#         melody = melody_convert(melody)
#
#         music_len, listen_len = len(melody), listen_len_finder(start, end)
#
#         # 조건일치 음악이 복수일때 라디오에서 재생된 가장 긴 시간을 기록하기 위함
#         longest_song = max(longest_song, listen_len)
#
#         # 전체 재생된 음악 생성
#         music = ""
#
#         # 전체 음악이 라디오 재생시간 보다 짧으면
#         if music_len < listen_len:
#             for i in range(listen_len // music_len):
#                 music += melody
#             music += melody[:listen_len % music_len]
#
#             # 전체 음악이 라디오 재생시간 보다 길면
#         elif music_len > listen_len:
#             music = melody[:listen_len - music_len]
#
#             # 전체 음악이 라디오 재생시간과 같다면
#         else:
#             music = melody
#
#         # 음악 일치 여부 확인 (부분 문자열 확인)
#         found = False
#         i, j, cnt, max_cnt = 0, 0, 0, 0
#         while i < len(m) and j < len(music):
#
#             if m[i] == music[j]:
#                 cnt += 1
#                 i += 1
#                 j += 1
#                 continue
#
#             max_cnt = max(cnt, max_cnt)
#             cnt = 0
#             i = 0
#             j += 1
#
#             if max_cnt == len(m):
#                 if listen_len == longest_song or ans == "None":
#                     found = True
#                     break
#
#         if cnt == len(m):
#             if listen_len == longest_song or ans == "None":
#                 found = True
#
#         if found:
#             ans = title
#
#     return ans


b = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF", "13:00,13:05,WOW,ABCDEF", "13:00,13:05,HOW,ABCDEF"]
a = "ABC"

print(solution(a, b))

temp = [1, 1, 1, 2, 3]
tt = temp[::-1]
i = tt.index(1) - 1
print(tt[i])