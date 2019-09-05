# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle


# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    # Right
    def testRightTriangleA(self):
        self.assertEqual('Right', classifyTriangle(3, 4, 5), '3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual('Right', classifyTriangle(5, 3, 4), '5,3,4 is a Right triangle')

    def testRightTriangleC(self):
        self.assertEqual('Right', classifyTriangle(4, 5, 3), '4,5,3 is a Right triangle')

    # Equilateral
    def testEquilateralTriangleA(self):
        self.assertEqual('Equilateral', classifyTriangle(1, 1, 1), '1,1,1 should be equilateral')

    def testEquilateralTriangleB(self):
        self.assertEqual('Equilateral', classifyTriangle(199, 199, 199), '199,199,199 should be equilateral')

    # Isosceles
    def testIsoscelesTriangleA(self):
        self.assertEqual('Isosceles', classifyTriangle(4, 4, 2), '4,4,2 should be isosceles')

    def testIsoscelesTriangleB(self):
        self.assertEqual('Isosceles', classifyTriangle(2, 4, 4), '2,4,4 should be isosceles')

    def testIsoscelesTriangleC(self):
        self.assertEqual('Isosceles', classifyTriangle(4, 2, 4), '4,2,4 should be isosceles')

    # Scalene
    def testScaleneTriangleA(self):
        self.assertEqual('Scalene', classifyTriangle(7, 4, 6), '7,4,6 should be scalene')

    def testScaleneTriangleB(self):
        self.assertEqual('Scalene', classifyTriangle(6, 4, 7), '6,4,7 should be scalene')

    def testScaleneTriangleC(self):
        self.assertEqual('Scalene', classifyTriangle(4, 6, 7), '4,6,7 should be scalene')

    # InvalidInput
    def testInvalidInputA(self):
        self.assertEqual('InvalidInput', classifyTriangle(1, 1, 201), '1,1,201 should be InvalidInput')

    def testInvalidInputB(self):
        self.assertEqual('InvalidInput', classifyTriangle(-1, 1, 1), '-1,1,1 should be InvalidInput')

    def testInvalidInputC(self):
        self.assertEqual('InvalidInput', classifyTriangle(1, 'A', 1), '1,A,1 should be InvalidInput')

    # NotATriangle
    def testNotATriangleA(self):
        self.assertEqual('NotATriangle', classifyTriangle(100, 1, 1), '100,1,1 should be NotATriangle')

    def testNotATriangleB(self):
        self.assertEqual('NotATriangle', classifyTriangle(1, 100, 1), '1,100,1 should be NotATriangle')

    def testNotATriangleC(self):
        self.assertEqual('NotATriangle', classifyTriangle(1, 1, 100), '1,1,100 should be NotATriangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
