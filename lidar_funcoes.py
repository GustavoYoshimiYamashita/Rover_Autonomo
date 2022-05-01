import math

grafico = []
momento = []
valor = []
list_valorX = []
list_valorY = []
list_norte = []
list_leste = []
list_oeste = []
graus = 0.0

vertical = 600
horizontal = 600
centroY = int(vertical / 2)
centroX = int(horizontal / 2)



def leitura(lidar, number_points):
    graus = 0
    for x in range(number_points):

        # Coletando dado polar
        imagem = lidar.getRangeImage()
        # if imagem[x] != float('inf'):
        #    print(imagem[x])

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

    return list_valorX, list_valorY

