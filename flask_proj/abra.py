import os
import librosa
import matplotlib.pyplot as plt
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

    return average_tempos

def draw_graph(avg_tempos: List[float]) -> None:
    """Строит график усреднения темпа по времени.

    Args:
        avg_tempos: Список усредненных темпов.

    Returns:
        None
    """

    plt.plot(average_tempos, label='Усредненный темп (BPM)')
    plt.xlabel('Время (в секундах)')
    plt.ylabel('Темп (в BPM)')
    plt.title('Усредненный темп по времени')
    plt.legend()
    plt.grid(True)
    plt.show()

# Пример использования
audio_file = 'flask_proj/uploads/JEEMBO- TVETH-SOLDIER OF PAIN-kissvk.com.mp3'

frame_length = 2048
hop_length = 512

y, sr = librosa.load(audio_file)
frames = librosa.util.frame(y, frame_length=frame_length, hop_length=hop_length).T

audio_duration = len(y) / sr

# Вычисляем усредненные темпы по блокам
average_tempos = calculate_average_tempos(frames, sr, audio_duration, 1)

for i, avg_tempo in enumerate(average_tempos):
    print(f"Block {i}: Tempo = {avg_tempo} ")

# Выводим среднее значение темпа и длительность аудиофайла
print('Сумма темпов = ', sum(average_tempos))
print('Среднее значение темпа:', sum(average_tempos) / len(average_tempos), 'BPM')
print('Длительность аудиофайла:', audio_duration, 'секунд')

draw_graph(average_tempos)
