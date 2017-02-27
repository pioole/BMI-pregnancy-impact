

class DataFeeder(object):
    def __init__(self, patient_list):
        """
        creates new DataFeeder, it asked data in lists assuring data indexes match.
        :param patient_list: [Patient]
        :return: DataFeeder
        """
        self.patient_list = patient_list

    def get_initial_weight_list(self):
        return [patient.weight_initially for patient in self.patient_list]

    def get_child_weight_list(self):
        return [patient.child_weight for patient in self.patient_list]

    def get_delta_weight_list(self):
        return [patient.delta_weight for patient in self.patient_list]

    def get_initial_BMI_list(self):
        return [patient.BMI_initially for patient in self.patient_list]

    def get_delta_weight_to_initial_weight_ratio_list(self):
        return [patient.delta_weight / patient.weight_initially for patient in self.patient_list]
