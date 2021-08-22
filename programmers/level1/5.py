from collections import defaultdict
def solution(board, moves):
    answer = 0
    boardTemp = defaultdict(list)
    board.reverse()
    for _, board_ in enumerate(board):
        for i, elem in enumerate(board_):
            if elem != 0:
                boardTemp[i + 1].append(elem)
    stack = []
    for _, move in enumerate(moves):
        if len(boardTemp[move]) > 0:
            elem = boardTemp[move].pop()
            if len(stack) > 0 and elem == stack[-1]:
                stack.pop()
                answer += 2
            else:
                stack.append(elem)
    return answer
