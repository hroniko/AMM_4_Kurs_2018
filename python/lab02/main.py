if __name__ == '__main__':
    # import matplotlib as mpl
    # import matplotlib.pyplot as plt
    # # Вывод на экран текущей версии библиотеки matplotlib
    # print('Current version on matplotlib library is', mpl.__version__)
    #
    # fig = plt.figure()
    # # Добавление на рисунок прямоугольной (по умолчанию) области рисования
    # ax = fig.add_axes([0, 0, 1, 1])
    # print(type(ax))
    # plt.scatter(1.0, 1.0)
    # plt.savefig('example 142a.png', fmt='png')
    #
    # fig = plt.figure()
    # # Добавление на рисунок круговой области рисования
    # ax = fig.add_axes([0, 0, 1, 1], polar=True)
    # plt.scatter(0.0, 0.5)
    # plt.savefig('example 142b.png', fmt='png')
    # plt.show()

    import matplotlib.pyplot as plt
    import numpy as np


    def f(t):
        'A damped exponential'
        s1 = np.cos(2 * np.pi * t)
        e1 = np.exp(-t)
        return s1 * e1


    t1 = np.arange(0.0, 5.0, .2)

    l = plt.plot(t1, f(t1), 'ro')
    plt.setp(l, markersize=30)
    plt.setp(l, markerfacecolor='C0')

    plt.show()

    # 2)
    N = 5
    menMeans = (20, 35, 30, 35, 27)
    womenMeans = (25, 32, 34, 20, 25)
    menStd = (2, 3, 4, 1, 2)
    womenStd = (3, 5, 2, 3, 3)
    ind = np.arange(N)  # the x locations for the groups
    width = 0.35  # the width of the bars: can also be len(x) sequence

    p1 = plt.bar(ind, menMeans, width, yerr=menStd)
    p2 = plt.bar(ind, womenMeans, width,
                 bottom=menMeans, yerr=womenStd)

    plt.ylabel('Scores')
    plt.title('Scores by group and gender')
    plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
    plt.yticks(np.arange(0, 81, 10))
    plt.legend((p1[0], p2[0]), ('Men', 'Women'))

    plt.show()

    # 3)

    men_means, men_std = (20, 35, 30, 35, 27), (2, 3, 4, 1, 2)
    women_means, women_std = (25, 32, 34, 20, 25), (3, 5, 2, 3, 3)

    ind = np.arange(len(men_means))  # the x locations for the groups
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind - width / 2, men_means, width, yerr=men_std,
                    color='SkyBlue', label='Men')
    rects2 = ax.bar(ind + width / 2, women_means, width, yerr=women_std,
                    color='IndianRed', label='Women')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.set_xticks(ind)
    ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))
    ax.legend()


    def autolabel(rects, xpos='center'):
        """
        Attach a text label above each bar in *rects*, displaying its height.

        *xpos* indicates which side to place the text w.r.t. the center of
        the bar. It can be one of the following {'center', 'right', 'left'}.
        """

        xpos = xpos.lower()  # normalize the case of the parameter
        ha = {'center': 'center', 'right': 'left', 'left': 'right'}
        offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() * offset[xpos], 1.01 * height,
                    '{}'.format(height), ha=ha[xpos], va='bottom')


    autolabel(rects1, "left")
    autolabel(rects2, "right")

    plt.show()

    # 4)
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    plt.rcdefaults()
    fig, ax = plt.subplots()

    # Example data
    people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
    y_pos = np.arange(len(people))
    performance = 3 + 10 * np.random.rand(len(people))
    error = np.random.rand(len(people))

    ax.barh(y_pos, performance, xerr=error, align='center',
            color='green', ecolor='black')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(people)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Performance')
    ax.set_title('How fast do you want to go today?')

    plt.show()

    # 5)
    fig, ax = plt.subplots()
    ax.broken_barh([(110, 30), (150, 10)], (10, 9), facecolors='blue')
    ax.broken_barh([(10, 50), (100, 20), (130, 10)], (20, 9),
                   facecolors=('red', 'yellow', 'green'))
    ax.set_ylim(5, 35)
    ax.set_xlim(0, 200)
    ax.set_xlabel('seconds since start')
    ax.set_yticks([15, 25])
    ax.set_yticklabels(['Bill', 'Jim'])
    ax.grid(True)
    ax.annotate('race interrupted', (61, 25),
                xytext=(0.8, 0.9), textcoords='axes fraction',
                arrowprops=dict(facecolor='black', shrink=0.05),
                fontsize=16,
                horizontalalignment='right', verticalalignment='top')

    plt.show()

    # 6)
    data = {'apples': 10, 'oranges': 15, 'lemons': 5, 'limes': 20}
    names = list(data.keys())
    values = list(data.values())

    fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
    axs[0].bar(names, values)
    axs[1].scatter(names, values)
    axs[2].plot(names, values)
    fig.suptitle('Categorical Plotting')
    cat = ["bored", "happy", "bored", "bored", "happy", "bored"]
    dog = ["happy", "happy", "happy", "happy", "bored", "bored"]
    activity = ["combing", "drinking", "feeding", "napping", "playing", "washing"]

    fig, ax = plt.subplots()
    ax.plot(activity, dog, label="dog")
    ax.plot(activity, cat, label="cat")
    ax.legend()

    plt.show()

    # 8)
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    dt = 0.01
    t = np.arange(0, 30, dt)
    nse1 = np.random.randn(len(t))  # white noise 1
    nse2 = np.random.randn(len(t))  # white noise 2

    # Two signals with a coherent part at 10Hz and a random part
    s1 = np.sin(2 * np.pi * 10 * t) + nse1
    s2 = np.sin(2 * np.pi * 10 * t) + nse2

    fig, axs = plt.subplots(2, 1)
    axs[0].plot(t, s1, t, s2)
    axs[0].set_xlim(0, 2)
    axs[0].set_xlabel('time')
    axs[0].set_ylabel('s1 and s2')
    axs[0].grid(True)

    cxy, f = axs[1].cohere(s1, s2, 256, 1. / dt)
    axs[1].set_ylabel('coherence')

    fig.tight_layout()
    plt.show()

    # 9)
    fig, (ax1, ax2) = plt.subplots(2, 1)
    # make a little extra space between the subplots
    fig.subplots_adjust(hspace=0.5)

    dt = 0.01
    t = np.arange(0, 30, dt)

    # Fixing random state for reproducibility
    np.random.seed(19680801)

    nse1 = np.random.randn(len(t))  # white noise 1
    nse2 = np.random.randn(len(t))  # white noise 2
    r = np.exp(-t / 0.05)

    cnse1 = np.convolve(nse1, r, mode='same') * dt  # colored noise 1
    cnse2 = np.convolve(nse2, r, mode='same') * dt  # colored noise 2

    # two signals with a coherent part and a random part
    s1 = 0.01 * np.sin(2 * np.pi * 10 * t) + cnse1
    s2 = 0.01 * np.sin(2 * np.pi * 10 * t) + cnse2

    ax1.plot(t, s1, t, s2)
    ax1.set_xlim(0, 5)
    ax1.set_xlabel('time')
    ax1.set_ylabel('s1 and s2')
    ax1.grid(True)

    cxy, f = ax2.csd(s1, s2, 256, 1. / dt)
    ax2.set_ylabel('CSD (db)')
    plt.show()

    # 9)

    fig = plt.figure(0)
    x = np.arange(10.0)
    y = np.sin(np.arange(10.0) / 20.0 * np.pi)

    plt.errorbar(x, y, yerr=0.1)

    y = np.sin(np.arange(10.0) / 20.0 * np.pi) + 1
    plt.errorbar(x, y, yerr=0.1, uplims=True)

    y = np.sin(np.arange(10.0) / 20.0 * np.pi) + 2
    upperlimits = np.array([1, 0] * 5)
    lowerlimits = np.array([0, 1] * 5)
    plt.errorbar(x, y, yerr=0.1, uplims=upperlimits, lolims=lowerlimits)

    plt.xlim(-1, 10)

    fig = plt.figure(1)
    x = np.arange(10.0) / 10.0
    y = (x + 0.1) ** 2

    plt.errorbar(x, y, xerr=0.1, xlolims=True)
    y = (x + 0.1) ** 3

    plt.errorbar(x + 0.6, y, xerr=0.1, xuplims=upperlimits, xlolims=lowerlimits)

    y = (x + 0.1) ** 4
    plt.errorbar(x + 1.2, y, xerr=0.1, xuplims=True)

    plt.xlim(-0.2, 2.4)
    plt.ylim(-0.1, 1.3)

    plt.show()

    #