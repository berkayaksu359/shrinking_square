import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("black")
turtle_screen.title("shrinking square")

#eğer çizginin rengini değiştirmek istersek ise böyle

turtle_instance = turtle.Turtle()
turtle_instance.color("white")

#bu şekilde colorını değiştirebiliriz
def shrinkingSquare(size):
    for i in range(6):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size = size -2
shrinkingSquare(150)
shrinkingSquare(140)
shrinkingSquare(130)
shrinkingSquare(120)
shrinkingSquare(110)
shrinkingSquare(100)
shrinkingSquare(90)
shrinkingSquare(80)
shrinkingSquare(70)
shrinkingSquare(60)
shrinkingSquare(50)
shrinkingSquare(40)

turtle.done()