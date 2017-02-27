from matplotlib.pyplot import plot, show, savefig, close


def simple_plot(args, vals):
    plot(args, vals, 'rd')
    show()


def plot_and_save(args, vals, name):
    plot(args, vals, 'rd')
    savefig('{}.jpg'.format(name))
    close()

