import turtle

# Membuat window untuk menggambar
window = turtle.Screen()
window.bgcolor("white")

# Membuat turtle
t = turtle.Turtle()
t.speed(0)

# Membuat bunga
for i in range(6):
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.color("pink")
    t.begin_fill()
    for j in range(3):
        t.forward(50)
        t.right(120)
    t.end_fill()
    t.right(60)

# Membuat tangkai bunga
t.penup()
t.goto(0,-150)
t.pendown()
t.color("green")
t.pensize(10)
t.right(90)
t.forward(150)

# Menutup window ketika di-klik
window.exitonclick()
