import librosa

def calculate_tempo(frame, sr):
    # Рассчитываем амплитуду для каждого сэмпла во фрейме
    magnitudes = []
    for sample in frame:
        magnitude = abs(sample)
        magnitudes.append(magnitude)

    # Находим пики в амплитудах
    peaks = []
    for i in range(1, len(magnitudes) - 1):
        if magnitudes[i] > magnitudes[i - 1] and magnitudes[i] > magnitudes[i + 1]:
            peaks.append(i)

    # Рассчитываем частоту для каждого пика
    frequencies = []
    for peak in peaks:
        frequency = peak * sr / len(frame)
        frequencies.append(frequency)

    # Рассчитываем темп на основе разницы в частоте между пиками
    tempo = None
    if len(frequencies) > 1:
        differences = [frequencies[i] - frequencies[i - 1] for i in range(1, len(frequencies))]
        tempo = sum(differences) / len(differences)

    return tempo

# Пример использования
audio_file = 'JEEMBO- TVETH-SOLDIER OF PAIN-kissvk.com.mp3'

frame_length = 2048
hop_length = 512

audio, sr = librosa.load(audio_file)
frames = librosa.util.frame(audio, frame_length=frame_length, hop_length=hop_length).T

audio_duration = len(audio) / sr

tempos = []
for frame in frames:
    tempo = calculate_tempo(frame, sr)
    tempos.append(tempo)

for i, tempo in enumerate(tempos):
    print(f"Фрейм {i+1}: Темп = {tempo} BPM")

print(sum(tempos) / len(tempos))
print(audio_duration)


