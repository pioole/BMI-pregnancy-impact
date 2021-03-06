import numpy as np


class DataFeeder(object):
    def __init__(self, patient_list):
        """
        creates new DataFeeder, it asked data in lists assuring data indexes match.
        :param patient_list: [Patient]
        :return: DataFeeder
        """
        self.patient_list = patient_list

    # defaults

    def get_number_of_patients(self):
        return len(self.patient_list)

    def get_mean_initial_weight(self):
        return np.mean(self.get_initial_weight_list())

    def get_mean_weight_at_labour(self):
        return np.mean(self.get_weight_at_labour_list())

    def get_child_weight_standard_deviation(self):
        return np.std([patient.child_weight for patient in self.patient_list])

    def get_child_weight_mean(self):
        return np.mean([patient.child_weight for patient in self.patient_list])

    def get_mean_initial_BMI(self):
        return np.mean(self.get_initial_BMI_list())

    def get_mean_thrombosis_risk(self):
        return np.mean(self.get_thrombosis_risk_list())

    def get_mean_length_of_pregnancy(self):
        return np.mean(self.get_length_of_pregnancy_list())

    def get_percentage_of_first_timers(self):
        def is_first_timer(patient):
            if patient.number_of_labours == 1:
                return 1
            return 0
        try:
            return 1. * sum([is_first_timer(patient) for patient in self.patient_list]) / len(self.patient_list)
        except ZeroDivisionError:
            return -1

    # lists

    def get_initial_weight_list(self):
        return [patient.weight_initially for patient in self.patient_list]

    def get_weight_at_labour_list(self):
        return [patient.weight_at_labour for patient in self.patient_list]

    def get_number_of_miscarriages_list(self):
        return [patient.number_of_miscarriages for patient in self.patient_list]

    def get_child_weight_list(self):
        return [patient.child_weight for patient in self.patient_list]

    def get_child_weight_standard_deviation_list(self):
        stds = []
        for x in xrange(10, 50, 1):
            list_filtered = filter(lambda patient: x < patient.BMI_initially <= x + 10, self.patient_list)
            stds.append(np.std([patient.child_weight for patient in list_filtered]))
        return stds

    def get_child_weight_mean_list(self):
        stds = []
        for x in xrange(10, 50, 1):
            list_filtered = filter(lambda patient: x < patient.BMI_initially <= x + 10, self.patient_list)
            if len([patient.child_weight for patient in list_filtered]) != 0:
                stds.append(np.mean([patient.child_weight for patient in list_filtered]))
            else:
                stds.append(0)
        return stds

    def get_delta_weight_list(self):
        return [patient.delta_weight for patient in self.patient_list]

    def get_weight_change_percentage_list(self):
        return [patient.weight_change_percentage for patient in self.patient_list]

    def get_initial_BMI_list(self):
        return [patient.BMI_initially for patient in self.patient_list]

    def get_length_of_pregnancy_list(self):
        return [patient.pregnancy_time for patient in self.patient_list]

    def get_delta_weight_to_initial_weight_ratio_list(self):
        return [patient.delta_weight / patient.weight_initially for patient in self.patient_list]

    def get_count_of_early_births(self):
        return sum([patient.preterm_birth for patient in self.patient_list])

    def get_thrombosis_risk_list(self):
        return [patient.thrombosis_risk for patient in self.patient_list]
