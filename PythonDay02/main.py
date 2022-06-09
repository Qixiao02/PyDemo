# x = float(input('x = '))
# if x > 1:
#     y = 3 * x -5
# elif -1 <= x <= 1:
#     y = x + 2
# elif x < -1:
#     y = 5 * x + 3
# print('%.1f = %.2f' % (x, y))
# 优化👇
def Math_function():
    print(f"f(x) =\t3x - 5 (x > 1) \n\t\tx + 2 (-1 <= x <= 1) \n\t\t5x + 3 (x < -1)")
    x = float(input('x = '))
    if x > 1:
        y = 3 * x - 5
    else:
        if -1 <= x <= 1:
            y = x + 2
        else:
            y = 5 * x + 3
    return y
print("y = " "%.2f" % Math_function())