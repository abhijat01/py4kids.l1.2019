import XY as xy
import turtle as t

def line(x):
    return 3 * x

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
    t.shape('turtle')
    xy.make_xy(-500, 500, 50, 'black')

    x_list = []
    for i in range(-500, 500, 1):
        x_list.append(i)
    plot_function_values(line, x_list)

    t.Screen().mainloop()