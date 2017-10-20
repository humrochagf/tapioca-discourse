# coding: utf-8

import unittest

from tapioca_discourse import Discourse


class TestTapiocaDiscourse(unittest.TestCase):

    def setUp(self):
        self.wrapper = Discourse()


if __name__ == '__main__':
    unittest.main()
