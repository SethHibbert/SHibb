import numpy as np
import matplotlib.pyplot as plt

xmin = -0.1
xmax = 1.1
no_iterations = 1000



def f(X, t):
    N = 1
    a = 0.5
    b = 2
    g = 1
    
    x1, x2 = X
    return [(a - 1)*x1+g*x2*x1, b*(N - x1 - x2)*x1 - g*x2*x1 - x2]


y1 = np.linspace(xmin, xmax, no_iterations)
y2 = np.linspace(xmin, xmax, no_iterations)

Y1, Y2 = np.meshgrid(y1, y2)

t = 0

u, v = np.zeros(Y1.shape), np.zeros(Y2.shape)

NI, NJ = Y1.shape

for i in range(NI):
    for j in range(NJ):
        x = Y1[i, j]
        y = Y2[i, j]
        yprime = f([x, y], t)
        u[i,j] = yprime[0]
        v[i,j] = yprime[1]

Q = plt.streamplot(Y1, Y2, u, v, color='b', linewidth=1)

xaxis = np.linspace(xmin, xmax, 100)
yaxis = np.zeros(100)

plt.plot(xaxis, yaxis, 'r', linewidth=1)
plt.plot(yaxis, xaxis, 'r', linewidth=1)
plt.title("Model")
plt.xlabel('Proficient Users')
plt.ylabel('Intermediate Users')
plt.xlim([xmin, xmax])
plt.ylim([xmin, xmax])