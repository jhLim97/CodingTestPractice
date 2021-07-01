from collections import deque, defaultdict

def solution(tickets):
    answer = []
    
    tickets.sort(key = lambda x : (x[0], x[1]))
    d = defaultdict(list)
    
    for depart, arrive in tickets:
        d[depart].append(arrive)
        d[depart].sort(reverse = True)

    stack = ["ICN"]
    while stack:
        depart = stack[-1]
        if d[depart]:
            stack.append(d[depart].pop())
        else:
            answer.append(stack.pop())
    
    return answer[::-1]
