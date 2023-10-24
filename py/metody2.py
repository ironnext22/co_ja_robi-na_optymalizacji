def ekspansja(x0: float, d: float, alpha: float, nmax: int, func):
    i = 0
    x_list = [x0, x0 + d]
    if func(x_list[0]) == func(x_list[1]):
        return x_list[0], x_list[1]
    if func(x_list[1]) > func(x_list[0]):
        d = -d
        x_list[1] = x_list[0] + d
        if func(x_list[1]) >= func(x_list[0]):
            return x_list[1], x_list[0] - d
    while True:
        if i > nmax:
            raise ValueError("Nmax has been exceeded")
        i += 1
        x_list.append(x_list[0] + alpha ** i * d)
        if func(x_list[i]) <= func(x_list[i + 1]):
            break
    if (d > 0):
        return x_list[i - 1], x_list[i + 1]
    return x_list[i + 1], x_list[i - 1]


def fibonacci(a: float, b: float, epsilon: float, func):
    fib_seq = [0, 1]
    k = 1
    while fib_seq[k] < (b - a) / epsilon:
        fib_seq.append(fib_seq[-2] + fib_seq[-1])
        k += 1
    a_list = [a]
    b_list = [b]
    c_list = [b_list[0] - fib_seq[k - 1] / fib_seq[k] * (b_list[0] - a_list[0])]
    d_list = [a_list[0] + b_list[0] - c_list[0]]

    for i in range(k - 3):
        if func(c_list[i]) < func(d_list[i]):
            a_list.append(a_list[i])
            b_list.append(d_list[i])
        else:
            b_list.append(b_list[i])
            a_list.append(c_list[i])
        c_list.append(b_list[i + 1] - fib_seq[k - i - 2] / fib_seq[k - i - 1] * (b_list[i + 1] - a_list[i + 1]))
        d_list.append(a_list[i + 1] + b_list[i + 1] - c_list[i + 1])
    return c_list[i + 1]