import math
import pygame

grafico = []
momento = []
valor = []
list_valorX = []
list_valorY = []
list_norte = []
list_leste = []
list_oeste = []
graus = 0.0

# Inicializando cor
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
gray = (200, 200, 200)
white = (255, 255, 255)
vertical = 600
horizontal = 600
centroY = int(vertical/2)
centroX = int(horizontal/2)

def leitura_lidar(number_points, Lidar, lidar, imagem):
    grafico = []
    momento = []
    valor = []
    list_valorX = []
    list_valorY = []
    list_norte = []
    list_leste = []
    list_oeste = []
    graus = 0.0

    for x in range(number_points):
        valor.append(imagem[x])
        momento.append(x)
        grafico = [valor, momento]
        graus = graus + 2.8125
        rad = (graus * math.pi) / 180

        # Transformando em coordenada cartesiana
        # cosseno -> x
        # seno -> y
        retaX = math.cos(rad) * imagem[x]
        retaX = (retaX * 60) + centroX
        list_valorX.append(retaX)
        retaY = math.sin(rad) * imagem[x]
        retaY = (retaY * 60) + centroY
        list_valorY.append(retaY)
        # print(f"RetaX: {retaY}, RetaY: {retaY}")
    return list_valorX, list_valorY



def desenhar_pontos_2d(Lidar, lidar, surface):
    number_points = Lidar.getNumberOfPoints(lidar)
    grafico = []
    momento = []
    valor = []
    list_valorX = []
    list_valorY = []
    list_norte = []
    list_leste = []
    list_oeste = []
    graus = 0.0

    # Coletando dado polar
    imagem = lidar.getRangeImage()

    for x in range(number_points):
        valor.append(imagem[x])
        momento.append(x)
        grafico = [valor, momento]
        graus = graus + 2.8125
        rad = (graus * math.pi) / 180

        # Transformando em coordenada cartesiana
        # cosseno -> x
        # seno -> y
        retaX = math.cos(rad) * imagem[x]
        retaX = (retaX * 60) + centroX
        list_valorX.append(retaX)
        retaY = math.sin(rad) * imagem[x]
        retaY = (retaY * 60) + centroY
        list_valorY.append(retaY)
        # print(f"RetaX: {retaY}, RetaY: {retaY}")

        # line(surface, color, start_pos, end_pos)
        if valor[x] != float('inf'):
            pygame.draw.line(surface, blue, (centroX, centroY), (list_valorX[x], list_valorY[x]))

        pygame.draw.circle(surface, white, (list_valorX[x], list_valorY[x]), 5)
