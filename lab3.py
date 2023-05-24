
infl = 0.2
spad = 0.15
nothing = 0.65

obl = nothing * (0.075 * 1.08) + infl*(0.08*1.1) + spad*(0.06*1.05)

print(f'\nЗ урахуванням всіх ризиків прибуток від покупки облігацій : {obl}')

persent = 0.01
divident = nothing * (persent * 1.2) + infl*(persent*1) + spad*(persent*0.8)

print(f'З урахуванням всіх ризиків прибуток від інвестицій у фонд : {divident}')
