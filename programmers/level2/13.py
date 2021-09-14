def solution(progresses, speeds):
    answer = []
    time = 0
    while progresses:
        progress, speed = progresses[0], speeds[0]
        count = 0
        time += 1
        while progresses and time * speed >= 100 - progress:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
            if not progresses:
                break
            progress, speed = progresses[0], speeds[0]
        if count != 0:
            answer.append(count)
    return answer
