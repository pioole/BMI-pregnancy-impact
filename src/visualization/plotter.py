from matplotlib.pyplot import plot, show, savefig, close


def simple_plot(args, vals):
    plot(args, vals, 'rd')
    show()


def plot_and_save(args, vals, name, shape='d'):
    plot(args, vals, 'b' + shape)
    savefig('{}.png'.format(name))
    close()


def plot_and_save_multiple(args, vals, name):
    colours = ['m', 'g', 'b', 'r']
    x = 0
    for arg, val in zip(args, vals):
        plot(arg, val, '{}o'.format(colours[x]))
        x += 1
    savefig('{}.png'.format(name))
    close()

