# -*- coding: utf-8 -*-


__metaclass__ = type


class QAPair:
    def __init__(self, question, answer, cell_pos, positions, para_idx, part_id):
        self._question = question
        self._answer = answer
        self._cell_pos = cell_pos
        self._positions = positions
        self._para_idx = para_idx
        self._part_id = part_id

    def __eq__(self, other):
        if not isinstance(other, QAPair):
            return False
        return self._question == other.question and self._answer == other.answer and self._cell_pos == other.cell_pos\
               and self._para_idx == other.para_idx and self._part_id == other.part_id

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return (self._question, self._answer, self._cell_pos, self.part_id).__hash__()

    def to_string(self):
        return u"[Q: " + self._question + u"] [A: " + self._answer + u"]"

    @property
    def question(self):
        return self._question

    @property
    def answer(self):
        return self._answer

    @property
    def cell_pos(self):
        return self._cell_pos

    @property
    def positions(self):
        return self._positions

    @property
    def para_idx(self):
        return self._para_idx

    @property
    def part_id(self):
        return self._part_id

    @staticmethod
    def merge(qa_pairs):
        answer = "\n".join([qa_pair.answer for qa_pair in qa_pairs])
        para_idx = []
        positions = []
        for qa_pair in qa_pairs:
            para_idx += qa_pair.para_idx
            positions += qa_pair.positions
        return QAPair(qa_pairs[0].question, answer, (0, 0), positions, para_idx, 0)
