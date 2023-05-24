import numpy as np

A_matrix = np.array([[1, 2, 0.5],
                     [0.5, 1, 0.2],
                     [2, 5, 1]])

Al_matrix = np.array([[1, 0.333, 0.5],
                      [3, 1, 0.333],
                      [2, 3, 1]])

Ac_matrix = np.array([[1, 2, 2],
                      [0.5, 1, 1],
                      [0.5, 1, 1]])

Ar_matrix = np.array([[1, 1, 9],
                      [1, 1, 8],
                      [0.111, 0.125, 1]])

A_matrix_sum = A_matrix.sum(axis=0)
Al_matrix_sum = Al_matrix.sum(axis=0)
Ac_matrix_sum = Ac_matrix.sum(axis=0)
Ar_matrix_sum = Ar_matrix.sum(axis=0)
NA = []
for i in range(A_matrix_sum.shape[0]):
    for j in range(A_matrix_sum.shape[0]):
        A_matrix[:, i] = i[j] / A_matrix_sum[j]
        NA.append(A_matrix)

NA = [[A_matrix[:, i] for i in range(A_matrix_sum.shape[0])][j] / A_matrix_sum[j] for j in range(A_matrix_sum.shape[0])]
NAl = [[Al_matrix[:, i] for i in range(Al_matrix_sum.shape[0])][j] / Al_matrix_sum[j] for j in
       range(Al_matrix_sum.shape[0])]
NAc = [[Ac_matrix[:, i] for i in range(Ac_matrix_sum.shape[0])][j] / Ac_matrix_sum[j] for j in
       range(Ac_matrix_sum.shape[0])]
NAr = [[Ac_matrix[:, i] for i in range(Ar_matrix_sum.shape[0])][j] / Ar_matrix_sum[j] for j in
       range(Ar_matrix_sum.shape[0])]
avr_NA = np.mean(NA, axis=0).reshape(3, 1)
avr_NAl = np.mean(NAl, axis=0).reshape(3, 1)
avr_NAc = np.mean(NAc, axis=0).reshape(3, 1)
avr_NAr = np.mean(NAr, axis=0).reshape(3, 1)


def get_stat(BaseM, w):
    n = 3
    BaseMw = np.dot(BaseM, w)
    Base_sum = BaseMw.sum()
    CI = (Base_sum - n) / (n - 1)
    RI = (1.98 * (n - 2)) / n
    CR = CI / RI

    return CI, RI, CR


print("Для матриці: А ")
if get_stat(A_matrix, avr_NA)[0] < 0.1:
    print(f'CI = {get_stat(A_matrix, avr_NA)[0]} < 0.1 - рівень непогодженості є прийнятним ')
else:
    print(f'CI = {get_stat(A_matrix, avr_NA)[0]} < 0.1 - рівень непогодженості є не прийнятним ')
print(f'RI = {get_stat(A_matrix, avr_NA)[1]} \nCR = {get_stat(A_matrix, avr_NA)[2]} \n')

print("Для матриці: Аl ")
if get_stat(Al_matrix, avr_NAl)[0] < 0.1:
    print(f'CI = {get_stat(Al_matrix, avr_NAl)[0]} < 0.1 - рівень непогодженості є прийнятним ')
else:
    print(f'CI = {get_stat(Al_matrix, avr_NAl)[0]} < 0.1 - рівень непогодженості є не прийнятним ')
print(f'RI = {get_stat(Al_matrix, avr_NAl)[1]} \nCR = {get_stat(Al_matrix, avr_NAl)[2]} \n')

print("Для матриці: Аc ")
if get_stat(Ac_matrix, avr_NAc)[0] < 0.1:
    print(f'CI = {get_stat(Ac_matrix, avr_NAc)[0]} < 0.1 - рівень непогодженості є прийнятним ')
else:
    print(f'CI = {get_stat(Ac_matrix, avr_NAc)[0]} < 0.1 - рівень непогодженості є не прийнятним ')
print(f'RI = {get_stat(Ac_matrix, avr_NAc)[1]} \nCR = {get_stat(Ac_matrix, avr_NAc)[2]} \n')

print("Для матриці: Аr ")
if get_stat(Ar_matrix, avr_NAr)[0] < 0.1:
    print(f'CI = {get_stat(Ar_matrix, avr_NAr)[0]} < 0.1 - рівень непогодженості є прийнятним ')
else:
    print(f'CI = {get_stat(Ar_matrix, avr_NAr)[0]} < 0.1 - рівень непогодженості є не прийнятним ')
print(f'RI = {get_stat(Ar_matrix, avr_NAr)[1]} \nCR = {get_stat(Ar_matrix, avr_NAr)[2]} \n')

L = get_stat(Al_matrix, avr_NAl)
R = get_stat(Ar_matrix, avr_NAr)
C = get_stat(Ac_matrix, avr_NAc)
A = get_stat(A_matrix, avr_NA)

coef_L = A[0] * (L[0] * R[0] * C[1]) + A[1] * (L[1] * R[1] * C[0])
coef_R = A[0] * (L[0] * R[1] * C[1]) + A[1] * (L[1] * R[1] * C[1])
coef_C = A[0] * (L[0] * R[2] * C[1]) + A[1] * (L[1] * R[2] * C[2])

print(f'Кобінований ваговий коефіцієнт для кандидата L = {coef_L}')
print(f'Кобінований ваговий коефіцієнт для кандидата R = {coef_R}')
print(f'Кобінований ваговий коефіцієнт для кандидата C = {coef_C}')
