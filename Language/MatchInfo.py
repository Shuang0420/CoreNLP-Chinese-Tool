# -*- coding: utf-8 -*-
from __future__ import print_function


__metaclass__ = type


class MatchInfo:
    def __init__(self, start, end, name, children_start, children_end, children_name):
        self._start = start
        self._end = end
        self._name = name
        self._children_start = children_start
        self._children_end = children_end
        self._children_name = children_name

    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end

    @property
    def name(self):
        return self._name

    @property
    def children_start(self):
        return self._children_start

    @property
    def children_end(self):
        return self._children_end

    @property
    def children_name(self):
        return self._children_name

    def contains(self, other):
        return self._name == other.name and self._start <= other.start and self._end >= other.end

    def to_string(self, text):
        return text + u"[" + unicode(self.start) + u":" + unicode(self.end) + u"] = " + \
               text[self.start:self.end] + u"  <" + self._name + u">"

    @staticmethod
    def closure(matches):
        nested_matches = set()
        for match in matches:
            for other in matches:
                if match == other:
                    continue
                if match.contains(other) and not other.contains(match):
                    nested_matches.add(other)
        return [match for match in matches if match not in nested_matches]