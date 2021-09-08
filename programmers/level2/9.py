from collections import defaultdict

def helper(skill_tree, skill, dic):
    adoptedSkillOrder = []
    for skill_tree_ in skill_tree:
        temp = dic[skill_tree_]
        if temp == 0:
            continue
        if not adoptedSkillOrder or adoptedSkillOrder[-1] == temp - 1:
            adoptedSkillOrder.append(temp)
        else:
            return False
    if adoptedSkillOrder and adoptedSkillOrder[0] != 1:
        return False
    return True
def solution(skill, skill_trees):
    answer = 0
    index = 1
    dic = defaultdict(int)
    for skill_ in skill:
        dic[skill_] = index
        index += 1
    for skill_tree in skill_trees:
        if helper(skill_tree, skill, dic):
            answer += 1   
    return answer
