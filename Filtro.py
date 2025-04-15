import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve

# Cargar imagen
img = cv2.imread("letra.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convertir a RGB

# Definir kernels (filtros)
kernels = [
    np.ones((5, 5)) / 25,  # Promedio
    np.array([[-1,-1,-1], [-1, 9,-1], [-1,-1,-1]]),  # Enfoque
    np.array([[0,-1,0], [-1,5,-1], [0,-1,0]]),  # Realce
    np.array([[1,1,1], [1,-7,1], [1,1,1]]),  # Detalle
    np.array([[-1,-1,-1], [-1,8,-1], [-1,-1,-1]])  # Borde
]

# Aplicar y mostrar
plt.figure(figsize=(12, 6))
plt.subplot(2, 3, 1)
plt.imshow(img)
plt.title("Original")
plt.axis('off')

for i, k in enumerate(kernels):
    filtrada = np.stack([convolve(img[:,:,c], k, mode='reflect') for c in range(3)], axis=2)
    plt.subplot(2, 3, i+2)
    plt.imshow(np.clip(filtrada, 0, 255).astype(np.uint8))
    plt.title(f"Filtro {i+1}")
    plt.axis('off')

plt.tight_layout()
plt.show()
