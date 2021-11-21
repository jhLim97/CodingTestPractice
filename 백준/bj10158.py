w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

result_p_mod = (p + t) // w
result_q_mod = (q + t) // h

result_p_rest = (p + t) % w
result_q_rest = (q + t) % h

result_p = result_p_rest if result_p_mod % 2 == 0 else w - result_p_rest
result_q = result_q_rest if result_q_mod % 2 == 0 else h - result_q_rest

print(result_p, result_q)
