import numpy as np


# def ekspansji(x0,f,d,alpha,N):
#     i=0
#     x = [x0, x0 + d]
#     if f(x[1]) == f(x[0]):
#         return x[0],x[1]
#     if f(x[1]) > f(x[0]):
#         d = -d
#         x[1] = x[0] + d
#         if f(x[1]) >= f(x[0]):
#             return x[1], x[0] - d
#     for i in N:
#         i = i+1
#         #x[i+1] = x0 + (alpha**i)*d
#         x.append(x0 + (alpha**i)*d)
#         if f(x[1]) <= f(x[i+1]):
#             break
#     if d>0:
#         return x[i - 1],x[i + 1]
#     return x[i + 1],x[i - 1]

def ekspansji(x0, f, d, alpha, N):
    x = [x0, x0 + d]
    i=0
    if f(x[1]) == f(x[0]):
        return x[0], x[1]

    if f(x[1]) > f(x[0]):
        d = -d
        x[1] = x[0] + d
        if f(x[1]) >= f(x[0]):
            return x[1], x[0] - d

    for i in range(N):
        x.append(x0 + (alpha**i) * d)
        if f(x[i]) <= f(x[i + 1]):
            break

    if d > 0:
        return x[i - 1], x[i+1]

    return x[i+1], x[i - 1]
