import turtle

turtle.setup(400,500)
J = turtle.Screen()
J.title("Tess becomes a traffic light!")
J.bgcolor("lightgreen")
tess = turtle.Turtle()
Z = turtle.Turtle()
S = turtle.Turtle()


def draw_housing():

    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()


draw_housing()

tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle

tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")


Z.forward(40)
Z.left(90)
Z.forward(190)

Z.shape("circle")
Z.shapesize(3)
Z.fillcolor("black")

S.forward(40)
S.left(90)
S.forward(120)
S.shape("circle")
S.shapesize(3)
S.fillcolor("black")


state_num = 2


def advance_state_machine():
    global state_num
    if state_num == 0:
        tess.fillcolor("black")
        Z.fillcolor("black")
        S.fillcolor("orange")
        state_num = 1
    elif state_num == 1:
        tess.fillcolor("black")
        S.fillcolor("black")
        Z.fillcolor("red")
        state_num = 2
    else:
        Z.fillcolor("black")
        S.fillcolor("black")
        tess.fillcolor("green")
        state_num = 0


J.onkey(advance_state_machine, "space")

J.listen()
J.mainloop()