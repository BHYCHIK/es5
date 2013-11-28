# -*- coding: utf-8 -*-

class HopfieldVectorSizeMissmatchError(Exception):pass
class HopfieldVectorIncorrectFormatError(Exception):pass

class HopfieldNetwork(object):
    def __init__(self, neurons_count):
        self._neurons_count = neurons_count
        self._diap = tuple(range(0, self._neurons_count))
        self._weights = [[0 for j in self._diap] for i in self._diap]

    def _check_input_vector(self, vector):
        if len(vector) != self._neurons_count:
            raise HopfieldVectorSizeMissmatchError()
        for i in vector:
            if i != -1 and i != 1:
                raise HopfieldVectorIncorrectFormatError()

    def _activation_function(self, value):
        return -1 if value < 0 else 1

    def learn_vector(self, vector_to_learn):
        self._check_input_vector(vector_to_learn)
        for i in self._diap:
            for j in self._diap:
                self._weights[i][j] = self._weights[i][j] + (vector_to_learn[i] * vector_to_learn[j] if i != j else 0)

    def filter_vector(self, vector_to_filter):
        self._check_input_vector(vector_to_filter)
        new_y = vector_to_filter[:]
        y = new_y[:]
        y[0] = 12 # Make bad vector
        while new_y != y:
            y = new_y[:]
            for i in sepf._diap:
                new_y[i] = 0
                for j in self._diap:
                    new_y[i] = new_y[i] + self._weights[i][j] * y[j]
                new_y[i] = self._activation_function(new_y[i])
        return y
