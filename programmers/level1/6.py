def solution(absolutes, signs):
    answer = 0
    for absolute, sign in zip(absolutes, signs):
        if not sign:
            absolute *= -1
        answer += absolute
    return answer
