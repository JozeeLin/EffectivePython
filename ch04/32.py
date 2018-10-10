#!/usr/bin/env python
# coding=utf-8
class LazyDB(object):
    def __init__(self):
        self.exists = 5

    def __getattr__(self, name):
        value = 'Value for %s' % name
        setattr(self, name, value)
        return value

# 1==================
#data = LazyDB()
#print('Before:', data.__dict__)
#print('foo:  ', data.foo)
#print('After: ', data.__dict__)


class LoggingLazyDB(LazyDB):
    def __getattr__(self, name):
        print('Called __getattr__(%s)' % name)
        return super().__getattr__(name)

# 2===================
#data = LoggingLazyDB()
#print('exists:', data.exists)
#print('foo:', data.foo)
#print('foo:', data.foo)


class ValidatingDB(object):
    def __init__(self):
        self.exists = 5

    def __getattribute__(self, name):
        print('Called __getattribute__(%s)' % name)
        try:
            return super().__getattribute__(name)
        except AttributeError:
            value = 'Value for %s' % name
            setattr(self, name, value)
            return value
#3 =================
#data = ValidatingDB()
#print('exists:', data.exists)
#print('foo:  ', data.foo)
#print('foo:  ', data.foo)


class SavingDB(object):
    def __setattr__(self, name, value):
        super().__setattr__(name, value)

class LoggingSavingDB(SavingDB):
    def __setattr__(self, name, value):
        print('Called __setattr__(%s, %r)' % (name, value))
        super().__setattr__(name, value)


# 4============================
#data = LoggingSavingDB()
#print('Before: ', data.__dict__)
#data.foo = 5
#print('After: ', data.__dict__)
#data.foo = 7
#print('Finally: ', data.__dict__)
#print('='*40)
#print(data.foo)


class DictionaryDB(object):
    def __init__(self, data):
        self._data = data

    def __getattribute__(self, name):
        data_dict = super().__getattribute__('_data')
        return data_dict[name]


data = DictionaryDB({'foo':3})
print(data.foo)
