"""

Lab 5 SPPR
by Senko

"""

import numpy as np

IN = np.array([[85, 60, 40],
               [92, 85, 81],
               [100, 88, 82]])


def Chose(n):
    if n == 1:
        return 'на вечірці всю ніч'
    elif n == 2:
        return 'на вечірці тільки на півночі, а після готуватись до екзамену'
    elif n == 3:
        return 'готуватись всю ніч'
    else:
        return 'роби, що хочеш, я з тобою не розмовляю'


def Laplase(M):
    return np.argmax(np.array([(1 / M.shape[0]) * np.sum(M[i]) for i in range(M.shape[0])])) + 1


def Maxima(M):
    return np.argmax(np.array([np.min(M[i]) for i in range(M.shape[0])]))


def Sevidg(M):
    max = np.array([np.max(M[i]) for i in range(M.shape[0])])
    Max = np.zeros(3)
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            if (max[i] - M[i][j]) > Max[i]:
                Max[i] = max[i] - M[i][j]

    return np.argmax(Max) + 1


def Gurvits(M, a):
    return np.argmax(np.array([a * np.max(M[i]) + (1 - a) * np.min(M[i]) for i in range(M.shape[0])]))


print(f'За критерієм Лапласа - Хенк буде {Chose(Laplase(IN))}')
print(f'За критерієм Вальда(максімінн) - Хенк буде {Chose(Maxima(IN))}')
print(f'За критерієм Севіджа - Хенк буде{Chose(Sevidg(IN))}')

print(f'За критерієм Гурвіца: \n'
      f'При а = 0.25 - Хенк буде {Chose(Gurvits(IN, 0.25))}\n'
      f'При а = 0.5 - Хенк буде {Chose(Gurvits(IN, 0.5))}\n'
      f'При а = 0.75 - Хенк буде {Chose(Gurvits(IN, 0.75))}')
