"""
Lab6 SPPR
by Senko
"""

import numpy as np

TELEVISION = 0.5
NEWSPAPER = 0.3
RADIO = 0.2

BASE_FIRST = 0.5
BASE_SECOND = 0.5

START_MONEY = 1000

FOR_TEL = 700
FOR_RAD = 200
FOR_NEWS = 300
choise_menu = f"Реклама коштує: \n" \
              f"Телебачення - 700 у.о. (+50% потенційних споживачів)\n" \
              f"Газета - 300 у.о. (+30% потенційних споживачів)\n" \
              f"Радіо - 200 у.о. (+20% потенційних споживачів)\n"

input_choise = f"1 - купити рекламу на телебаченні\n" \
               f"2 - купити рекламу на радіо \n" \
               f"3 - купити рекламу в газеті\n"


def Buy(c, n, m):
    cover = c
    money = m
    if n == '1' and money >= FOR_TEL:
        money = money - FOR_TEL
        cover = cover + TELEVISION
        print(f'Ви купили рекламу на телебачені: \n'
              f'Ваш відсоток ринку на цей хід {cover * 100} \n'
              f'Залишок коштів: {money}\n\n')
        return money, cover
    elif n == '2' and money >= FOR_NEWS:
        money = money - FOR_NEWS
        cover = cover + NEWSPAPER
        print(f'Ви купили рекламу в газеті: \n'
              f'Ваш відсоток ринку на цей хід {cover * 100} \n'
              f'Залишок коштів: {money}\n\n')
        return money, cover
    elif n == '3' and money >= FOR_RAD:
        money = money - FOR_RAD
        cover = cover + RADIO
        print(f'Ви купили рекламу на радіо: \n'
              f'Ваш відсоток ринку на цей хід {cover * 100} \n'
              f'Залишок коштів: {money} \n\n')
        return money, cover
    else:
        print(f'Не вистачає грошей, ви програли гру')
        return 0, 0
def EndGame(c, m):
    print(f'Гру завершено \n'
          f'Перший гравець закінчив із результатом:\n'
          f'Обхват: {c[0]} Залишок коштів: {m[0]} \n'
          f'Другий гравець закінчив із результатом:\n'
          f'Обхват: {c[1]} Залишок коштів: {m[1]} \n')
    if c[0] > c[1]:
        print('Переміг перший гравець \n')
    elif c[0] < c[1]:
        print('Переміг другий гравець \n')
    else:
        print('Нічия')


def Game():
    print(f' Початок гри, коже із гравців котролює 50% ринку.\n {choise_menu}'
          f'Початкова сума на рекламу у кожного гравця - {START_MONEY}\n')
    money = [START_MONEY, START_MONEY]
    cover = [BASE_FIRST, BASE_SECOND]
    k = 1
    while True:
        if k == 1 and money[0] > 200:
            get = input(f'Хід першого гравця {choise_menu}{input_choise}')
            money[0], cover[0] = Buy(cover[0], get, money[0])
            cover[1] = 1 - cover[0]
            k = 2
        elif k == 2 and money[1] > 200:
            get = input(f'Хід другого гравця {choise_menu}{input_choise}')
            money[1], cover[1] = Buy(cover[1], get, money[1])
            cover[0] = 1 - cover[1]
            k = 1
        else:
            EndGame(cover, money)
            break

Game()

