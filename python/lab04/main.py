"""
Movement along z-axis (perpendiculary surface)
dz(t)/dt = v(t)
dv(t)/dt = -g - (A*v(t) + B*v(t)^3)/m
"""


# пользовательская фуг=нкция для вычисления правых частей
def system(f, t):
    global m,g,A,B
    z = f[0]
    v = f[1]
    dzdt = v
    dvdt = -g - (A*v + B*v**3)/m
    return [dzdt,dvdt]

def poletnoe(t, v, z):
    ttm = 0.0 # время полета
    ttmi = 0;
    ttz = 0.0  # высота подъема
    t_pod = 0.0 # время подъема
    t_spusk = 0.0 # время спуска
    for i in range(0, len(t)-1, 1):
        if z[i] >= 0.0:
            ttm = t[i]
            ttmi = i
        if z[i] >= ttz:
            ttz = z[i]
            t_pod = t[i]
    t_spusk = ttm - t_pod
    return [ttmi, ttm, ttz, t_pod, t_spusk]


if __name__ == '__main__':
    import numpy as np
    # import scipy.integrate as si
    from scipy.integrate import odeint
    import matplotlib.pyplot as plt

    z0 = 0.0  # m  нач услович
    v0 = 500.0  # m/sec нач условия, скорость начальная
    m = 0.009  # kg
    g = 9.8  # m/sec^2
    A = 1.e-5  # N*sec/m
    B = 1.e-8  # N*sec^3/m^3
    tm = 110.0  # sec  <-- должен быть больше, чем реальное полетное время

    nt = 1000
    t = np.linspace(0., tm, nt) # разбиваем на узлы времени
    sol = odeint(system, [z0, v0], t) # решаем
    z = sol[:, 0]
    v = sol[:, 1]

    solv = poletnoe(t, v, z)
    ttmi = solv[0]
    ttm = solv[1]
    maxz = solv[2]
    t_pod = solv[3]
    t_spusk = solv[4]

    t = t[:ttmi]
    v = v[:ttmi]
    z = z[:ttmi]
    nt = ttmi
    tm = ttm


    # и строим графики Здесь полетное время не вичислено!!
    plt.plot(t, v, 'r-', linewidth=3) # график скорости от времени
    plt.plot(t, [0.0] * nt, 'g-', linewidth=1)
    plt.axis([0, tm, -250., 500.])
    plt.grid(True)
    plt.xlabel("t")
    plt.ylabel("v(t)")
    plt.savefig("v.pdf", dpi=300)
    plt.show()

    plt.plot(t, z, 'b-', linewidth=3) # график положения от времени
    plt.axis([0, tm + 1., 0., 3500.])
    plt.grid(True)
    plt.xlabel("t")
    plt.ylabel("z(t)")
    plt.savefig("z.pdf", dpi=300)
    plt.show()

    # eще нужно определить полетное время, в цикле обойти массив z и начти, когда поменяет знак
    # или же методом деления пополам, это лучше
    # НУЖНО НАЙТИ:
    # 1) полетное время и перечертить графики с учетом полетного времени
    # (чтобы кривая заполняла полностью поле графика)
    # 2) Найти максимальную высоту полета
    # 3) найти время подъема и время спуска, сравнить их
