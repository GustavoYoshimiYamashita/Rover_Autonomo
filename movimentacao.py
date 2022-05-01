def set_steering_angle(wheel_angle, motores_angulo):
    back_left_angle = wheel_angle[0]
    back_right_angle = wheel_angle[1]
    front_left_angle = wheel_angle[2]
    front_right_angle = wheel_angle[3]

    motores_angulo[0].setPosition(back_left_angle)
    motores_angulo[1].setPosition(back_right_angle)
    motores_angulo[2].setPosition(front_left_angle)
    motores_angulo[3].setPosition(front_right_angle)

def set_speed(velocity, motores_velocidade):
    motores_velocidade[0].setVelocity(velocity)
    motores_velocidade[1].setVelocity(velocity)
    motores_velocidade[2].setVelocity(velocity)
    motores_velocidade[3].setVelocity(velocity)
    motores_velocidade[4].setVelocity(velocity)
    motores_velocidade[5].setVelocity(velocity)