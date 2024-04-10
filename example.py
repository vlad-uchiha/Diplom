import librosa
import numpy as np

def calculate_tempo(frame, sr):
    # Рассчитываем амплитуду для каждого сэмпла во фрейме
    magnitudes = np.abs(frame)

    # Находим пики в амплитудах
    peaks = librosa.util.peak_pick(magnitudes, pre_max=2, post_max=5, pre_avg=2, post_avg=4, delta=0.23101, wait=0)

    # Рассчитываем частоту для каждого пика
    frequencies = librosa.fft_frequencies(sr=sr, n_fft=len(frame))
    peak_frequencies = frequencies[peaks.astype(int)]

    # Рассчитываем темп на основе разницы в частоте между пиками
    tempo = np.median(np.diff(peak_frequencies))
    return tempo

# Загрузка аудиофайла
filename = 'JEEMBO- TVETH-SOLDIER OF PAIN-kissvk.com.mp3'
y, sr = librosa.load(filename)

# Определение параметров
frame_length = 2 * sr  # Длительность фрейма в сэмплах (2 секунды)
hop_length = frame_length // 0.5  # Шаг между фреймами (50% перекрытие)

# Разбиваем аудио на фреймы
frames = librosa.util.frame(y, frame_length=frame_length, hop_length=hop_length).T

# Рассчитываем темп для каждого фрейма
tempos = []
for frame in frames:
    tempo = calculate_tempo(frame, sr)
    tempos.append(tempo)

# Выводим результат
print(tempos)
