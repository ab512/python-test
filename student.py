#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from datetime import datetime, timedelta
from enum import Enum
import time


class Gender(Enum):
    Male = 1
    FeMale = 2


class Student(object):
    count = 0
    _birthday = '1901-01-01'

    def __init__(self, name, score):
        self.name = name
        self.score = score
        Student.count += 1
        # self.count=3

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, birthday):
        self._birthday = birthday

    @property
    def age(self):
        return (datetime.now().year-datetime.strptime(self._birthday, '%Y-%m-%d').year)

    def get_grade(self):
        if self.score<0 or self.score>100:
            raise ValueError('score must between 0-100')
        if self.score >= 80:
            return 'A'
        if self.score >= 60:
            return 'B'
        return 'C'
