import os
import csv
import operator


class Request:

    def __init__(self, pos_key, pos, num_key, num, reas_key, reason, sol_key, solved):
        self.pos_key = pos_key
        self.pos = pos
        self.num_key = num_key
        self.num = num
        self.reas_key = reas_key
        self.reason = reason
        self.sol_key = sol_key
        self.solved = solved

    def __repr__(self):
        return f"{self.pos_key}: {self.pos}; {self.num_key}"

