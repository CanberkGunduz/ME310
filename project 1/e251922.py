import f as func
import fp as funcp


class Abc:

    def __init__(self):
        try:
            self.array = []
            self.text_to_array()

            self._lbound = float(self.array[0])
            self._ubound = float(self.array[1])
            self._errtolerance = float(self.array[2])
            self._iterlimit = int(self.array[3])

            self.false_position()
            self.bisection()
            self.polynomial()
            self.newton()
            self.secant()
        except Exception:
            self.unknown_error()

    def text_to_array(self):
        try:
            with open("input.txt", "r") as file:
                [self.array.append(line.rstrip("\n")) for line in file]
            if self.array.__len__() != 4: raise Exception
        except Exception:
            self.unknown_error()


    def false_position(self):
        lbound, ubound = self._lbound, self._ubound
        prev_x_root, x_root, approx_perc_error = 1.0, 1.0, 100.0
        with open("output_falseposition.txt", "w") as file:
            try:
                self.root_exists()  # can be done in init
                for iteration_num in range(1, self._iterlimit + 1):
                    # algorithm here
                    x_root = ubound - (func.f(ubound) * (lbound - ubound)) \
                             / (func.f(lbound) - func.f(ubound))

                    lbound, ubound = self.bracket(lbound, x_root, ubound)

                    if iteration_num > 1:
                        approx_perc_error = abs((x_root - prev_x_root) / x_root) * 100

                    prev_x_root = x_root

                    file.write(f"{iteration_num} {round(x_root, 6)} {round(func.f(x_root), 6)} "
                               f"{approx_perc_error if iteration_num != 1 else '----'}\n")
                    if approx_perc_error < self._errtolerance:
                        file.write("Error tolerance is met")
                        self.method_summary("False Position Method",x_root,approx_perc_error,iteration_num)
                        break
            except NoRootsInBracket:
                file.write("No roots in given bracket")
            except ExactRootFound:
                file.write("Exact root found")
            except ZeroDivisionError:
                file.write("Division by zero occurred")
            except Exception:
                file.write("An error occurred, terminating process")

    def bisection(self):
        lbound, ubound = self._lbound, self._ubound
        prev_x_root, x_root, approx_perc_error = 1.0, 1.0, 100
        with open("output_bisection.txt", "w") as file:
            try:
                self.root_exists()
                for iteration_num in range(1, self._iterlimit + 1):
                    # algorithm here
                    x_root = (lbound + ubound) / 2

                    lbound, ubound = self.bracket(lbound, x_root, ubound)

                    if iteration_num > 1:
                        approx_perc_error = abs((x_root - prev_x_root) / x_root) * 100

                    prev_x_root = x_root

                    file.write(f"{iteration_num} {round(x_root, 6)} {round(func.f(x_root), 6)} "
                               f"{approx_perc_error if iteration_num != 1 else '----'}\n")
                    if approx_perc_error < self._errtolerance:
                        file.write("Error tolerance is met")
                        self.method_summary("Bisection Method", x_root, approx_perc_error, iteration_num)
                        break
            except NoRootsInBracket:
                file.write("No roots in given bracket")
            except ExactRootFound:
                file.write("Exact root found")
            except ZeroDivisionError:
                file.write("Division by zero occurred")
            except Exception:
                file.write("An error occurred, terminating process")

    def polynomial(self):
        lbound, ubound = self._lbound, self._ubound
        prev_x_root, x_root, approx_perc_error = 0.0, 0.0, 0.0
        with open("output_polynomial.txt", "w") as file:
            try:
                self.root_exists()
                for iteration_num in range(1, self._iterlimit + 1):
                    # algorithm here
                    x_root = (lbound + ubound) / 2

                    a = (func.f(lbound) - func.f(x_root)) / ((lbound - x_root) * (lbound - ubound)) + \
                        (func.f(x_root) - func.f(ubound)) / ((ubound - x_root) * (lbound - ubound))

                    b = (((func.f(lbound) - func.f(x_root)) * (x_root - ubound))
                         / ((lbound - x_root) * (lbound - ubound))) - \
                        (((func.f(x_root) - func.f(ubound)) * (lbound - x_root))
                         / ((ubound - x_root) * (lbound - ubound)))

                    c = func.f(x_root)

                    x_root = x_root - (2 * c) / (b + ((abs(b) // b) * (b ** 2 - 4 * a * c) ** 0.5))

                    lbound, ubound = self.bracket(lbound, x_root, ubound)

                    approx_perc_error = abs((x_root - prev_x_root) / x_root) * 100

                    prev_x_root = x_root

                    file.write(f"{iteration_num} {round(x_root, 6)} {round(func.f(x_root), 6)} "
                               f"{approx_perc_error if iteration_num != 1 else '----'}\n")
                    if approx_perc_error < self._errtolerance:
                        file.write("Error tolerance is met")
                        self.method_summary("Polynomial Method", x_root, approx_perc_error, iteration_num)
                        break
            except NoRootsInBracket:
                file.write("No roots in given bracket")
            except ZeroDivisionError:
                file.write("Division by zero occurred")
            except Exception:
                file.write("An error occurred, terminating process")

    def newton(self):
        lbound, ubound = self._lbound, self._ubound
        # prev_x_root = (lbound + ubound) / 2
        prev_x_root = 0.3
        x_root, approx_perc_error = 1.0, 0.0
        with open("output_newton.txt", "w") as file:
            try:
                for iteration_num in range(1, self._iterlimit + 1):
                    # algorithm here
                    x_root = prev_x_root - func.f(prev_x_root) / funcp.fp(prev_x_root)
                    approx_perc_error = abs((x_root - prev_x_root) / x_root) * 100
                    prev_x_root = x_root

                    file.write(f"{iteration_num} {round(x_root, 6)} {round(func.f(x_root), 6)} "
                               f"{approx_perc_error if iteration_num != 1 else '----'}\n")
                    if approx_perc_error < self._errtolerance:
                        file.write("Error tolerance is met")
                        self.method_summary("Newton Method", x_root, approx_perc_error, iteration_num)
                        break
            except NoRootsInBracket:
                file.write("No roots in given bracket")
            except ZeroDivisionError:
                file.write("Division by zero occurred")
            except Exception:
                file.write("An error occurred, terminating process")

    def secant(self):
        lbound, ubound = self._lbound, self._ubound
        prev_x_root = (lbound + ubound) / 2
        x_init = prev_x_root-0.01
        x_root, approx_perc_error = 0.0, 0.0
        with open("output_secant.txt", "w") as file:
            try:
                for iteration_num in range(1, self._iterlimit + 1):
                    # algorithm here
                    funcprime = (func.f(x_init)-func.f(prev_x_root))/(x_init-prev_x_root)
                    x_root = prev_x_root - func.f(prev_x_root) / funcprime
                    approx_perc_error = abs((x_root - prev_x_root) / x_root) * 100
                    prev_x_root = x_root

                    file.write(f"{iteration_num} {round(x_root, 6)} {round(func.f(x_root), 6)} "
                               f"{approx_perc_error if iteration_num != 1 else '----'}\n")
                    if approx_perc_error < self._errtolerance:
                        file.write("Error tolerance is met")
                        self.method_summary("Secant Method", x_root, approx_perc_error, iteration_num)
                        break
            except NoRootsInBracket:
                file.write("No roots in given bracket")
            except ZeroDivisionError:
                file.write("Division by zero occurred")
            except Exception:
                file.write("An error occurred, terminating process")

    def bracket(self, x1, x2, x3):
        prod = func.f(x1) * func.f(x2)
        prod2 = func.f(x2) * func.f(x3)
        if prod < 0:
            return x1, x2
        elif prod2 < 0:
            return x2, x3
        elif prod == 0 or prod2 == 0:
            raise ExactRootFound("Exact root found")
        else:
            raise NoRootsInBracket("There are no roots in this bracket")

    def root_exists(self):
        if func.f(self._lbound) * func.f(self._ubound) >= 0:
            raise NoRootsInBracket

    def method_summary(self,method_name,x_root,error,iteration):
        print(f"{method_name}: \nLast estimate of the root: {round(x_root, 6)} \n"
              f"Approximate percent relative error: {error} \n"
              f"Total number of iterations: {iteration} \n"
              f"Function value at the calculated root: {round(func.f(x_root), 6)}\n\n")

    def unknown_error(self):
        with open("output_falseposition.txt", "w") as f1:
            f1.write("Error reading input values please provide correctly formatted values")
        with open("output_bisection.txt", "w") as f2:
            f2.write("Error reading input values please provide correctly formatted values")
        with open("output_polynomial.txt", "w") as f3:
            f3.write("Error reading input values please provide correctly formatted values")
        with open("output_newton.txt", "w") as f4:
            f4.write("Error reading input values please provide correctly formatted values")
        with open("output_secant.txt", "w") as f5:
            f5.write("Error reading input values please provide correctly formatted values")
        quit()

class NoRootsInBracket(Exception):
    pass

class ExactRootFound(Exception):
    pass


a = Abc()
