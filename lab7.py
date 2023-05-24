"""

Lab 7 SPPR
by Senko

"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)

y1 = [14*i - 8 for i in x]
y2 = [50*i + 1 for i in x]
y3 = [59.8*i - 9.8 for i in x]

plt.title('Lab7 Yusenko437')
plt.xlabel("x")
plt.ylabel("y1, y2, y3")
plt.grid()
plt.plot(x, y1, x, y2, x, y3)
plt.show()