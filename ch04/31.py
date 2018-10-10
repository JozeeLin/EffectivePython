#!/usr/bin/env python
# coding=utf-8

class Grade(object):
    def __init__(self):
        self._value = 0

    def __get__(self, instance, instance_type):
        return self._value

    def __set__(self, instance, value):
        if not(0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._value = value

class Exam(object):
    # 类属性Class attributes
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()

exam = Exam()
exam.writing_grade = 40  # python会将代码转译为Exam.__dict__['writing_grade'].__set__(exam,40)
exam.math_grade = 90

# 1===============
#print('Writing', exam.writing_grade)
#print('Math', exam.math_grade)

# 2=============
exam_second = Exam()
exam_second.writing_grade = 88
print('first exam writing', exam.writing_grade) #first exam 88
print('second exam writing', exam_second.writing_grade) # second exam 88
print('first exam math',exam.math_grade)
