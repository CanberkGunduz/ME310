import numpy as np
import sympy
import numpy


class Abc:
    def __init__(self):
        self.input_to_array()
        # self.x_input = float(input("x: "))
        print(self.x_values)
        print(self.y_values)
        self.create_variables()
        self.subst_initially_known_values()
        self.form_b_matrix()
        self.form_C_matrix()
        self.form_A_matrix()
        self.convert_to_np()
        self.solve_np()
        # print("------")
        # self.abc()

    def input_to_array(self):
        with open("input.txt", "r") as input:
            lines = input.readlines()
            self.x_values = [[float(x)] for x in lines[0].rstrip("\n").split(" ")]
            self.y_values = [[float(y)] for y in lines[1].rstrip("\n").split(" ")]
        self.n = len(self.x_values)

    def create_variables(self):
        self.S = {f"s_{i},{j}": 1 for i in range(1, self.n + 1) for j in range(1, 6)}
        print(self.S)

    def form_C_matrix(self):
        self.C = [[[f"s_{i},{j}"] for i in range(1,self.n+1)] for j in range(1,6)]
        # print(self.C)
        self.C.append([[f"s_{i},{1}"] for i in range(2,self.n+1)])
        self.C[5].append(0)
        self.C.append([[f"s_{i},{2}"] for i in range(2, self.n + 1)])
        self.C[6].append(0)
        self.C.append([[f"s_{i},{3}"] for i in range(2, self.n + 1)])
        self.C[7].append(0)
        self.C.append([[f"s_{i},{4}"] for i in range(2, self.n + 1)])
        self.C[8].append(0)
        # self.C=[]
        # for i in range(1,self.n+1):
        #     for j in range(1,6):
        #         self.C = self.S[f"s_{i},{j}"]

        print(self.C)

    def form_A_matrix(self):
        self.A = []

        #interior
        self.A.extend([[(self.x_values[i][0]-self.x_values[i-1][0])**(j-1) for j in range(1,6)] for i in range(1,self.n)])
        for k in range(self.n-1): self.A[k].extend([-1,0,0,0])
        #1st deriv
        self.A.extend([[(j-1)*(self.x_values[i][0] - self.x_values[i - 1][0]) ** (j - 2) for j in range(1, 6)] for i in range(1, self.n )])
        for k in range(self.n-1,self.n*2-2): self.A[k].extend([0,-1,0,0])
        #2nd deriv
        self.A.extend(
            [[(j - 1) * (j - 2) / 2 * (self.x_values[i][0] - self.x_values[i - 1][0]) ** (j - 3) for j in range(1, 6)] for i in range(1, self.n )])
        print(self.A)

        for k in range(self.n*2-2,self.n*3-3):self.A[k].extend([0,0,-1,0])
        #3rd deriv
        self.A.extend(
            [[(j - 1) * (j - 2) *(j-3) / 6 * (self.x_values[i][0] - self.x_values[i - 1][0]) ** (j - 4) for j in range(1, 6)] for i in
             range(1, self.n)])
        for k in range(self.n*3-3,self.n*4-4):self.A[k].extend([0,0,0,-1])
        #end point
        self.A.append([(self.x_values[self.n-1][0]-self.x_values[self.n-2][0])**(j-1) for j in range(1,6)])
        self.A[self.n*4-4].extend([0, 0, 0, 0])
        print(self.A)

    def subst_initially_known_values(self):
        self.S["s_1,1"] = self.y_values[0][0]
        self.S["s_1,3"], self.S["s_1,4"], self.S[f"s_{self.n},3"] = 0, 0, 0


    def form_b_matrix(self):
        self.b = [[self.y_values[i][0] if i == j else 0 for j in range(self.n)] for i in range(self.n+4)]
        print(self.b)

    def convert_to_np(self):
        self.np_b = np.array(self.b)
        self.np_A = np.array(self.A)

    def solve_np(self):
        x = np.linalg.solve(self.np_A,self.np_b)
        print("----------------------------------------------------------------------\n\n")
        print(x)


a = Abc()