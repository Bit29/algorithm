def solution(s):
    answer = 0
    isFirst=True
    Xs=""
    l=""
    for c in s:
        if isFirst:
            Xs+=c
            isFirst=False
        else:
            if Xs[-1] == c:
                Xs+=c
            else:
                l+=c
            if len(Xs)==len(l):
                answer+=1
                Xs=""
                l=""
                isFirst=True
    if len(Xs)!=0:
        answer+=1
    return answer