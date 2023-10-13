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
        x_list.append(x_list[0] + alpha**i * d)
        if func(x_list[i]) <= func(x_list[i + 1]):
            break
    if(d > 0):
        return x_list[i - 1], x_list[i + 1]
    return x_list[i + 1], x_list[i - 1]
