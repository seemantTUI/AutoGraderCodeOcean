from .exercise import *
import unittest
import pip

from . import chat_gpt_request


class ExerciseTests(unittest.TestCase):
    def test_even(self):
        exceptions = []
        for x in [1, 3, 5, 7, 9]:
            try:
                self.assertFalse(even(x))
            except Exception as e:
                exceptions.append("Error for {}: {}".format(x, e))

        for x in [2, 4, 6, 8, 10]:
            try:
                self.assertTrue(even(x))
            except Exception as e:
                exceptions.append("Error for {}: {}".format(x, e))

        if exceptions:
            exceptions_string = '\n'.join(exceptions)

            gpt_response = chat_gpt_request.get_completion(exceptions_string)
            print(gpt_response)
            self.assertEqual(gpt_response, [])

    def test_odd(self):
        exceptions = []
        for x in [1, 3, 5, 7, 9]:
            try:
                self.assertTrue(odd(x))
            except Exception as e:
                exceptions.append("Error for {}: {}".format(x, e))

        for x in [2, 4, 6, 8, 10]:
            try:
                self.assertFalse(odd(x))
            except Exception as e:
                exceptions.append("Error for {}: {}".format(x, e))

        if exceptions:
            exceptions_string = '\n'.join(exceptions)

            gpt_response = chat_gpt_request.get_completion(exceptions_string)
            print(gpt_response)
            self.assertEqual(gpt_response, [])