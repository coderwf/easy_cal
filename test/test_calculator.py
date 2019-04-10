# -*- coding:utf-8 -*-

import unittest
from calculator.interpreter import Calculator


class TestCal(unittest.TestCase):
    def test_cal(self):
        text = "a=10;a+=10;b=40;b+=a"
        self.assertEqual(Calculator.calculate(text), 60)
        text += "; b*=a"
        self.assertEqual(Calculator.calculate(text), 1200)

    def test_func(self):
        text = "a=20;b=20;c=100;AVG(a,b+c)"
        self.assertEqual(Calculator.calculate(text), 70)
        self.assertEqual(Calculator.calculate("SUM(10,10,AVG(20,40))"), 50)
        self.assertEqual(Calculator.calculate("b=10;b**=2;b/=2"), 50)
        self.assertEqual(Calculator.calculate("a=10;b=20;a+=b+=10"), 40)