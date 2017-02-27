from src.data.data_feeder import DataFeeder
from src.visualization.plotter import simple_plot, plot_and_save


def run_statistics(patient_list):
    feeder = DataFeeder(patient_list)

    plot_and_save(feeder.get_delta_weight_list(), feeder.get_child_weight_list(), 'delta_weight_to_child_weight')
    plot_and_save(feeder.get_initial_BMI_list(), feeder.get_child_weight_list(), 'initial_BMI_to_child_weight')
    plot_and_save(feeder.get_initial_weight_list(), feeder.get_delta_weight_list(), 'initial_weight_to_delta_weight')
    plot_and_save(feeder.get_delta_weight_to_initial_weight_ratio_list(), feeder.get_child_weight_list(), 'delta_weight_divided_by_initial_weight_tochild_weight')
