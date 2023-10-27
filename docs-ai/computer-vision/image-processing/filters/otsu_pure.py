import numpy as np

def otsu_threshold(img):
    # Passo 1: Histograma
    histogram = [0] * 256
    for pixel in img.flatten():
        histogram[pixel] += 1

    total_pixels = img.size
    current_max, threshold = 0, 0
    total_foreground, total_background = 0, sum([i * histogram[i] for i in range(256)])

    for i in range(256):
        # Passo 2: Testando Limiares
        foreground_pixel_count = histogram[i]
        background_pixel_count = total_pixels - foreground_pixel_count

        total_foreground += i * histogram[i]
        total_background -= i * histogram[i]

        if foreground_pixel_count == 0 or background_pixel_count == 0:
            continue

        # Passo 3: Calculando a Variância
        mean_foreground = total_foreground / foreground_pixel_count
        mean_background = total_background / background_pixel_count
        variance = foreground_pixel_count * background_pixel_count * (mean_foreground - mean_background) ** 2

        # Passo 4: Escolhendo o Melhor Limiar
        if variance > current_max:
            current_max = variance
            threshold = i

    return threshold

# Matriz 4x4 de exemplo
img = np.array([
    [50,  55,  52,  53],
    [60,  65,  62,  63],
    [110, 115, 112, 113],
    [120, 125, 122, 123]
])

# Calculando o limiar usando o método de Otsu
threshold = otsu_threshold(img)
print(f"O limiar ótimo calculado usando o método de Otsu é: {threshold}")
