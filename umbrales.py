import cv2
import matplotlib.pyplot as plt

# Cargar imagen en escala de grises
img = cv2.imread("letra.jpg", 0)

# Umbral binario (fijo)
_, binaria = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Umbral adaptativo gaussiano
adapt = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 11, 2)

# Mostrar resultados
plt.subplot(1, 3, 1); plt.imshow(img, cmap='gray'); plt.title("Original"); plt.axis('off')
plt.subplot(1, 3, 2); plt.imshow(binaria, cmap='gray'); plt.title("Binaria"); plt.axis('off')
plt.subplot(1, 3, 3); plt.imshow(adapt, cmap='gray'); plt.title("Adaptativa"); plt.axis('off')
plt.tight_layout(); plt.show()
