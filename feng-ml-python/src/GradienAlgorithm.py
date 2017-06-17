# encoding=utf-8

x_old = 0
x_new = 6
gamma = 0.01
precision = 0.00000001


# x = Symbol("x")
# f = (x ** 4) - (3 * (x ** 3)) + 2

# 梯度下降算法
def df(x):
    y = 4 * x ** 3 - 9 * x ** 2
    return y


while abs(x_new - x_old) > precision:
    x_old = x_new
    x_new += -gamma * df(x_old)

print("The local minimum occurs at", x_new)


#梯度上升算法
def df(x):
    y = -2 * x
    return y


while abs(x_new - x_old) > precision:
    x_old = x_new
    x_new += gamma * df(x_old)

print("The local maximum occurs at", x_new)
