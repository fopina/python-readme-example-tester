import unittest

from . import sample_pump_it_up


class TestSomeSample(unittest.TestCase):
    def test_it(self):
        self.assertEqual(sample_pump_it_up.pump_it_up(2), 102)
