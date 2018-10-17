# -*- coding: cp1251 -*-
"""
Lotka–Volterra using scipy.integrate.odeint:

dx/dt = x*(alpha - beta*y);
dy/dt =-y*(gamma - delta*x);
"""


def system(z,t):
   x,y=z[0],z[1]
   dxdt= x*(alpha-beta*y)
   dydt=-y*(gamma-delta*x)
   return [dxdt,dydt]

if __name__ == '__main__':
    import numpy as np
    from scipy.integrate import odeint
    import matplotlib .pyplot as plt

    alpha = 0.1
    beta = 0.015
    gamma = 0.0225
    delta = 0.02

    t = np.linspace(0, 300., 1000)
    x0, y0 = 1.0, 1.0
    sol = odeint(system, [x0, y0], t)
    X, Y = sol[:, 0], sol[:, 1]
    plt.plot(X, Y, 'b-', linewidth=5)
    plt.grid(True)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.savefig('y1.pdf', dpi=300)
    plt.show()
