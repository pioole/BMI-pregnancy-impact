import csv
import logging

from src.model.patient import Patient


class PatientReader(object):
    @staticmethod
    def parse_patient(data, ignore_weight_at_labour=False, ignore_thrombosis_risk=False):
        """

        :param data: list of values [age (y), height (m), weight at labour (kg), weight initially (kg), child weight (g), pregnancy time in format "weeks+days" || "weeks"
        :return: Patient || None
        """
        try:
            age = int(data[0])
            height = float(data[1].replace(',', '.'))
            weight_initially = float(data[3].replace(',', '.'))
            if not ignore_weight_at_labour:
                weight_at_labour = float(data[2].replace(',', '.'))
            else:
                weight_at_labour = 0
            child_weight = int(data[4])
            pregnancy_time_weeks = int(data[5].strip().split('+')[0])
            pregnancy_time_additional_days = int(data[5].strip().split('+')[1]) if '+' in data[5] else 0
            pregnancy_time = pregnancy_time_weeks * 7 + pregnancy_time_additional_days
            number_of_labours = int(data[7])
            number_of_miscarriages = int(data[6]) - int(data[7])
            if not ignore_thrombosis_risk:
                thrombosis_risk = int(data[8])  # lots of invalid data
            else:
                thrombosis_risk = 0
            t_section = data[9] == '2'
            t_section_planned = data[10] == '1'
            return Patient(age, height, weight_initially, weight_at_labour, child_weight, pregnancy_time,
                           number_of_labours, number_of_miscarriages, thrombosis_risk, t_section, t_section_planned)
        except ValueError as e:
            logging.error('error: {} in {}'.format(e, data))
        return None

    @staticmethod
    def return_as_list(path_to_csv, ignore_weight_at_labour=False, ignore_thrombosis_risk=False):
        """

        :param path_to_csv: String
        :return: [Patient]
        """
        with open(path_to_csv, 'r') as csv_file:
            file_reader = csv.reader(csv_file)
            patient_list = [PatientReader.parse_patient(x,
                                                        ignore_weight_at_labour=ignore_weight_at_labour,
                                                        ignore_thrombosis_risk=ignore_thrombosis_risk)
                            for x in file_reader]
            logging.info('{} invalid lines'.format(patient_list.count(None)))
        return filter(lambda x: x is not None, patient_list)
