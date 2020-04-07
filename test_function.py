#!/usr/bin/env python
# coding=utf-8


'''
@Description:
@Version    :0.1
@CreateTime :2020/03/12 Thursday 09:50:59
@Author     :Le
@LastEditor :
@EditTime   :
'''


import unittest
from name import formatted_name as fname


class TestNameCase(unittest.TestCase):

    def setUp(self):
        self.formatted_name = fname('jack', 'steven')

    def test_full_name(self):
        self.assertEqual(self.formatted_name, 'Jack Steven')


if __name__ == "__main__":
    unittest.main()
