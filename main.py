import cv2

# Carregar a imagem
img = cv2.imread('biscoito.jpg')

# Exibir a imagem original
img = cv2.resize(img, (600,600))
filteredImg = cv2.GaussianBlur(img, (9,9), 1)
filteredImg = cv2.medianBlur(filteredImg, 9)
# Converter para escala de cinza e exibir
gray = cv2.cvtColor(filteredImg, cv2.COLOR_BGR2GRAY)
equalized_img = cv2.equalizeHist(gray)


# Binarizar a imagem e exibir
_, binary = cv2.threshold(equalized_img, 179, 255, cv2.THRESH_BINARY)
binary = cv2.bitwise_not(binary)
cv2.imshow('Imagem Binarizada', binary)
cv2.waitKey(0)

# Aplicar filtro Canny para detecção de bordas e exibir
edges = cv2.Canny(binary, 150, 1500)
cv2.imshow('Bordas Detectadas', edges)
cv2.waitKey(0)

# Encontrar contornos na imagem e exibir
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (245, 228, 73), 3)
cv2.imshow('Contornos Detectados', img)
cv2.waitKey(0)

# Verificar se há contornos suficientes para considerar o biscoito quebrado
if len(contours) > 1:
    print("O biscoito está quebrado.")
else:
    print("O biscoito está inteiro.")

# Fechar as janelas
cv2.destroyAllWindows()
