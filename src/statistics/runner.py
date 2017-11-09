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
    plot_and_save(feeder.get_initial_BMI_list(), feeder.get_child_weight_list(), 'initial_BMI_to_child_weight')
    plot_and_save(xrange(15, 55), feeder.get_child_weight_standard_deviation_list(), 'initial_BMI_to_child_weight_standard_deviation')
    plot_and_save(xrange(15, 55), feeder.get_child_weight_mean_list(), 'initial_BMI_to_child_mean_weight')
    plot_and_save(feeder.get_initial_weight_list(), feeder.get_delta_weight_list(), 'initial_weight_to_delta_weight')
    plot_and_save(feeder.get_number_of_miscarriages_list(), feeder.get_initial_BMI_list(), 'initial_BMI_to_number_of_miscarriages', shape='.')

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

    def count_ORs(name, method, method_positive, method_negative):
        print name
        chance_0 = method(feeders[0])
        chance_1 = method(feeders[1])
        chance_2 = method(feeders[2])
        chance_3 = method(feeders[3])

        print "chances: ", chance_0, chance_1, chance_2, chance_3
        or1, or2, or3, or4 = chance_0 / chance_1, chance_1 / chance_1, chance_2 / chance_1, chance_3 / chance_1
        print "ORs: ", or1, or2, or3, or4

        a1 = method_positive(feeders[0])
        b1 = method_negative(feeders[0])
        a3 = method_positive(feeders[2])
        b3 = method_negative(feeders[2])
        a4 = method_positive(feeders[3])
        b4 = method_negative(feeders[3])

        c = method_positive(feeders[1])
        d = method_negative(feeders[1])

        try:
            SE = math.sqrt(1./a1 + 1./b1 + 1./c + 1./d)
            bottom = math.exp(math.log(or1) - 1.96*SE)
            top = math.exp(math.log(or1) + 1.96 * SE)
            print "group 1: ", bottom, top
        except ZeroDivisionError:
            pass

        try:
            SE = math.sqrt(1. / a3 + 1. / b3 + 1. / c + 1. / d)
            bottom = math.exp(math.log(or3) - 1.96 * SE)
            top = math.exp(math.log(or3) + 1.96 * SE)
            print "group 3: ", bottom, top
        except ZeroDivisionError:
            pass
        try:
            SE = math.sqrt(1. / a4 + 1. / b4 + 1. / c + 1. / d)
            bottom = math.exp(math.log(or4) - 1.96 * SE)
            top = math.exp(math.log(or4) + 1.96 * SE)
            print "group 4: ", bottom, top
        except ZeroDivisionError:
            pass

        print

    count_ORs("not planned t section chance", lambda x: x.get_not_planned_t_section_chance(),
              lambda x: x.get_not_planned_t_section_positive(), lambda x: x.get_not_planned_t_section_negative())

    count_ORs("t section chance", lambda x: x.get_t_section_chance(),
              lambda x: x.get_t_section_positive(), lambda x: x.get_t_section_negative())

    count_ORs("over 90 percentile", lambda x: x.get_90_percentile_chance(),
              lambda x: x.get_90_percentile_positive(), lambda x: x.get_90_percentile_negative())

    count_ORs("hipotrophic", lambda x: x.get_hipotrophic_chance(),
              lambda x: x.get_hipotrophic_positive(), lambda x: x.get_hipotrophic_negative())

    count_ORs("macrosomic", lambda x: x.get_macrosomic_chance(),
              lambda x: x.get_macrosomic_positive(), lambda x: x.get_macrosomic_negative())

    count_ORs("prebirth", lambda x: x.get_premature_birth_chance(),
              lambda x: x.get_premature_birth_positive(), lambda x: x.get_premature_birth_negative())

    count_ORs("under 10 percentile", lambda x: x.get_10_percentile_chance(),
              lambda x: x.get_10_percentile_positive(), lambda x: x.get_10_percentile_negative())


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

