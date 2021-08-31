def solution(s):
    stack = []
    for _, s_ in enumerate(s):
        if stack:
            if stack[-1] == s_:
                stack.pop()
            else:
                stack.append(s_)
        else:
            stack.append(s_)
    if stack:
        return 0
    else:
        return 1
