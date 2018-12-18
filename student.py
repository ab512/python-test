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

    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
        Student.count += 1
        # self.count=3

    @property
    def gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, birthday):
        self._birthday = birthday

    @property
    def age(self):
        return (datetime.now().year-datetime.strptime(self._birthday, '%Y-%m-%d').year)


# s1 = Student('Joy', 'male')
# print('%s' % s1.name)
# print('%s' % s1.get_gender())
# bart = Student('Bart', 'male')
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')
# if Student.count != 0:
#     print('测试失败0!%s' % Student.count)
# else:
#     bart = Student('Bart', '')
#     if Student.count != 1:
#         print('测试失败1!'+Student.count.__str__())
#     else:
#         lisa = Student('Bart', '')
#         if Student.count != 2:
#             print('测试失败2!'+Student.count.__str__())
#         else:
#             print('Students:', Student.count.__str__())
#             print('测试通过!')

# print('%s' % bart.count)
bart = Student('Bart', Gender.Male)
print(bart.birthday)
print(bart.gender)
bart.birthday = '2000-01-01'
print(bart.birthday)
print(bart.age)

if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')