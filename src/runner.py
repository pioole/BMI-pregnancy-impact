import logging

from src.data.patients import PatientReader
from src.statistics.runner import run_statistics


def main():
    logging.basicConfig(level=logging.DEBUG)
    patient_list = PatientReader.return_as_list('../data.csv')
    run_statistics(patient_list)


if __name__ == '__main__':
    main()
