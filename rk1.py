import numpy as np
import pandas as pd
from scipy.optimize import linprog
from prettytable import PrettyTable
import matplotlib.pyplot as plt


class SimplexMethod:
    column_titles = ['basis', 'B', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6']
    row_titles = ['x4', 'x5', 'x6', 'F(x)']
    a = -5
    b = 5 / 4
    c = 10 / 3
    d = -2 / 3
    e = -8 / 3

    @classmethod
    def calculate_simplex(cls):
        """
        Method for calculation
        """
        a = np.array(
            [
                [2, 1, 1, 1, 0, 0],
                [1, 1, 0, 0, 1, 0],
                [0, 0.5, 2, 0, 0, 1]
            ]
        )
        b = np.array([3, 6, 3])
        c = np.array([-5, -3, -8, 0, 0, 0])

        boundaries = (0, None)
        res = linprog(
            c, A_ub=a, b_ub=b,
            bounds=(boundaries, boundaries, boundaries, boundaries, boundaries, boundaries),
            callback=cls.simplex_callback
        )
        print(f"Optimal value: {res.fun}\n X: {res.x} \n Iterations: {res.nit}")

    @classmethod
    def simplex_callback(cls, xk, **kwargs):
        """
        Just a method for pretty formatting
        """

        phase = kwargs.get('phase')
        if phase == 2:
            current_iteration = kwargs.get('nit', [])

            print(f'Current iteration {current_iteration}')
            table = kwargs.get('tableau', [])
            pivot_change = kwargs.get('pivot')
            try:
                change_row_name = int(pivot_change[0])
                change_col_name = int(pivot_change[1])
                cls.row_titles[change_row_name] = cls.column_titles[change_col_name+1]
            except:
                pass
            t = PrettyTable(cls.column_titles)
            for iterator, row in enumerate(table):
                r = list(row)
                t.add_row([cls.row_titles[iterator]] + r[9:] + r[:6])
            print(t, '\n')

    @classmethod
    def test(cls):
        a = -5
        b = 5 / 4
        c = 10 / 3
        d = -2 / 3
        e = -8 / 3

        # Data for plotting
        x = np.arange(0.1, 0.5, 0.01)

        f1 = -(d + 2 * a * x) / c
        f2 = -(e + c * x) / (2 * b)

        fig, ax = plt.subplots()
        ax.plot(x, f1)
        ax.plot(x, f2)

        ax.set(xlabel='x', ylabel='y',
               title='')
        ax.grid()

        fig.savefig("test.png")
        plt.show()

    @classmethod
    def check(cls):

        a = np.array([[2*cls.a, cls.c], [cls.c, 2 * cls.b]])
        b = np.array([-cls.d, -cls.e])
        x = np.linalg.solve(a, b)
        print(x)

    @classmethod
    def H(cls, x, y):
        return cls.a * x ** 2 + cls.b * y ** 2 + cls.c * x * y + cls.d * x + cls.e * y

    @classmethod
    def find_opt(cls, n, max):
        M = np.empty([n + 1, n + 1]) 

        for i in range(0, n + 1):
            for j in range(0, n + 1):
                M[i][j] = cls.H(i / n, j / n)

        "седловая точка - минимальный элемент строки и одновременно максимальный элемент столбца"

        mins = np.amin(M, axis=1) "axis = 1 - для каждой строки возвращается минимальный элемент - ввиде массива из n элементов (сколько строк в M)"
        mins_pos = np.argmin(M, axis=1) "axis = 1 - для каждой строки возвращается индекс минимального элемента - в виде массива из n элементов (сколько строк в M)"

        max_min = np.amax(mins) "максимальный элемент из минимальных в строках элементов (максмин - минимальный выигрыш А)"
        max_min_pos = np.argmax(mins)  "индекс строки в которой находится максмин"

        y = mins_pos[max_min_pos] / n  "индекс столбца / n"
        x = max_min_pos / n "индекс строки / n"

        if max_min >= max:0

            t = PrettyTable()
            for r in M:
                t.add_row(r)

            print(t)

            print('N: %d,\tx: %.2f,\ty: %.2f,\tmax_min: %.2f' % (n, x, y, max_min))
            return max_min
        else:
            return None

    @classmethod
    def find(cls):
        max = -100
        for i in range(1, 20):
            max = cls.find_opt(i, max)
            if not max:
                break


class SecondLab:
    column_titles = ['Num', 'A choice', 'B choice', 'A winnings', 'B loss', '1/k -v', '1/k v-', 'eps']
    mtx_rows = [
        [13, 2, 4],
        [7, 6, 10],
        [8, 14, 6]
    ]

    mtx_columns = [
        [13, 7, 8],
        [2, 6, 14],
        [4, 10, 6]
    ]

    eps = 0.1

    eps_vals = [11]

    a_strategy = ['x1']
    b_strategy = ['y1']
    a_player_mtx = [mtx_columns[0]]
    b_player_mtx = [mtx_rows[0]]
    k1 = [max(a_player_mtx[0])]
    k2 = [min(b_player_mtx[0])]
