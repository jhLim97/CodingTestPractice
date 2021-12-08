def solution(w,h):
    a, b = max([w, h]), min([w, h])
    while True:
        r = a % b
        if r == 0:
            break
        a, b = b, r
    
    answer = w * h - (w + h - b)
    return answer
