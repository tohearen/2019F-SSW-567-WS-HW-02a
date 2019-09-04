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

    def testRightTriangleA(self):
        self.assertEqual('Right', classifyTriangle(3, 4, 5), '3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual('Right', classifyTriangle(5, 3, 4), '5,3,4 is a Right triangle')

    def testEquilateralTriangleA(self):
        self.assertEqual('Equilateral', classifyTriangle(1, 1, 1), '1,1,1 should be equilateral')

    def testEquilateralTriangleB(self):
        self.assertEqual('Equilateral', classifyTriangle(100, 100, 100), '100,100,100 should be equilateral')

    def testIsoscelesTriangleA(self):
        self.assertEqual('Equilateral', classifyTriangle(1, 1, 2), '1,1,2 should be isosceles')

    def testIsoscelesTriangleB(self):
        self.assertEqual('Isosceles', classifyTriangle(2, 1, 1), '2,1,1 should be isosceles')

    def testScaleneTriangleA(self):
        self.assertEqual('Scalene', classifyTriangle(1, 1, 2), '1,1,2 should be scalene')

    def testScaleneTriangleB(self):
        self.assertEqual('Scalene', classifyTriangle(1, 2, 3), '1,2,3 should be scalene')

    def testInvalidInputA(self):
        self.assertEqual('InvalidInput', classifyTriangle(1, 1, 201), '1,1,201 should be InvalidInput')

    def testInvalidInputB(self):
        self.assertEqual('InvalidInput', classifyTriangle(-1, 1, 1), '-1,1,1 should be InvalidInput')

    def testInvalidInputC(self):
        self.assertEqual('InvalidInput', classifyTriangle('A', 1, 1), 'A,1,1 should be InvalidInput')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
