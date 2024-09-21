""" florWendy/turtle_flower.py """
from turtle import *
from math import *

# Optimización de la velocidad
speed(0)
bgcolor("black")
tracer(10)  # Ajusta la velocidad de actualización (0 es instantáneo, 10 es una velocidad intermedia)

# Ajustar la posición inicial
penup()
goto(0, -40)
pendown()

# Dibuja las hojas (con menos iteraciones para mayor eficiencia)
for i in range(12):  # Reducimos el número de repeticiones para optimizar
    for j in range(12):  # Reducimos el número de hojas
        color('#FFA216')
        right(90)
        circle(150-j*6, 90)
        left(90)
        circle(150-j*6, 90)
        right(180)
    circle(40, 30)

# Centro de la flor
color('black')
shape('circle')
shapesize(0.5)
fillcolor('#8B4513')
golden_ang = 137.508
phi = golden_ang * (pi / 180)

for i in range(100):  # Reducimos el número de círculos
    r = 4 * sqrt(i)
    theta = i * phi
    x = r * cos(theta)
    y = r * sin(theta)
    penup()
    goto(x, y)
    setheading(i * golden_ang)
    pendown()
    stamp()

# Define los puntos para dibujar letras
def point(x, y):
    penup()
    goto(x, y)
    pendown()
    color('black')
    fillcolor('#FFA216')
    begin_fill()
    circle(4)
    end_fill()

# Función para dibujar la letra 'T'
def draw_T(x, y):
    positions_t = [(x, y+30), (x+6, y+30), (x+12, y+30), (x+18, y+30), (x+24, y+30),
                   (x+12, y+30), (x+12, y+24), (x+12, y+18), (x+12, y+12), (x+12, y+6), (x+12, y)]
    for pos in positions_t:
        point(*pos)

# Función para dibujar la letra 'Ú'
def draw_U(x, y):
    positions_u = [(x, y+30), (x, y+24), (x, y+18), (x, y+12), (x, y+6),
                   (x+3, y+3), (x+6, y), (x+12, y-1), (x+18, y), (x+21, y+3),
                   (x+24, y+6), (x+24, y+12), (x+24, y+18), (x+24, y+24), (x+24, y+30),
                   (x+12, y+36), (x+16, y+40)]
    for pos in positions_u:
        point(*pos)

# Dibuja "TÚ"
draw_T(-27, -20)
draw_U(7, -20)

# Añadir mensaje personalizado
penup()
goto(0, -120)  # Ajustar la posición para el mensaje, debajo de la flor
pendown()
color("white")
write("Feliz Día del Amor y la Amistad Wendy", align="center", font=("Arial", 16, "normal"))

# Mostrar todo de golpe para mejorar la velocidad
tracer(1)

hideturtle()
done()

getscreen().getcanvas().postscript(file="static/images/flor.ps")
from PIL import Image
img = Image.open("static/images/flor.ps")
img.save("static/images/flor.png", "png")

