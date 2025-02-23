#!/usr/bin/python3
import unittest

class Test_console(unittest.TestCase):
    def test_create_with_string_param(self):
        self.assertFalse("MyClass" in self.capt_output("create MyClass name='Hello World'"))
        self.assertTrue("MyClass" in self.capt_output("all MyClass"))
        self.assertTrue("'name': 'Hello World'" in self.capt_output("show MyClass"))

    def test_create_with_float_param(self):
        self.assertFalse("MyClass" in self.capt_output("create MyClass price=9.99"))
        self.assertTrue("MyClass" in self.capt_output("all MyClass"))
        self.assertTrue("'price': 9.99" in self.capt_output("show MyClass"))

    def test_create_with_integer_param(self):
        self.assertFalse("MyClass" in self.capt_output("create MyClass quantity=10"))
        self.assertTrue("MyClass" in self.capt_output("all MyClass"))
        self.assertTrue("'quantity': 10" in self.capt_output("show MyClass"))

    def test_create_with_invalid_param(self):
        self.assertFalse("MyClass" in self.capt_output("create MyClass invalid=abc"))
        self.assertFalse("MyClass" in self.capt_output("all MyClass"))

