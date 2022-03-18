'''
way to unit test backend functions

'''
import sys

sys.path.append('/backend')

import unittest
from recognition import OffsetListCreate

class TestRecgnition(unittest.TestCase):
    def test_OffsetListCreate(self):
        result OffsetListCreate()