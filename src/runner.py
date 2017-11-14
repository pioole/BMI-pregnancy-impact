import logging

from src.data.patients import PatientReader
from src.statistics.runner_initial_weight import run_statistics as run_statistics_initial_weight
from src.statistics.runner_thrombosis import run_statistics as run_statistics_thrombosis
from src.statistics.runner_weight_at_labour import run_statistics as run_statistics_weight_at_labour


def main():
    logging.basicConfig(level=logging.DEBUG)
    patient_list = PatientReader.return_as_list('../data.csv',
                                                ignore_thrombosis_risk=True,
                                                ignore_weight_at_labour=True)
    run_statistics_initial_weight(patient_list)
    # patient_list = PatientReader.return_as_list('../data.csv',
    #                                             ignore_weight_at_labour=True)
    # run_statistics_thrombosis(patient_list)
    # patient_list = PatientReader.return_as_list('../data.csv',
    #                                             ignore_thrombosis_risk=True)
    # run_statistics_weight_at_labour(patient_list)


if __name__ == '__main__':
    main()
