import math

class Project2:

    def __init__(self):
        self.numOfParticles = int(input("Enter the number of particles: "))
        self.timeInstant = float(input("Enter the time instant: "))
        self.terminationTolerance = float(input("Enter the tolerance to terminate: "))
        self.maxIterNum = int(input("Enter the maximum number of iterations to terminate: "))
        print("______________________________")

        self.GaussElimination(self.numOfParticles,self.timeInstant)
        self.GaussSiedel(self.numOfParticles,self.timeInstant)

        # Below two functions calls were made to acquire data points for different matrix sizes and time instants
        # self.sameTime()
        # self.sameNum()

    def MatrixFormer(self,n,t):
        # Ax=b
        b = [0 if 0 < i < n - 1 else 1 if i == n - 1 else self.f(t) for i in range(n)]

        # World's most absurd list comprehension xd
        A = [[-2 if i == j else 1 if i == j + 1 else 1 if i == j - 1 else 0 for j
              in range(n)] if 0 < i < n - 1 else [1 if j == 0 else
            0 for j in range(n)] if i == 0 else [1 if j == n - 1 else
            0 for j in range(n)] for i in range(n)]

        return A, b

    def GaussElimination(self,n,t):
        # define the matrix of coefficients, define the vector of constants
        A,b = self.MatrixFormer(n,t)

        # perform Gauss elimination
        for i in range(n):
            # pivot on the diagonal element
            pivot = A[i][i]
            for j in range(i + 1, n):
                # perform row operations to eliminate the off-diagonal elements
                scale = A[j][i] / pivot
                for k in range(i, n):
                    A[j][k] -= scale * A[i][k]
                b[j] -= scale * b[i]

        # solve for the unknowns using back-substitution
        x = [0 for i in range(n)]
        for i in range(n - 1, -1, -1):
            x[i] = b[i]
            for j in range(i + 1, n):
                x[i] -= A[i][j] * x[j]
            x[i] /= A[i][i]

        # print the solution
        print(f"Gauss Elimination solution for time = {t} and matrix size = {n} is:"
              f"\n{x}\n______________________________")
        return x

    def GaussSiedel(self,n,t):

        # define the matrix of coefficients, define the vector of constants
        A, b = self.MatrixFormer(n,t)

        # define the initial guess for the solution
        x = [0 for i in range(n)]

        # define the convergence tolerance
        tol = self.terminationTolerance

        # define the maximum number of iterations
        max_iter = self.maxIterNum

        for k in range(max_iter):
            # store the previous solution
            x_prev = x.copy()

            # perform the Gauss-Seidel method
            for i in range(n):
                s = 0
                for j in range(n):
                    if i != j:
                        s += A[i][j] * x[j]
                x[i] = (b[i] - s) / A[i][i]

            # check for convergence
            if max(abs(x[i] - x_prev[i]) for i in range(n)) < tol:
                break
        # print the solution
        print(f"Gauss-Seidel solution for time = {t} and matrix size = {n} is:"
              f"\n{x}\n______________________________")
        return x

    def f(self,t):
        return 0.25 * math.sin(math.pi * t)

    # Below two functions were used to acquire data for plots

    # def sameTime(self):
    #     solnElm=[]
    #     solnSeid=[]
    #     for i in range(1,11):
    #         solnElm.append(self.GaussElimination(i, self.timeInstant))
    #         solnSeid.append(self.GaussSiedel(i, self.timeInstant))
    #
    #     # print(f"Gauss Elimination for same Time instant: {solnElm}")
    #     # print(f"Gauss Seidel for same Time instant: {solnSeid}\n_________________________")

    # def sameNum(self):
    #     solnElm=[]
    #     solnSeid=[]
    #     for t in range(11):
    #         solnElm.append(self.GaussElimination(self.numOfParticles,t/10))
    #         solnSeid.append(self.GaussSiedel(self.numOfParticles,t/10))
    #
    #     # print(f"Gauss Elimination for same Matrix Size: {solnElm}")
    #     # print(f"Gauss Seidel for same Matrix Size: {solnSeid}\n_________________________")



a = Project2()
