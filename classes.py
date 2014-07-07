#!/bin/bash

class Parent(object):

    CONSTANT_1 = 1
    CONSTANT_2 = 2

    def __init__(self):
        print self.CONSTANT_1
        i = dir(self)
        print i

class Kid(Parent):

    def __init__(self):
        print self.CONSTANT_1

if __name__ == "__main__":
    p = Parent()
    k = Kid()
