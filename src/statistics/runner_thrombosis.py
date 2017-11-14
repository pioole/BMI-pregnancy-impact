import math

from src.data.data_feeder import DataFeeder
from src.visualization.plotter import simple_plot, plot_and_save, plot_and_save_multiple


def generate_feeder(patient_list, patient_arg, filter_, groups):
    return [DataFeeder([patient for patient in patient_list if filter_(patient_arg(patient), group)])
            for group in groups]


def run_multiple_plotter(name, feeders, method1, method2):
    args, vals = [], []
    for feed in feeders:
        arg, val = method1(feed), method2(feed)
        args.append(arg)
        vals.append(val)
    plot_and_save_multiple(args, vals, name)


def calculate_in_groups(name, feeders, method):
    print name
    for feed in feeders:
        print method(feed)
    print


def run_statistics(patient_list):
    ##### GROUPS

    intervals = [(0, 18.5), (18.5, 25), (25, 30), (30, 100)]
    method = lambda x, y: y[0] <= x < y[1]

    feeders = generate_feeder(patient_list, lambda x: x.BMI_initially, method, intervals)

    run_multiple_plotter('BMI_to_thrombosis_in_GROUPS_BMI_INITIALLY',
                         feeders,
                         lambda x: x.get_initial_BMI_list(),
                         lambda x: x.get_thrombosis_risk_list())

    calculate_in_groups('mean_thrombosis_in_GROUPS_BMI_INITIALLY', feeders, lambda x: x.get_mean_thrombosis_risk())
