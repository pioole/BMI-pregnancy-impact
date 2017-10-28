from src.data.data_feeder import DataFeeder
from src.visualization.plotter import simple_plot, plot_and_save, plot_and_save_multiple


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

    feeder_1 = DataFeeder([patient for patient in patient_list if patient.BMI_initially < 18.5])
    feeder_2 = DataFeeder([patient for patient in patient_list if 18.5 <= patient.BMI_initially < 25])
    feeder_3 = DataFeeder([patient for patient in patient_list if 25 <= patient.BMI_initially < 30])
    feeder_4 = DataFeeder([patient for patient in patient_list if 30 <= patient.BMI_initially])

    feeders = [feeder_1, feeder_2, feeder_3, feeder_4]


    name = 'weight_change_percentage_to_child_weight_GROUPS'
    args, vals = [], []
    for feed in feeders:
        arg, val = feed.get_weight_change_percentage_list(), feed.get_child_weight_list()
        args.append(arg)
        vals.append(val)

    plot_and_save_multiple(args, vals, name)

    name = 'delta_weight_to_child_weight_GROUPS'
    args, vals = [], []
    for feed in feeders:
        arg, val = feed.get_delta_weight_list(), feed.get_child_weight_list()
        args.append(arg)
        vals.append(val)

    plot_and_save_multiple(args, vals, name)

    name = 'BMI_to_mean_time_of_pregnancy_in_GROUPS_BMI_INITIALLY'
    args, vals = [], []
    for feed in feeders:
        arg, val = feed.get_initial_BMI_list(), feed.get_length_of_pregnancy_list()
        args.append(arg)
        vals.append(val)

    plot_and_save_multiple(args, vals, name)

    name = 'BMI_to_thrombosis_in_GROUPS_BMI_INITIALLY'
    args, vals = [], []
    for feed in feeders:
        arg, val = feed.get_initial_BMI_list(), feed.get_thrombosis_risk_list()
        args.append(arg)
        vals.append(val)

    plot_and_save_multiple(args, vals, name)

    name = 'standard_deviation_in_GROUPS'
    print name
    for feed in feeders:
        print feed.get_child_weight_standard_deviation()

    name = 'mean_in_GROUPS'
    print
    print name
    for feed in feeders:
        print feed.get_child_weight_mean()

    name = 'percentage_of_first_timers_in_GROUPS'
    print
    print name
    for feed in feeders:
        print feed.get_percentage_of_first_timers()

    name = 'number_of_patients_in_GROUPS'
    print
    print name
    for feed in feeders:
        print feed.get_number_of_patients()

    name = 'mean_time_of_pregnancy_in_GROUPS_BMI_INITIALLY'
    print
    print name
    for feed in feeders:
        print feed.get_mean_length_of_pregnancy()


    name = 'count_of_early_births_in_GROUPS_BMI_INITIALLY'
    print
    print name
    for feed in feeders:
        print feed.get_count_of_early_births(), 'z', feed.get_number_of_patients(), '->', 1.*feed.get_count_of_early_births()/feed.get_number_of_patients(), '%'

    name = 'mean_thrombosis_in_GROUPS_BMI_INITIALLY'
    print
    print name
    for feed in feeders:
        print feed.get_mean_thrombosis_risk()

    ######### GROUPS 2

    feeder_1 = DataFeeder([patient for patient in patient_list if patient.BMI_at_labour < 18.5])
    feeder_2 = DataFeeder([patient for patient in patient_list if 18.5 <= patient.BMI_at_labour < 25])
    feeder_3 = DataFeeder([patient for patient in patient_list if 25 <= patient.BMI_at_labour < 30])
    feeder_4 = DataFeeder([patient for patient in patient_list if 30 <= patient.BMI_at_labour])

    feeders = [feeder_1, feeder_2, feeder_3, feeder_4]

    name = 'percentage_of_first_timers_in_GROUPS_BMI_AT_LABOUR'
    print
    print name
    for feed in feeders:
        print feed.get_percentage_of_first_timers()

    name = 'number_of_patients_in_GROUPS_BMI_AT_LABOUR'
    print
    print name
    for feed in feeders:
        print feed.get_number_of_patients()


    ######### GROUPS 3

    feeder_1 = DataFeeder([patient for patient in patient_list if patient.number_of_labours == 1])
    feeder_2 = DataFeeder([patient for patient in patient_list if patient.number_of_labours > 1])

    feeders = [feeder_1, feeder_2]

    name = 'mean_patient_weight_initially_in_GROUPS_BY_NUMBER_OF_LABOURS'
    print
    print name
    for feed in feeders:
        print feed.get_mean_initial_weight()

    name = 'mean_patient_weight_at_labour_in_GROUPS_BY_NUMBER_OF_LABOURS'
    print
    print name
    for feed in feeders:
        print feed.get_mean_weight_at_labour()

    ######### GROUPS 4

    feeder_1 = DataFeeder([patient for patient in patient_list if patient.number_of_miscarriages == 0])
    feeder_2 = DataFeeder([patient for patient in patient_list if patient.number_of_miscarriages == 1])
    feeder_3 = DataFeeder([patient for patient in patient_list if patient.number_of_miscarriages == 2])
    feeder_4 = DataFeeder([patient for patient in patient_list if patient.number_of_miscarriages == 3])
    feeder_5 = DataFeeder([patient for patient in patient_list if patient.number_of_miscarriages == 4])

    feeders = [feeder_1, feeder_2, feeder_3, feeder_4, feeder_5]

    name = 'mean_patient_initial_BMI_in_GROUPS_BY_NUMBER_OF_MISCARRIAGES'
    print
    print name
    for feed in feeders:
        print feed.get_mean_initial_BMI()

    name = 'number_of_patients_in_GROUPS_BY_NUMBER_OF_MISCARRIAGES'
    print
    print name
    for feed in feeders:
        print feed.get_number_of_patients()

