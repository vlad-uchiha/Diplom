import os
import numpy as np
import librosa
import matplotlib.pyplot as plt
import csv

def spectral_analysis(audio_file, n_fft=2048, hop_length=512):
    y, sr = librosa.load(audio_file)
    S = np.abs(librosa.stft(y, n_fft=n_fft, hop_length=hop_length))
    mean_amplitude = np.mean(S, axis=0)
    return mean_amplitude

def print_spectral_analysis_results(mean_amplitude):
    print("Результаты для спектрального анализа")
    for i, amplitude in enumerate(mean_amplitude):
        print(f"Фрейм {i}: Амплитуда = {amplitude}")

def save_spectral_analysis_results_to_file(mean_amplitude, output_file):
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Фрейм', 'Амплитуда'])
        for i, amplitude in enumerate(mean_amplitude):
            writer.writerow([i, amplitude])
    print(f"Результаты сохранены в {output_file}")

def plot_spectral_analysis(times, mean_amplitude):
    plt.figure(figsize=(10, 4))
    plt.plot(times, mean_amplitude, label='Амплитуда')
    plt.xlabel('Время (с)')
    plt.ylabel('Амплитуда')
    plt.title('Спектральный анализ')
    plt.legend()
    plt.grid(True)
    plt.show()

# Пример использования
audio_file = 'Three Days Grace-Never Too Late-kissvk.com.mp3'
# output_folder = 'data'
# output_file = os.path.join(output_folder, 'spectral_analysis_results.csv')
# os.makedirs(output_folder, exist_ok=True)
mean_amplitude = spectral_analysis(audio_file)
print_spectral_analysis_results(mean_amplitude)
#save_spectral_analysis_results_to_file(mean_amplitude, output_file)
times = librosa.times_like(mean_amplitude)
plot_spectral_analysis(times, mean_amplitude)
