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
    feeder = DataFeeder(patient_list)

    plot_and_save(feeder.get_delta_weight_list(), feeder.get_child_weight_list(), 'delta_weight_to_child_weight')
    plot_and_save(feeder.get_weight_change_percentage_list(), feeder.get_child_weight_list(), 'weight_change_percentage_to_child_weight')
    plot_and_save(feeder.get_initial_weight_list(), feeder.get_delta_weight_list(), 'initial_weight_to_delta_weight')

    ##### GROUPS

    intervals = [(0, 18.5), (18.5, 25), (25, 30), (30, 100)]
    method = lambda x, y: y[0] <= x < y[1]

    feeders = generate_feeder(patient_list, lambda x: x.BMI_initially, method, intervals)
    control_group = feeders[1]

    run_multiple_plotter('weight_change_percentage_to_child_weight_GROUPS',
                         feeders,
                         lambda x: x.get_weight_change_percentage_list(),
                         lambda x: x.get_child_weight_list())

    run_multiple_plotter('delta_weight_to_child_weight_GROUPS',
                         feeders,
                         lambda x: x.get_delta_weight_list(),
                         lambda x: x.get_child_weight_list())

    ######### GROUPS 2

    intervals = [(0, 18.5), (18.5, 25), (25, 30), (30, 100)]
    method = lambda x, y: y[0] <= x < y[1]

    feeders = generate_feeder(patient_list, lambda x: x.BMI_at_labour, method, intervals)

    calculate_in_groups('percentage_of_first_timers_in_GROUPS_BMI_AT_LABOUR', feeders, lambda x: x.get_percentage_of_first_timers())
    calculate_in_groups('number_of_patients_in_GROUPS_BMI_AT_LABOUR', feeders, lambda x: x.get_number_of_patients())
