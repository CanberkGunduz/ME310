from math import sqrt
# from scipy import integrate
import matplotlib.pyplot as plt
import f, fp


class Integration():

    def __init__(self):
        self.lower_bound, self.upper_bound, self.err_tolerance = -1,1, 0.000001
        self.trapezoidal_results, self.gauss_quadrature_results = [], []
        # self.find_actual_result()
        print("Trapezoidal Rule\n")
        self.trapezoidal_rule()
        print("--------------------\n\nGauss Quadrature Rule\n")
        self.gauss_quadrature()
        self.plot_results()

    # def find_actual_result(self):
    #     self.actual_result = integrate.quad(f.f, self.lower_bound, self.upper_bound)
    #     print("Actual integral result: ", self.actual_result)
    #     print()

    def trapezoidal_rule(self):
        count = 1
        n = 1
        calculated_values = {}
        calculated_values[f"{self.lower_bound}"] = f.f(self.lower_bound)
        calculated_values[f"{self.upper_bound}"] = f.f(self.upper_bound)
        prev_result = 0
        while True:
            current_x = self.lower_bound
            sum = calculated_values[f"{self.lower_bound}"] + calculated_values[f"{self.upper_bound}"]
            integration_result = 0
            step = (self.upper_bound - self.lower_bound) / n
            for i in range(1, n):
                current_x += step
                if current_x == self.upper_bound:
                    break
                if current_x not in calculated_values.keys():
                    calculated_values[f"{current_x}"] = f.f(current_x)
                sum += calculated_values[f"{current_x}"] * 2

            integration_result = step * sum / 2
            current_err = abs((integration_result - prev_result) / integration_result)*100

            self.trapezoidal_results.append(integration_result)

            print("--------------------")
            print("Integration Result:", integration_result)
            print("Number of Segments:", n)
            print("Error:", current_err)
            print("Count:", count)

            if current_err < self.err_tolerance:
                break
            n *= 2
            prev_result = integration_result
            count += 1

    def gauss_quadrature(self):
        weight_1, weight_2, weight_3 = 5 / 9, 8 / 9, 5 / 9
        z_1, z_2, z_3 = -sqrt(3/5),0,sqrt(3/5)
        n=1
        prev_result = 0

        while True:
            current_x = self.lower_bound
            step = (self.upper_bound-self.lower_bound)/n
            integral= 0

            for i in range(n):
                upper_bound, lower_bound = current_x+step*(i+1), current_x+step*i
                height = (upper_bound - lower_bound) / 2
                r_side = (upper_bound + lower_bound) / 2
                point_1,point_2,point_3 = height*z_1+r_side,height*z_2+r_side,height*z_3+r_side
                integral += height*(weight_1*f.f(point_1)+weight_2*f.f(point_2)+weight_3*f.f(point_3))

            current_err = abs((integral - prev_result) / integral)*100
            self.gauss_quadrature_results.append(integral)

            print("--------------------")
            print("Integration Result:", integral)
            print("Number of Segments:", n)
            print("Error:",current_err)

            if current_err < self.err_tolerance:
                break

            n+=1
            prev_result = integral

    def plot_results(self):
        fig, ax = plt.subplots()
        # for i in range(len(self.trapezoidal_results)):
        #     ax.plot(self.trapezoidal_results[i][1], self.trapezoidal_results[i][0])
        #     print(self.trapezoidal_results[i][1],self.trapezoidal_results[i][0])
        ax.plot(range(1,len(self.trapezoidal_results)+1),self.trapezoidal_results,'o-',label = 'Trapezoidal Rule')
        ax.plot(range(1,len(self.gauss_quadrature_results)+1),self.gauss_quadrature_results,'.-',label = 'Gauss Quadrature Rule')
        ax.set_xticks(range(1,len(self.trapezoidal_results)+1))
        plt.title("Numerical Integration")
        plt.xlabel("Iteration Count")
        plt.ylabel("Integral Result")
        ax.grid(linestyle='--', alpha=0.5)
        _ = plt.legend()
        plt.show()


int = Integration()
