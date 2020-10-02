import unittest

#This is a simple test to test the simple function
#Importing the function for use in the test
from main import func

#Test the function
class TestSimpleFunction(unittest.TestCase):
    def test_answer(self):
        self.assertEqual(func(4), 5)
