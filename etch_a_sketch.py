from turtle import Turtle, Screen


tom = Turtle()
screen = Screen()
def move_forward() -> None:
    """_Move turtle forward 10 paces_
    """
    tom.forward(10)
def move_backward() -> None:
    """_move turtle backward 10 paces_
    """
    tom.backward(10)
def move_left()->None:
    """_Turn turtle left 10 degrees_
    """
    to =tom.heading() + 10
    tom.setheading(to)
def move_right()->None:
    """_Turn turtle right 10 degrees_
    """
    to = tom.heading() - 10
    tom.setheading(to)
def clear_screen()-> None:
    """_Clear the screen and return turtle home_
    """
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()

def etch_a_sketch():
    screen.listen()
    screen.onkey(move_forward,"w")
    screen.onkey(move_backward,"s")
    screen.onkey(move_left,"a")
    screen.onkey(move_right,"d")
    screen.onkey(clear_screen,"c")
    screen.exitonclick()

if __name__ == "__main__":
    etch_a_sketch()