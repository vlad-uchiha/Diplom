import librosa
import os
import numpy as np
import matplotlib.pyplot as plt


def foo(file):
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    plt.figure(figsize=(10, 4))
    plt.plot(x, y, label='Темп')
    plt.xlabel('Время (с)')
    plt.ylabel('Темп')
    plt.title('График изменения темпа с окном в 1 секунду')
    plt.legend()
    plt.grid(True)

    if not os.path.exists('flask_proj/static'):
        os.makedirs('static')

    path = os.path.join('flask_proj/static', f'{file}.png')  # Путь для сохранения изображения
    plt.savefig(path)
    plt.close() 

    print(path)

foo("stih.mp3")