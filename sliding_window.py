import os
import numpy as np
import librosa
import matplotlib.pyplot as plt
import csv

def sliding_window_tempo_analysis(audio_file, hop_length=512):
    y, sr = librosa.load(audio_file)
    tempo_series = librosa.feature.tempogram(y=y, sr=sr, hop_length=hop_length)
    try:
        bpm = librosa.beat.tempo(tempo_series, sr=sr, hop_length=hop_length)[0]
        return bpm
    except Exception as e:
        print(f"An error occurred in librosa.beat.tempo: {e}")
        return None

def print_tempo_analysis_results(mean_tempo):
    print("Результаты для скользящего окна")
    for i, tempo in enumerate(mean_tempo):
        print(f"Окно {i}: Темп = {tempo}")

def save_tempo_analysis_results_to_file(mean_tempo, output_file):
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Окно', 'Темп (bpm)'])
        for i, tempo in enumerate(mean_tempo):
            writer.writerow([i, tempo])
    print(f"Результаты сохранены в {output_file}")

def plot_tempo_analysis(times, mean_tempo):
    plt.figure(figsize=(10, 4))
    plt.plot(times, mean_tempo, label='Темп')
    plt.xlabel('Время (с)')
    plt.ylabel('Темп')
    plt.title('Анализ темпа со скользящим окном')
    plt.legend()
    plt.grid(True)
    plt.show()

# Пример использования
audio_file = 'Three Days Grace-Never Too Late-kissvk.com.mp3'
# output_folder = 'data'
# output_file = os.path.join(output_folder, 'sliding_window_results1.csv')
# os.makedirs(output_folder, exist_ok=True)
mean_tempo = sliding_window_tempo_analysis(audio_file)
print_tempo_analysis_results(mean_tempo)
# save_tempo_analysis_results_to_file(mean_tempo, output_file)
times = librosa.times_like(mean_tempo)
plot_tempo_analysis(times, mean_tempo)
