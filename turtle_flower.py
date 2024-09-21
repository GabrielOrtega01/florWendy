""" florWendy/turtle_flower.py """
from flask import Flask, render_template, send_file
from turtle import *
from math import *
import io
from PIL import Image

app = Flask(__name__)

def draw_flower():
    # Inicializar el canvas de Turtle
    screen = Screen()
    screen.setup(width=800, height=600)

    # Configuración de Turtle
    t = Turtle()
    t.speed(0)
    t.bgcolor("black")
    t.color('#FFA216')

    # Dibuja una flor simple
    for _ in range(36):
        t.circle(100)
        t.right(10)

    # Capturar el canvas
    canvas = screen.getcanvas()
    img = Image.frombytes('RGB', (canvas.winfo_width(), canvas.winfo_height()), canvas.postscript(colormode='color'))

    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)

    t.hideturtle()
    screen.bye()  # Cerrar la ventana de Turtle

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

