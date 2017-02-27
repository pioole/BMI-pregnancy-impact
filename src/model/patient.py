

class Patient(object):
    def __init__(self, age, height, weight_initially, weight_at_labour, child_weight, pregnancy_time):
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

