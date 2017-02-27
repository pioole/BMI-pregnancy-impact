import csv
import logging

from src.model.patient import Patient


class PatientReader(object):
    @staticmethod
    def parse_patient(data):
        """

        :param data: list of values [age (y), height (m), weight at labour (kg), weight initially (kg), child weight (g), pregnancy time in format "weeks+days" || "weeks"
        :return: Patient || None
        """
        if all(data):
            try:
                age = int(data[0])
                height = float(data[1].replace(',', '.'))
                weight_initially = float(data[3].replace(',', '.'))
                weight_at_labour = float(data[2].replace(',', '.'))
                child_weight = int(data[4])
                pregnancy_time_weeks = int(data[5].strip().split('+')[0])
                pregnancy_time_additional_days = int(data[5].strip().split('+')[1]) if '+' in data[5] else 0
                pregnancy_time = pregnancy_time_weeks * 7 + pregnancy_time_additional_days
                return Patient(age, height, weight_initially, weight_at_labour, child_weight, pregnancy_time)
            except ValueError as e:
                logging.error('error: {} in {}'.format(e, data))
        return None

    @staticmethod
    def return_as_list(path_to_csv):
        """

        :param path_to_csv: String
        :return: [Patient]
        """
        with open(path_to_csv, 'r') as csv_file:
            file_reader = csv.reader(csv_file)
            patient_list = [PatientReader.parse_patient(x) for x in file_reader]
            logging.info('{} invalid lines'.format(patient_list.count(None)))
        return filter(lambda x: x is not None, patient_list)
