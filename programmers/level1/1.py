def solution(lottos, win_nums):
    answer = []
    rank = {
        6: 1,
        5: 2,
        4: 3,
        3: 4,
        2: 5,
        1: 6,
        0: 6,
    }
    lottos.sort()
    win_nums.sort()
    for i, lotto in enumerate(lottos):
        if lotto in win_nums:
            answer.append(lotto)
    return [rank[len(answer) + lottos.count(0)], rank[len(answer)]]
