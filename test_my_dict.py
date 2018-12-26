#!usr/bin/env python3
# -*- coding:utf-8 -*-
import unittest
from my_dict import Dict


class Test_Dict(unittest.TestCase):
    def test_init(self):
        a, b = 1, 'test'
        d = Dict(a=a, b=b)
        self.assertEqual(d.a, a, ('value is err,d.a not equal %s', a))
        self.assertEqual(d.b, 'test', ('value is err,d.a not equal %s', a))
        self.assertTrue(isinstance(d, Dict))


    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')
