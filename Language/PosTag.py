# -*- coding: utf-8 -*-


__metaclass__ = type


class PosTag:
    def __init__(self, start, end, name):
        self._start = start
        self._end = end
        self._name = name

    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end

    @property
    def name(self):
        return self._name
