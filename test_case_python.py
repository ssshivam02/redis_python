from unit_tests import addition
import unittest

# from unittest import mock
# @mock.patch('here we pass path of file and fuction too')
# def test_mocking(mock_variable,then any fixture):
#     mock_variable.return_value=  True

class TestAddition(unittest.TestCase):
    def test_addition(self):
        expected_value = 10
        print(expected_value)
        self.assertEqual(expected_value, addition(5,5))

    def test_addition_failed(self):
        expected_value = 10
        print(expected_value)
        self.assertEqual(expected_value, addition(5,6))