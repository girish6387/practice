from question10 import sample_func
import unittest
import pytest


class TestCode(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(sample_func(3), [[2, 0, 1, 1.0], [4, 0, 4, 1.0], [6, 0, 9, 1.0]])
        assert 2==2

    def test_negative(self):
        try:
            assert sample_func("#")
        except:
            print("must be integer")  
        
    def test_exception(self):
        with pytest.raises(Exception):
            assert sample_func(0)


