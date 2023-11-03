from math import cos, sin, sqrt, atan2, pi
# import openpyxl

# defining constants
a1, a2, a3, a4, a5, b1, b4, c1, beta4 = 350, 150, 450, 300, 700, 350, 220, 170, 165 * pi / 180
w12 = 2
soln = []
for theta12 in range(0, 361):
    theta12 = theta12 * pi / 180

    # defining Freudenstein's Equations Coefficients
    K1 = a2 * cos(theta12) + a1
    K2 = a2 * sin(theta12) - b1
    K3 = (a4 ** 2 - a3 ** 2 - K1 ** 2 - K2 ** 2) / (2 * a3)

    # for loop to cover all closures
    for i in range(-1, 2, 2):
        t13 = (K2 + i * sqrt(K2 ** 2 + K1 ** 2 - K3 ** 2)) / (K1 + K3)
        theta13 = atan2(2 * t13, 1 - t13 ** 2)
        theta14 = atan2(a3 * sin(theta13) + K2, a3 * cos(theta13) + K1)

        # defining Freudenstein's Equations Coefficients
        K4 = b4 * cos(theta14 - beta4) + c1
        K5 = b4 * sin(theta14 - beta4) + b1

        # defining quadratic coefficients
        A = 1
        B = 2 * K5
        C = K5 ** 2 + K4 ** 2 - a5 ** 2

        # for loop to cover all closures
        for j in range(-1, 2, 2):
            s16 = (-B + j * sqrt(B ** 2 - 4 * A * C)) / (2 * A)
            theta15 = atan2(s16 + K5, K4)

            # below are checks for negative values so the values don't jump 2pi e.g. 179° -> -181°
            if theta12 < 0:
                theta12 += 2 * pi
            if theta13 < 0:
                theta13 += 2 * pi
            if theta14 < 0:
                theta14 += 2 * pi
            if theta15 < 0:
                theta15 += 2 * pi

            print(f"For theta12 = {round(theta12 * 180 / pi, 4)}° and i={i},j={j}:"
                  f"\nTheta13 = {round(theta13 * 180 / pi, 4)}°\nTheta14 = {round(theta14 * 180 / pi, 4)}°\n"
                  f"Theta15 = {round(theta15 * 180 / pi, 4)}°\ns16 = {round(s16, 3)}cm\n_______________________")

            if i == 1 and j == 1:
                w13 = (a2 * sin(theta14 - theta12)) / (a3 * sin(theta13 - theta14)) * w12
                w14 = (a2 * sin(theta13 - theta12)) / (a4 * sin(theta13 - theta14)) * w12
                w15 = w14 * (b4 * sin(theta14 - beta4)) / (a5 * sin(theta15))
                v16 = w15 * a5 * cos(theta15) - w14 * b4 * cos(theta14 - beta4)

                k1 = w14 ** 2 * a4 * cos(theta14) - w12 ** 2 * a2 * cos(theta12) - w13 ** 2 * a3 * cos(theta13)
                k2 = w14 ** 2 * a4 * sin(theta14) - w12 ** 2 * a2 * sin(theta12) - w13 ** 2 * a3 * sin(theta13)

                alpha13 = (k1 * cos(theta14) + k2 * sin(theta14)) / (a3 * sin(theta13 - theta14))
                alpha14 = (k2 * sin(theta13) + k1 * cos(theta13)) / (a4 * sin(theta13 - theta14))

                k3 = w14 ** 2 * b4 * cos(theta14 - beta4) - w15 ** 2 * a5 * cos(theta15)
                k4 = -w15 ** 2 * a5 * sin(theta15) - alpha14 * b4 * cos(theta14 - beta4)

                alpha15 = (k2 * sin(theta13) + k1 * cos(theta13)) / (a4 * sin(theta13 - theta14)) \
                          * (b4 * sin(theta14 - beta4)) / (a5 * sin(theta15)) + (k3) / (a5 * sin(theta15))
                acc16 = w14 ** 2 * b4 * sin(theta14 - beta4) + (
                            (k2 * sin(theta13) + k1 * cos(theta13)) / (a4 * sin(theta13 - theta14)) \
                            * (b4 * sin(theta14 - beta4)) / (sin(theta15)) + (k3) / (sin(theta15))) * cos(theta15) + k4

                soln.append([(theta12, i, j), (theta13, theta14, theta15, s16),
                             (w13, w14, w15, v16), (alpha13, alpha14, alpha15, acc16)])

# # This below part is to plot the graph in Excel with ease.
#
# # Create a new Excel file
# wb = openpyxl.Workbook()
# # Create a new sheet
# sheet = wb.active
# # Loop over the values and write them to cells
# for i, value in enumerate(soln):
#     # position analysis data
#     sheet.cell(row=i + 2, column=1).value = round(value[0][0] * 180 / pi, 4)
#     sheet.cell(row=i + 2, column=2).value = round(value[1][0] * 180 / pi, 4)
#     sheet.cell(row=i + 2, column=3).value = round(value[1][1] * 180 / pi, 4)
#     sheet.cell(row=i + 2, column=4).value = round(value[1][2] * 180 / pi, 4)
#     sheet.cell(row=i + 2, column=5).value = round(value[1][3], 4)
#     # velocity analysis data
#     sheet.cell(row=i + 2, column=6).value = round(value[2][0], 4)
#     sheet.cell(row=i + 2, column=7).value = round(value[2][1], 4)
#     sheet.cell(row=i + 2, column=8).value = round(value[2][2], 4)
#     sheet.cell(row=i + 2, column=9).value = round(value[2][3], 4)
#     # acceleration analysis data
#     sheet.cell(row=i + 2, column=10).value = round(value[3][0], 4)
#     sheet.cell(row=i + 2, column=11).value = round(value[3][1], 4)
#     sheet.cell(row=i + 2, column=12).value = round(value[3][2], 4)
#     sheet.cell(row=i + 2, column=13).value = round(value[3][3], 4)
#
# Save the file
# wb.save("project2_ed2.xlsx")
