A = -3
B = 3/2
C = 18/5
D = -18/50
E = -72/25

import BrownRobinson as br
import numpy as np

def H(x,y):
    return A*x**2 + B*y**2 + C*x*y + D*x + E*y

def find_opt(N):
    matrix = []
    for i in range(N+1):
        matrix.append([H(i/N, j/N) for j in range(N+1)])
    matrix = np.array(matrix)
    min_cost = np.max(matrix.min(axis=1))
    min_cost_y = np.argmax(matrix.min(axis=1))
    min_cost_x = matrix[min_cost_y].argmin()
    max_cost = np.min(matrix.max(axis=0))
    max_cost_x = np.argmin(matrix.max(axis=0))
    max_cost_y = matrix.argmax(axis=0)[max_cost_x]
    np.set_printoptions(precision=3, linewidth=np.nan)
    print(matrix)
    #print("max={0:.3f} min={1:.3f} max_x={2} max_y={3} min_x={4} min_y={5}".format(max_cost, min_cost, max_cost_x, max_cost_y, min_cost_x, min_cost_y))
    if min_cost == max_cost:
        print("x={1:.3f} y={0:.3f} H={2:.3f}".format(min_cost_x/N, min_cost_y/N, min_cost))
    else:
        game = br.BrownRobinson(matrix, 0.01, 1000)
        x = game['answer'][0]
        y = game['answer'][1]
        cost = game['answer'][3]
        opt_x = 0
        opt_y = 0
        delta = 10000
        for i in range(N):
            for j in range(N):
                if (abs(matrix[i][j] - cost) < delta):
                    opt_y = i
                    opt_x = j
                    delta = abs(matrix[i][j] - cost)
        print("x={1:.3f} y={0:.3f} H={2:.3f}".format(opt_x/N, opt_y/N, matrix[opt_y][opt_x]))

if __name__ == "__main__":
    print('-----------------------------------------')
    print("Аналитическое решение:\nx={0:.3f} y={1:.3f} H={2:.3f}\n".format(159/430, 111/215, H(159/430, 111/215)))
    for i in range(3, 11):
        print("N={0}".format(i))
        find_opt(i)
        print("\n")

