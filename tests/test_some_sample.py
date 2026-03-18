import unittest

from . import some_sample


class TestSomeSample(unittest.TestCase):
    def test_it(self):
        self.assertEqual(some_sample.pump_it_up(2), 102)
