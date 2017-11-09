import os


class WeekPercentile(object):
    percentiles = [2.5, 5, 10, 25, 50, 75, 90, 95, 97.5]

    def __init__(self, week, data):
        self.week = week
        self.data = zip(data.strip().split(','), self.percentiles)

    def get_percentile(self, weight):
        try:
            return [data[1] for data in self.data if int(data[0]) >= weight][0]
        except IndexError:
            return 100


class PercentileCalculator(object):
    def __init__(self):
        self.week_percentiles = {}
        weeks = [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32,
                 33, 34, 35, 36, 37, 38, 39, 40]
        with open(os.path.join(os.path.dirname(__file__), '..', '..', 'percentile_data.csv')) as f:
            data_lines = f.readlines()

            for week, data in zip(weeks, data_lines):
                self.week_percentiles[week] = WeekPercentile(week, data)

    def calculate_percentile(self, weight, pregnancy_time):
        week = (pregnancy_time - 1) / 7 + 1
        if week > 40:
            print pregnancy_time % 7, week
            week = 40
        return self.week_percentiles[week].get_percentile(weight)


calc = PercentileCalculator()


class Patient(object):
    def __init__(self, age, height, weight_initially, weight_at_labour, child_weight, pregnancy_time, number_of_labours,
                 number_of_miscarriages, thrombosis_risk, t_section, t_section_planned):
        """
        creates a new Patient
        :param age: Int, years
        :param height: Float, meters
        :param weight_initially: Float, kilograms
        :param weight_at_labour: Float, kilograms
        :param child_weight: Int, grams
        :param pregnancy_time: Int, days
        :return:
        """
        self.age = age
        self.height = height
        self.weight_initially = weight_initially
        self.weight_at_labour = weight_at_labour
        self.child_weight = child_weight
        self.pregnancy_time = pregnancy_time
        self.BMI_initially = weight_initially / (height * height)
        self.BMI_at_labour = weight_at_labour / (height * height)
        self.delta_BMI = self.BMI_at_labour - self.BMI_initially
        self.delta_weight = weight_at_labour - weight_initially
        self.weight_change_percentage = 100. * weight_at_labour / weight_initially
        self.number_of_labours = number_of_labours
        self.number_of_miscarriages = number_of_miscarriages
        self.thrombosis_risk = thrombosis_risk
        self.t_section = t_section
        self.t_section_planned = t_section_planned

        self.hipotrophic_child = self.child_weight < 2500
        self.macrosomic_child = self.child_weight > 4500
        self.preterm_birth = self.pregnancy_time <= 258
        self.percentile = calc.calculate_percentile(self.child_weight, self.pregnancy_time)
        self.under_10_percentile = self.percentile <= 10
        self.over_90_percentile = self.percentile >= 90
