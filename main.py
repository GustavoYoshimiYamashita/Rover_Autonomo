from controller import *
import movimentacao
import math
import pygame
import lidar_funcoes
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
from datetime import datetime

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

# Adicionando camera
camera = robot.getDevice('camera')
camera.enable(TIME_STEP)

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

now = datetime.now()


while robot.step(TIME_STEP) != -1:


    movimentacao.set_speed(0, motores_velocidade)

    for event in pygame.event.get():
        if event.type == 256:
            pygame.quit()
            exit()

    surface.fill(black)
    pygame.draw.circle(surface, white, (centroX, centroY), 5)

    # Coletando dado polar
    imagem = lidar.getRangeImage()

    list = []
    range1 = lidar.getLayerRangeImage(0)
    range2 = lidar.getLayerRangeImage(1)
    range3 = lidar.getLayerRangeImage(2)
    range4 = lidar.getLayerRangeImage(3)
    range5 = lidar.getLayerRangeImage(4)
    range6 = lidar.getLayerRangeImage(5)
    range7 = lidar.getLayerRangeImage(6)
    range8 = lidar.getLayerRangeImage(7)
    range9 = lidar.getLayerRangeImage(8)
    range10 = lidar.getLayerRangeImage(9)

    numberRange1 = len(range1)
    numberRange2 = len(range2)
    numberRange3 = len(range3)
    numberRange4 = len(range4)
    numberRange5 = len(range5)
    numberRange6 = len(range6)
    numberRange7 = len(range7)
    numberRange8 = len(range8)
    numberRange9 = len(range9)
    numberRange10 = len(range10)

    listaValorXRange1, listaValorYRange1 = lidar_funcoes.leitura_lidar(numberRange1, Lidar, lidar, range1)
    listaValorXRange2, listaValorYRange2 = lidar_funcoes.leitura_lidar(numberRange2, Lidar, lidar, range2)
    listaValorXRange3, listaValorYRange3 = lidar_funcoes.leitura_lidar(numberRange3, Lidar, lidar, range3)
    listaValorXRange4, listaValorYRange4 = lidar_funcoes.leitura_lidar(numberRange4, Lidar, lidar, range4)
    listaValorXRange5, listaValorYRange5 = lidar_funcoes.leitura_lidar(numberRange5, Lidar, lidar, range5)
    listaValorXRange6, listaValorYRange6 = lidar_funcoes.leitura_lidar(numberRange6, Lidar, lidar, range6)
    listaValorXRange7, listaValorYRange7 = lidar_funcoes.leitura_lidar(numberRange7, Lidar, lidar, range7)
    listaValorXRange8, listaValorYRange8 = lidar_funcoes.leitura_lidar(numberRange8, Lidar, lidar, range8)
    listaValorXRange9, listaValorYRange9 = lidar_funcoes.leitura_lidar(numberRange9, Lidar, lidar, range9)
    listaValorXRange10, listaValorYRange10 = lidar_funcoes.leitura_lidar(numberRange10, Lidar, lidar, range10)

    ax = plt.axes(projection='3d')

    # Data for three-dimensional scattered points
    zdata = 128 * [1] + 128 * [2] + 128 * [3] + 128 * [4] + 128 * [5] + 128 * [6] + 128 * [7] + 128 * [8] + 128 * [9] + 128 * [10]
    xdata = listaValorXRange1 + listaValorXRange2 + listaValorXRange3 + listaValorXRange4 + listaValorXRange5 + listaValorXRange6 + listaValorXRange7 + listaValorXRange8 + listaValorXRange9 + listaValorXRange10
    ydata = listaValorYRange1 + listaValorYRange2 + listaValorYRange3 + listaValorYRange4 + listaValorYRange5 + listaValorYRange6 + listaValorYRange7 + listaValorYRange8 + listaValorYRange9 + listaValorYRange10
    ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens')

    if (datetime.now() - now).seconds > 5:
        now = datetime.now()
        plt.show()

    pygame.display.update()
    pygame.display.flip()


