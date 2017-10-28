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
    plot_and_save(feeder.get_initial_BMI_list(), feeder.get_child_weight_list(), 'initial_BMI_to_child_weight')
    plot_and_save(xrange(15, 55), feeder.get_child_weight_standard_deviation_list(), 'initial_BMI_to_child_weight_standard_deviation')
    plot_and_save(xrange(15, 55), feeder.get_child_weight_mean_list(), 'initial_BMI_to_child_mean_weight')
    plot_and_save(feeder.get_initial_weight_list(), feeder.get_delta_weight_list(), 'initial_weight_to_delta_weight')
    plot_and_save(feeder.get_number_of_miscarriages_list(), feeder.get_initial_BMI_list(), 'initial_BMI_to_number_of_miscarriages', shape='.')

    ##### GROUPS

    intervals = [(0, 18.5), (18.5, 25), (25, 30), (30, 100)]
    method = lambda x, y: y[0] <= x < y[1]

    feeders = generate_feeder(patient_list, lambda x: x.BMI_initially, method, intervals)

    run_multiple_plotter('weight_change_percentage_to_child_weight_GROUPS',
                         feeders,
                         lambda x: x.get_weight_change_percentage_list(),
                         lambda x: x.get_child_weight_list())

    run_multiple_plotter('delta_weight_to_child_weight_GROUPS',
                         feeders,
                         lambda x: x.get_delta_weight_list(),
                         lambda x: x.get_child_weight_list())

    run_multiple_plotter('BMI_to_mean_time_of_pregnancy_in_GROUPS_BMI_INITIALLY',
                         feeders,
                         lambda x: x.get_initial_BMI_list(),
                         lambda x: x.get_length_of_pregnancy_list())

    run_multiple_plotter('BMI_to_thrombosis_in_GROUPS_BMI_INITIALLY',
                         feeders,
                         lambda x: x.get_initial_BMI_list(),
                         lambda x: x.get_thrombosis_risk_list())

    calculate_in_groups('standard_deviation_in_GROUPS', feeders, lambda x: x.get_child_weight_standard_deviation())
    calculate_in_groups('mean_in_GROUPS', feeders, lambda x: x.get_child_weight_mean())
    calculate_in_groups('percentage_of_first_timers_in_GROUPS', feeders, lambda x: x.get_percentage_of_first_timers())
    calculate_in_groups('number_of_patients_in_GROUPS', feeders, lambda x: x.get_number_of_patients())
    calculate_in_groups('mean_time_of_pregnancy_in_GROUPS_BMI_INITIALLY', feeders, lambda x: x.get_mean_length_of_pregnancy())
    calculate_in_groups('count_of_early_births_in_GROUPS_BMI_INITIALLY', feeders, lambda x: (x.get_count_of_early_births(), 'z', x.get_number_of_patients(), '->', 1.*x.get_count_of_early_births()/x.get_number_of_patients(), '%'))
    calculate_in_groups('mean_thrombosis_in_GROUPS_BMI_INITIALLY', feeders, lambda x: x.get_mean_thrombosis_risk())

    ######### GROUPS 2

    intervals = [(0, 18.5), (18.5, 25), (25, 30), (30, 100)]
    method = lambda x, y: y[0] <= x < y[1]

    feeders = generate_feeder(patient_list, lambda x: x.BMI_at_labour, method, intervals)

    calculate_in_groups('percentage_of_first_timers_in_GROUPS_BMI_AT_LABOUR', feeders, lambda x: x.get_percentage_of_first_timers())
    calculate_in_groups('number_of_patients_in_GROUPS_BMI_AT_LABOUR', feeders, lambda x: x.get_number_of_patients())

    ######### GROUPS 3

    feeder_1 = DataFeeder([patient for patient in patient_list if patient.number_of_labours == 1])
    feeder_2 = DataFeeder([patient for patient in patient_list if patient.number_of_labours > 1])

    feeders = [feeder_1, feeder_2]

    calculate_in_groups('mean_patient_weight_initially_in_GROUPS_BY_NUMBER_OF_LABOURS', feeders, lambda x: x.get_mean_initial_weight())
    calculate_in_groups('mean_patient_weight_at_labour_in_GROUPS_BY_NUMBER_OF_LABOURS', feeders, lambda x: x.get_mean_weight_at_labour())

    ######### GROUPS 4

    feeder_1 = DataFeeder([patient for patient in patient_list if patient.number_of_miscarriages == 0])
    feeder_2 = DataFeeder([patient for patient in patient_list if patient.number_of_miscarriages == 1])
    feeder_3 = DataFeeder([patient for patient in patient_list if patient.number_of_miscarriages == 2])
    feeder_4 = DataFeeder([patient for patient in patient_list if patient.number_of_miscarriages == 3])
    feeder_5 = DataFeeder([patient for patient in patient_list if patient.number_of_miscarriages == 4])

    feeders = [feeder_1, feeder_2, feeder_3, feeder_4, feeder_5]

    calculate_in_groups('mean_patient_initial_BMI_in_GROUPS_BY_NUMBER_OF_MISCARRIAGES', feeders, lambda x: x.get_mean_initial_BMI())
    calculate_in_groups('number_of_patients_in_GROUPS_BY_NUMBER_OF_MISCARRIAGES', feeders, lambda x: x.get_number_of_patients())

