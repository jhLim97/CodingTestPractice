from collections import defaultdict

def solution(tickets):
    answer = []
    
    d = defaultdict(list)
    for depart, arrive in tickets:
        d[depart].append(arrive)
        
    for depart, arrives in d.items():
        arrives.sort(reverse = True)
        
    stack = ["ICN"]
    while stack:
        depart = stack[-1]
        if depart in d and d[depart]:
            stack.append(d[depart].pop())
        else:
            answer.append(stack.pop())
            
    answer.reverse()
    return answer
