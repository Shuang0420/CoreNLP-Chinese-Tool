# -*- coding: utf-8 -*-


__metaclass__ = type


class DPTreePath:
    def __init__(self, first_start, first_end, second_start, second_end, name):
        self._first_start = first_start
        self._first_end = first_end
        self._second_start = second_start
        self._second_end = second_end
        self._name = name

    @property
    def first_start(self):
        return self._first_start

    @property
    def first_end(self):
        return self._first_end

    @property
    def second_start(self):
        return self._second_start

    @property
    def second_end(self):
        return self._second_end

    @property
    def name(self):
        return self._name
