from math import sin, cos, pi, sqrt, atan2

a1 = 350
a2 = 150
a3 = 450
a4 = 300
a5 = 700
b1 = 350
b4 = 220
c1 = 170
be4 = 165 * pi / 180

for th12 in range(0, 361, 1):
    th12 = th12 * pi / 180

    k1 = a2 * cos(th12) + a1
    k2 = a2 * sin(th12) - b1
    k3 = ((a4 ** 2 - a3 ** 2 - k1 ** 2 - k2 ** 2) / (2 * a3))

    t13_1 = ((k2 + sqrt(k2 ** 2 + k1 ** 2 - k3 ** 2)) / (k1 + k3))
    t13_2 = ((k2 - sqrt(k2 ** 2 + k1 ** 2 - k3 ** 2)) / (k1 + k3))

    th13_1 = atan2(2 * t13_1, 1 - t13_1 ** 2)
    th13_2 = atan2(2 * t13_2, 1 - t13_2 ** 2)

    th14_1 = atan2(a3 * sin(th13_1) + k2, a3 * cos(th13_1) + k1)
    th14_2 = atan2(a3 * sin(th13_2) + k2, a3 * cos(th13_2) + k1)

    k4_1 = b4 * cos(th14_1 - be4) + c1
    k4_2 = b4 * cos(th14_2 - be4) + c1
    k5_1 = b4 * sin(th14_1 - be4) + b1
    k5_2 = b4 * sin(th14_2 - be4) + b1

    A = 1
    B_1 = 2 * k5_1
    B_2 = 2 * k5_2
    C_1 = k5_1 ** 2 + k4_1 ** 2 - a5 ** 2
    C_2 = k5_2 ** 2 + k4_2 ** 2 - a5 ** 2

    s16_1 = ((-B_1 + sqrt(B_1 ** 2 - 4 * A * C_1)) / (2 * A))
    s16_2 = ((-B_1 - sqrt(B_1 ** 2 - 4 * A * C_1)) / (2 * A))
    s16_3 = ((-B_2 + sqrt(B_2 ** 2 - 4 * A * C_2)) / (2 * A))
    s16_4 = ((-B_2 - sqrt(B_2 ** 2 - 4 * A * C_2)) / (2 * A))

    th15_1 = atan2(s16_1 + k5_1, k4_1)
    th15_2 = atan2(s16_2 + k5_1, k4_1)
    th15_3 = atan2(s16_3 + k5_2, k4_2)
    th15_4 = atan2(s16_4 + k5_2, k4_2)

    if th14_2 < 0:
        th14_2 = th14_2 + 2 * pi
    if th14_1 < 0:
        th14_1 = th14_1 + 2 * pi

    if th13_1 < 0:
        th13_1 = th13_1 + 2 * pi
    if th13_2 < 0:
        th13_2 = th13_2 + 2 * pi

    if th15_1 < 0:
        th15_1 = th15_1 + 2 * pi
    if th15_2 < 0:
        th15_2 = th15_2 + 2 * pi
    if th15_3 < 0:
        th15_3 = th15_3 + 2 * pi
    if th15_4 < 0:
        th15_4 = th15_4 + 2 * pi

    print(f"For theta12 = {round(th12 * 180 / pi, 4)}°:"
          f"\nTheta13_1 = {round(th13_1 * 180 / pi, 4)}°"
          f"\nTheta13_2 = {round(th13_2 * 180 / pi, 4)}°"
          f"\nTheta14_1 = {round(th14_1 * 180 / pi, 4)}°"
          f"\nTheta14_2 = {round(th14_2 * 180 / pi, 4)}°"
          f"\nTheta15_1 = {round(th15_1 * 180 / pi, 4)}°"
          f"\nTheta15_2 = {round(th15_2 * 180 / pi, 4)}°"
          f"\nTheta15_3 = {round(th15_3 * 180 / pi, 4)}°"
          f"\nTheta15_4 = {round(th15_4 * 180 / pi, 4)}°"
          f"\ns16_1 = {round(s16_1, 3)}cm"
          f"\ns16_2 = {round(s16_2, 3)}cm"
          f"\ns16_3 = {round(s16_3, 3)}cm"
          f"\ns16_4 = {round(s16_4, 3)}cm"
          f"\n_______________________") 