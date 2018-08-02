import turtle

def draw_square(wrong_guy):
    for i in range(1,5):
        wrong_guy.forward(100)
        wrong_guy.right(90)

def draw_art():
    window=turtle.Screen()
    window.bgcolor("orange")
    jake=turtle.Turtle()
    jake.speed(200)
    for i in range(1,37):
        draw_square(jake)
        jake.right(10)

    window.exitonclick()

draw_art()

#In order to make multiple squares so that the image
#turns out to become a circle, make a loop
#with many squares at slightly different angle



#def draw_art():
    #lisa=turtle.Turtle()
    #lisa.shape("triangle")
    #lisa.color("purple")
    #lisa.circle(100)
