import librosa


def calculate_tempo(audio_file, block_size):
    # Загрузка аудиофайла
    y, sr = librosa.load(audio_file)

    # Разделение аудиофайла на блоки
    block_tempo = []
    for i in range(0, len(y), block_size):
        block = y[i:i + block_size]
        tempo = librosa.beat.tempo(block, sr=sr)[0]
        block_tempo.append(tempo)

    # Усреднение темпа по блокам
    average_tempo = sum(block_tempo) / len(block_tempo)

    return average_tempo


# Пример использования
if __name__ == "__main__":
    audio_file = "Three Days Grace-Never Too Late-kissvk.com.mp3"  # Путь к вашему аудиофайлу
    block_size = 44100  # Размер блока (например, 1 секунда при частоте дискретизации 44100 Гц)

    tempo = calculate_tempo(audio_file, block_size)
    print("Average tempo:", tempo, "BPM")
