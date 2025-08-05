def s_o_d(n):
    total = 0
    for i in range(1, n + 1):
        div_sum = 0
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                div_sum += j
                if j != i // j:
                    div_sum += i // j
        total += div_sum
    return total

print(s_o_d(4))
