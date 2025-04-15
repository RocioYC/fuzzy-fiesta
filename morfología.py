import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Cargar imagen en escala de grises
img = cv2.imread("letra.jpg", cv2.IMREAD_GRAYSCALE)

# 2. Umbralización binaria
_, img_bin = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY)

# 3. Crear kernel (elemento estructurante)
kernel = np.ones((3, 3), np.uint8)

# 4. Aplicar operaciones morfológicas
erosion = cv2.erode(img_bin, kernel, iterations=1)
dilatacion = cv2.dilate(img_bin, kernel, iterations=1)
apertura = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, kernel)
cierre = cv2.morphologyEx(img_bin, cv2.MORPH_CLOSE, kernel)

# 5. Mostrar resultados
titulos = ["Original", "Erosión", "Dilatación", "Apertura", "Cierre"]
imagenes = [img_bin, erosion, dilatacion, apertura, cierre]

plt.figure(figsize=(12, 6))
for i in range(5):
    plt.subplot(1, 5, i+1)
    plt.imshow(imagenes[i], cmap='gray')
    plt.title(titulos[i])
    plt.axis("off")
plt.tight_layout()
plt.show()

