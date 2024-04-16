import os
import librosa
import numpy as np
import matplotlib.pyplot as plt
from flask import jsonify
from typing import List


def calculate_average_tempos(frames: List[float], sr: int, audio_duration: float, n: int) -> List[float]: 
    """Вычисляет усредненные темпы по блокам для аудиофайла.

    Args:
        frames: Список фреймов аудио.
        sr: Частота дискретизации аудио.
        audio_duration: Длительность аудиофайла в секундах.
        n: Размер блока для усреднения темпов.

    Returns:
        Список усредненных темпов по блокам.
    """
    # Тело функции


    frames_per_sec = len(frames) // int(audio_duration) * n

    # Создаем список для хранения усредненных темпов
    average_tempos = []

    # Для каждой секунды в аудиофайле
    for i in range(int(audio_duration) // n):
        start_frame = i * frames_per_sec
        end_frame = start_frame + frames_per_sec
        tempo_sum = 0

        # Вычисляем средний темп для каждого фрагмента
        for frame in frames[start_frame:end_frame]:
            tempo, _ = librosa.beat.beat_track(y=frame, sr=sr)  # Используем librosa.beat.beat_track
            tempo_sum += tempo

        # Добавляем усредненный темп для данной секунды
        average_tempos.append(tempo_sum / frames_per_sec)
    

    return list(map(int, average_tempos))


import os

def draw_graphic(tempos: List[float], file: str, times) -> str:
    """Отрисовка графика для полученного аудиофайла и сохранение его как изображения.
    
    Args:
        tempos: Список темпов.
        times: Временные метки.
    
    Returns:
        Путь к картинке графика.
    """
    plt.figure(figsize=(10, 4))
    plt.plot(times, tempos, label='Темп')
    plt.xlabel('Время (с)')
    plt.ylabel('Темп')
    plt.title('График изменения темпа с окном в 1 секунду')
    plt.legend()
    plt.grid(True)
    # plt.show()

    # if not os.path.exists('static'):
    #     os.makedirs('static')

    # Сохраняем изображение
    path = os.path.join('static/', f'{file.replace(" ","")}.png')  # Путь для сохранения изображения
    plt.savefig(path)
    plt.close()  # Закрываем текущее изображение
    return path


def run_abra_script(filename: str) -> dict:
    """Запускает скрипт Abra для аудиофайла с заданным именем и возвращает результаты выполнения.
    
    Args:
        filename: Имя загруженного аудиофайла.
    
    Returns:
        Результат выполнения скрипта Abra.
    """
    try:
        frame_length = 2048
        hop_length = 512

        y, sr = librosa.load(f'flask_proj/uploads/{filename}')
        frames = librosa.util.frame(y, frame_length=frame_length, hop_length=hop_length).T

        audio_duration = len(y) / sr

        # Вычисляем усредненные темпы по блокам
        average_tempos = calculate_average_tempos(frames, sr, audio_duration, 1)

        time = np.linspace(0, audio_duration, len(average_tempos))

        image_path = draw_graphic(average_tempos, filename, time)

        return {
            'image_path': image_path,
            'average_tempos': average_tempos,
            'total_tempo': int(sum(average_tempos)),
            'average_tempo': int(sum(average_tempos) / len(average_tempos)),
            'audio_duration': int(audio_duration)
        }

    except Exception as e:
        return {'error': str(e)}

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        result = run_abra_script(filename)
        print(result)