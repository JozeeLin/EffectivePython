#!/usr/bin/env python
# coding=utf-8
import json

class Serializable(object):
    def __init__(self, *args):
        self.args = args

    def serialize(self):
        return json.dumps({'args':self.args})

class Point2D(Serializable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point2D(%d, %d)' % (self.x, self.y)


# 1=======================
#point = Point2D(5, 3)
#print('Object: ', point)
#print('Serialized: ', point.serialize())


# 2=========================
class Deserializable(Serializable):

    @classmethod
    def deserialize(cls, json_data):
        params = json.loads(json_data)
        return cls(*params['args'])

    def show_value(self):
        print('Deserializable show value:',self.x, self.y)


class BetterPoint2D(Deserializable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

    def __repr__(self):
        #这里的类名称应该写成BetterPointD而不是Point2D
        return 'BetterPoint2D(%d, %d)' % (self.x, self.y)


# 3===================
#point = BetterPoint2D(5,3)
#print('Before:  ', point)
#data = point.serialize()
#print('Serialized:', data)
#after = BetterPoint2D.deserialize(data)
#print('After:  ', after)
#after.show_value()


class BetterSerializable(object):
    def __init__(self, *args):
        self.args = args

    def serialize(self):
        return json.dumps({'args':self.args,'class':self.__class__.__name__})

    def __repr__(self):
        #这里的类名称应该写成BetterPointD而不是Point2D
        return 'BetterPoint2D(%d, %d)' % (self.x, self.y)


registry = {}
def registry_class(target_class):
    registry[target_class.__name__] = target_class


def deserialize(data):
    params = json.loads(data)
    name = params['class']
    target_class = registry[name]
    return target_class(*params['args'])


class Meta(type):
    def __new__(meta, name, bases, class_dict):
        cls = type.__new__(meta, name, bases, class_dict) #先创键出一个类的基本类型对象
        registry_class(cls)
        return cls

#class RegisteredSerializable(BetterSerializable, metaclass=Meta):
#    pass

#class Vector3D(RegisteredSerializable):
class Vector3D(BetterSerializable, metaclass=Meta):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)
        self.x, self.y, self.z = x,y,z

v3 = Vector3D(10, -7, 3)
print('Before:  ', v3)
data = v3.serialize()
print('Serialized:  ', data)
print('After: ', deserialize(data))
