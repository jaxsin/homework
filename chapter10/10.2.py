
import turtle

turtle.setup(200,500)
wn = turtle.Screen()
wn.title("Traffic light charges color automatically")
wn.bgcolor("blue")

J = turtle.Turtle()
def draw_picture():
    J.pensize(3)
    J.color("black", "blue")
    J.begin_fill()
    J.forward(60)
    J.left(90)
    J.forward(200)
    J.circle(40, 180)
    J.forward(200)
    J.left(90)
    J.forward(20)
    J.end_fill()
draw_picture()

J.penup()
J.forward(20)
J.left(90)
J.forward(50)
J.shape("circle")
J.shapesize(3)
J.fillcolor("green")

state_num = 0


def advance_state_machine():
    global state_num
    if state_num == 0:
        J.forward(70)
        J.fillcolor("orange")
        state_num = 1
        wn.ontimer(advance_state_machine, 3000)
    elif state_num == 1:
        J.forward(70)
        J.fillcolor("red")
        wn.ontimer(advance_state_machine, 20000)
        state_num = 2
    else:
        J.back(140)
        J.fillcolor("green")
        wn.ontimer(advance_state_machine, 20000)
        state_num = 0


advance_state_machine()
wn.listen()
wn.mainloop()