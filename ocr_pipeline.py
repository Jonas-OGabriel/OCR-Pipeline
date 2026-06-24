import numpy as np
import cv2

img = cv2.imread('Imagens/Frentre-Luz.jpg', cv2.IMREAD_GRAYSCALE)

blurred = cv2.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)

thresh = cv2.adaptiveThreshold(
        blurred, 
        255, 
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        11,
        2
)

cv2.imwrite('Resultado_Teste.jpg', thresh)
