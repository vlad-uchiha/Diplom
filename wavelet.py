import os
import numpy as np
import pywt
import librosa
import matplotlib.pyplot as plt
import csv

def wavelet_analysis(audio_file, wavelet='db4', level=5):
    y, sr = librosa.load(audio_file)
    coeffs = pywt.wavedec(y, wavelet, level=level)
    mean_coeffs = [np.mean(level_coeffs) for level_coeffs in coeffs]
    return mean_coeffs

def print_wavelet_analysis_results(mean_coeffs):
    print("Результаты для вейвлет-анализа")
    for i, coeff in enumerate(mean_coeffs):
        print(f"Уровень {i}: Коэффициент = {coeff}")

def save_wavelet_analysis_results_to_file(mean_coeffs, output_file):
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Уровень \t', 'Коэффициент'])
        for i, coeff in enumerate(mean_coeffs):
            writer.writerow([f"{i}\t", coeff])
    print(f"Результаты сохранены в {output_file}")

def plot_wavelet_analysis(levels, mean_coeffs):
    plt.figure(figsize=(10, 4))
    plt.plot(levels, mean_coeffs, label='Коэффициент')
    plt.xlabel('Уровень')
    plt.ylabel('Коэффициент')
    plt.title('Вейвлет-анализ')
    plt.legend()
    plt.grid(True)
    plt.show()

# Пример использования
audio_file = 'Three Days Grace-Never Too Late-kissvk.com.mp3'
# output_folder = 'data'
# output_file = os.path.join(output_folder, 'wavelet_analysis_results.csv')
# os.makedirs(output_folder, exist_ok=True)
mean_coeffs = wavelet_analysis(audio_file)
print_wavelet_analysis_results(mean_coeffs)
# save_wavelet_analysis_results_to_file(mean_coeffs, output_file)
levels = range(len(mean_coeffs))
plot_wavelet_analysis(levels, mean_coeffs)
