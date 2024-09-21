""" florWendy/app.py """
from flask import Flask, render_template
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Usar el backend Agg
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def home():
    draw_flower()
    return render_template('index.html')

def draw_flower():
    # Asegúrate de que el directorio existe
    os.makedirs('static/images', exist_ok=True)

    # Crear una figura
    plt.figure(figsize=(6, 6))
    ax = plt.subplot(111, projection='polar')
    ax.set_facecolor('black')

    # Generar la flor
    num_petals = 12
    theta = np.linspace(0, 2 * np.pi, 100)
    r = 1 + 0.5 * np.sin(num_petals * theta)

    ax.plot(theta, r, color='#FFA216')

    # Dibuja el centro de la flor
    ax.plot(0, 0, 'o', markersize=10, color='#8B4513')

    # Configura el título y el estilo
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_ylim(0, 1.5)

    # Agregar texto
    plt.text(0, -1.1, "Feliz Día del Amor y la Amistad Wendy", ha='center', fontsize=16, color='white')

    # Llama a plt.draw() para preparar la figura
    plt.draw()

    # Guardar la imagen
    plt.savefig('static/images/flor.png', bbox_inches='tight', facecolor='black')
    plt.close()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
