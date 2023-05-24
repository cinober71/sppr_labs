import numpy as np

Pm = np.array([[0.8, 0.2],
               [0.85, 0.15]])

Pm12 = np.array([0.7, 0.3])

Pm_step2 = np.array([Pm[i] * Pm12[i] for i in range(Pm.shape[0])])

print(f' Таблиця ймовірності спільної появи подій: \n {Pm_step2}')

Pm_step3 = Pm_step2.sum(axis=0)
print(f' Абсолютні ймовірності \n {Pm_step3}')
# [[Ac_matrix[:, i] for i in range(Ar_matrix_sum.shape[0])][j] / Ar_matrix_sum[j] for j in

Pm_step4_temp = np.array([Pm_step2[:, i] / Pm_step3[i] for i in range(Pm_step2.shape[0])])

Pm_step4 = Pm_step4_temp.T[:, ::1]

print(f' Отримані апостероїдні ймовірності: \n{Pm_step4}')

Success_self = 310000*Pm_step4[0][0] + (-70000) * Pm_step4[0][1]
Success_comp = 120000*Pm_step4[0][0] + 30000*Pm_step4[0][1]

Unsuccess_self = 310000*Pm_step4[1][0] + (-70000) * Pm_step4[1][1]
Unsuccess_comp = 120000*Pm_step4[1][0] + 30000*Pm_step4[1][1]

print(f'\nДохід при успіху роману: \n Самодрук: {Success_self} \n '
      f'Контракт: {Success_comp} \n'
      f'\nДохід при провалі роману: \n'
      f' Самодрук: {Unsuccess_self} \n'
      f' Контракт: {Unsuccess_comp} \n'
)
