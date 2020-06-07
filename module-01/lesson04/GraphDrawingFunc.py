import turtle as t


def make_x(start_x, end_x, del_x):
    t.penup()
    t.goto(start_x, 0)
    t.pendown()
    for i in range(start_x, end_x, del_x):
        t.goto(i, 0)
        t.write(str(i))
        t.goto(i, 5)
        t.goto(i, -5)
        t.goto(i, 0)


def make_y(start_y, end_y, del_y):
    t.penup()
    t.goto(0, start_y)
    t.pendown()
    for i in range(start_y, end_y, del_y):
        t.goto(0, i)
        t.write(str(i))
        t.goto(-5, i)
        t.goto(0, i)


def make_xy(start, end, delta, color_name):
    t.pencolor(color_name)
    make_x(start, end, delta)
    make_y(start, end, delta)


if __name__ == '__main__':
    t.shape('turtle')
    make_xy(-500,500, 50, 'black')
    t.Screen().mainloop()
