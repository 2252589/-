# -*- coding: utf-8 -*-
"""
Created on Sun May 14 13:32:37 2023

@author: 86166
"""

class Rect:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def sum_area(self, other_rect):
        return self.area() + other_rect.area()
r1 = Rect(4, 5)
r2 = Rect(3, 6)

print("矩形1的周长: ", r1.perimeter())
print("矩形1的面积: ", r1.area())
print("矩形2的周长: ", r2.perimeter())
print("矩形2的面积: ", r2.area())
print("两个矩形的面积和: ", r1.sum_area(r2))
