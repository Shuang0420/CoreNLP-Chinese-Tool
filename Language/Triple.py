# -*- coding: utf-8 -*-


__metaclass__ = type


class Entity:
    def __init__(self, name, ontology, para_idx):
        self._name = name
        self._ontology = ontology
        self._para_idx = para_idx

    def to_string(self):
        return self._name.decode("gb18030")

    @property
    def name(self):
        return self._name

    @property
    def ontology(self):
        return self._ontology

    @property
    def para_idx(self):
        return self._para_idx


class Key:
    def __init__(self, name, para_idx):
        self._name = name
        self._para_idx = para_idx

    def to_string(self):
        return self._name.decode("gb18030")

    @property
    def name(self):
        return self._name

    @property
    def para_idx(self):
        return self._para_idx


class Value:
    def __init__(self, value, unit, para_idx):
        self._value = value
        self._unit = unit
        self._para_idx = para_idx

    def to_string(self):
        if self._unit == "None":
            return self._value.decode("gb18030")
        else:
            return self._value.decode("gb18030") + self._unit.decode("gb18030")

    @staticmethod
    def merge(first, second):
        return Value(first.value + "\n" + second.value, "None", first.para_idx)

    @property
    def value(self):
        return self._value

    @property
    def unit(self):
        return self._unit

    @property
    def para_idx(self):
        return self._para_idx


class Triple:
    def __init__(self, lhs_entity, key, rhs_entity, rhs_value):
        self._lhs_entity = lhs_entity
        self._key = key
        self._rhs_entity = rhs_entity
        self._rhs_value = rhs_value

    def to_string(self):
        if self._rhs_entity is not None:
            return u"(" + self._lhs_entity.to_string() + u"; " + self._key.to_string() + u"; " + \
                   self._rhs_entity.to_string() + u")"
        else:
            return u"(" + self._lhs_entity.to_string() + u"; " + self._key.to_string() + u"; " + \
                   self._rhs_value.to_string() + u")"

    @property
    def lhs_entity(self):
        return self._lhs_entity

    @property
    def key(self):
        return self._key

    @property
    def rhs_entity(self):
        return self._rhs_entity

    @property
    def rhs_value(self):
        return self._rhs_value
