from collections import defaultdict

def solution(tickets):
    tickets.sort()
    stack = ["ICN"]
    data = []
    dic = defaultdict(list)
    
    for ticket in tickets:
        depart, arrive = ticket
        dic[depart].append(arrive)
        dic[depart].sort(reverse=True)
    while stack:
        depart = stack[-1]
        if depart in dic and dic[depart]:
            stack.append(dic[depart].pop())
        else:
            data.append(stack.pop())
    data.reverse()
    return data
