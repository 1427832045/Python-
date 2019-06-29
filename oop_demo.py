#!/user/bin/env python3
# -*- coding: utf-8 -*-

# 定义一个类，类名为Student
class Student(object):
    count = 0  # 类属性，所有实例共享
    def __init__(self, sno, name):
        '''初始化方法，或者叫构造器，对属性进行初始化

        '''
        self.sno = sno  # 实例属性，属于每个对象，每个对象都有一份
        self.name = name
        Student.count += 1   
    
    def show(self):
        print(self.name, self.sno)

s1 = Student(1001, "张三")  # 定义对象s1，将调用__init__方法对属性进行赋值
s1.show()  # 调用s1的show方法
s1.age = 33
s1.qq = '1427832045'
print(s1.age, s1.qq)

s2 = Student(1002, "李四")
print(s1.count)


class Dog:
    def show(self):
        print("我是猫星人~~~~~")
class Fish:
    def show(self):
        print("我是小鱼人")


def show(p):
    p.show()

show(s1)
show(Dog())
show(Fish())