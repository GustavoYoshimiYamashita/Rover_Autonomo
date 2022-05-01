from controller import *
import movimentacao
import math
import pygame

TIME_STEP = 10

robot = Robot()

# Definindo as partes de movimentação do robô
back_left_arm = robot.getDevice('BackLeftArm')
back_left_wheel = robot.getDevice('BackLeftWheel')
back_right_arm = robot.getDevice('BackRightArm')
back_right_wheel = robot.getDevice('BackRightWheel')
front_left_arm = robot.getDevice('FrontLeftArm')
front_left_wheel = robot.getDevice('FrontLeftWheel')
front_right_arm = robot.getDevice('FrontRightArm')
front_right_wheel = robot.getDevice('FrontRightWheel')
middle_left_wheel = robot.getDevice('MiddleLeftWheel')
middle_right_wheel = robot.getDevice('MiddleRightWheel')

# Motores Velocidade
motores_velocidade = [back_left_wheel, back_right_wheel, front_left_wheel, front_right_wheel, middle_left_wheel, middle_right_wheel]
# Motores angulo
motores_angulo = [back_left_arm, back_right_arm, front_left_arm, front_right_arm]


# Definindo o giro da roda como infinito
back_left_wheel.setPosition(float('inf'))
back_right_wheel.setPosition(float('inf'))
front_left_wheel.setPosition(float('inf'))
front_right_wheel.setPosition(float('inf'))
middle_left_wheel.setPosition(float('inf'))
middle_right_wheel.setPosition(float('inf'))

# Iniciando o sensor Lidar
lidar = robot.getDevice("lidar")
Lidar.enable(lidar, TIME_STEP)
Lidar.enablePointCloud(lidar)

# Adicioando o sensor compass (Bússola) ao robô
compass = robot.getDevice('compass')
compass.enable(TIME_STEP)
direction = 0
initial_value = True

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

surface = pygame.display.set_mode((horizontal, vertical))

while robot.step(TIME_STEP) != -1:
    movimentacao.set_speed(0.6, motores_velocidade)

    for event in pygame.event.get():
        if event.type == 256:
            pygame.quit()
            exit()

    surface.fill(black)
    pygame.draw.circle(surface, white, (centroX, centroY), 5)
    number_points = Lidar.getNumberOfPoints(lidar)
    grafico = []
    momento = []
    valor = []
    list_valorX = []
    list_valorY = []
    list_norte = []
    list_leste =[]
    list_oeste = []
    graus = 0.0

    for x in range(number_points):

        #Coletando dado polar
        imagem = lidar.getRangeImage()
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
        #print(f"RetaX: {retaY}, RetaY: {retaY}")

        # line(surface, color, start_pos, end_pos)
        if valor[x] != float('inf'):
            pygame.draw.line(surface, blue, (centroX, centroY), (list_valorX[x], list_valorY[x]))

        pygame.draw.circle(surface, white, (list_valorX[x], list_valorY[x]), 5)
    pygame.display.update()
    pygame.display.flip()