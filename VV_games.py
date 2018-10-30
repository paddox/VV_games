A = -3
B = 3/2
C = 18/5
D = -18/50
E = -72/25

import BrownRobinson as br

def H(x,y):
    return A*x**2 + B*y**2 + C*x*y + D*x + E*y

def find_opt(N):
    matrix = []
    for i in range(N):
        matrix.append([H(i/N, j/N) for j in range(N)])
    game = br.BrownRobinson(matrix, 0.1, 100)
    x = game['answer'][0]
    y = game['answer'][1]
    win = game['answer'][3]
    opt_x = 0
    opt_y = 0
    delta = 1
    for i in range(N):
        for j in range(N):
            print(matrix[i])
            if (abs(matrix[i][j] - win) < delta):
                opt_x = i
                opt_y = j
                delta = abs(matrix[i][j] - win)
    print(opt_x/N, opt_y/N, matrix[opt_x][opt_y])
    print('x: %.2f,\ty: %.2f,\tmax_min: %.2f' % (opt_x/N, opt_y/N, win))
    #print('N: %d, решение: %.2f' % (N, win))


if __name__ == "__main__":
    print('-----------------------------------------')
    print(H(159/430, 111/215))
    for i in range(3, 15):
        find_opt(i)
    '''
    for i in range(1, 20):
        find_opt(i)
    '''
