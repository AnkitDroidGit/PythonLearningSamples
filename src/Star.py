import turtle

my_turtle = turtle.Turtle()
size = 1
for _ in range(500):
    size = size +1
    for _ in range(50):
        my_turtle.forward(size)
        my_turtle.fillcolor("#555555")
        my_turtle.left(5)
