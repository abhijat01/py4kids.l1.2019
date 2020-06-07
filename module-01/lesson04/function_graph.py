import XY as xy
import turtle as t

def line(x):
    return 3 * x

def print_function_values(function, x_values):
    y_values = []
    for x in x_values:
        y = function(x)
        y_values.append(y)
        print("x={} , y={}".format(x, y))

def plot_function_values(function, x_values):
    first_x = x_values[0]
    first_y = function(first_x)
    t.penup()
    t.goto(first_x, first_y)
    t.pendown()

    for x in x_values:
        y = function(x)
        t.goto(x, y)


if __name__ == '__main__':
    xy.make_xy(-500, 500, 50, 'black')
    x_list = []
    for i in range(-500, 500, 100):
        x_list.append(i)

    print_function_values(line, x_list)
    x_list = []
    for i in range(-500, 500, 1):
        x_list.append(i)
    plot_function_values(line, x_list)

    t.Screen().mainloop()