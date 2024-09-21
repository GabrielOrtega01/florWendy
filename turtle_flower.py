""" florWendy/turtle_flower.py """
from flask import Flask, render_template, send_file
from turtle import *
from math import *
import io
from PIL import Image

app = Flask(__name__)

def draw_flower():
    # Configuración de Turtle
    speed(0)
    bgcolor("black")
    tracer(10)
    penup()
    goto(0, -40)
    pendown()

    # Dibuja las hojas
    for i in range(12):
        for j in range(12):
            color('#FFA216')
            right(90)
            circle(150 - j * 6, 90)
            left(90)
            circle(150 - j * 6, 90)
            right(180)
        circle(40, 30)

    # Centro de la flor
    color('black')
    shape('circle')
    shapesize(0.5)
    fillcolor('#8B4513')
    golden_ang = 137.508
    phi = golden_ang * (pi / 180)

    for i in range(100):
        r = 4 * sqrt(i)
        theta = i * phi
        x = r * cos(theta)
        y = r * sin(theta)
        penup()
        goto(x, y)
        setheading(i * golden_ang)
        pendown()
        stamp()

    # Dibuja "TÚ"
    draw_T(-27, -20)
    draw_U(7, -20)

    # Añadir mensaje personalizado
    penup()
    goto(0, -120)
    pendown()
    color("white")
    write("Feliz Día del Amor y la Amistad Wendy", align="center", font=("Arial", 16, "normal"))

    # Capturar el canvas
    canvas = getscreen().getcanvas()
    img = Image.frombytes('RGB', (canvas.winfo_width(), canvas.winfo_height()), canvas.postscript(colormode='color'))

    # Guardar en un objeto BytesIO para enviarlo directamente
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    return img_io

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/flower')
def flower():
    img_io = draw_flower()
    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)

