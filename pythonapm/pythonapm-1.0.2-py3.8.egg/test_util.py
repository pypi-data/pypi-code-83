import os
import unittest
from unittest import mock
from .util import (
    current_milli_time, 
    is_callable,is_digit,
    is_empty_string,
    is_non_empty_string, 
    is_allowed_url,
    get_normalized_url
)

class UtilTest(unittest.TestCase):
    def test_current_milli_time(self):
        millis = current_milli_time()
        self.assertTrue(type(millis) is int)
    
    def test_is_callable(self):
        
        self.assertFalse(is_callable({}))
        self.assertFalse(is_callable(10))
        self.assertFalse(is_callable(''))
        self.assertFalse(is_callable(None))
        self.assertTrue(is_callable(list))
    
    def test_is_digit(self):
        self.assertFalse(is_digit(None))
        self.assertTrue(is_digit(9))
        self.assertTrue(is_digit('9'))
    
    def test_is_empty_string(self):
        self.assertFalse(is_empty_string(None))
        self.assertFalse(is_empty_string('not empty'))
        self.assertFalse(is_empty_string(1))
        self.assertFalse(is_empty_string(['str']))
        self.assertTrue(is_empty_string(''))
    
    def test_is_non_empty_string(self):
        self.assertFalse(is_non_empty_string(None))
        self.assertFalse(is_non_empty_string([]))
        self.assertFalse(is_non_empty_string(''))
        self.assertTrue(is_non_empty_string('str'))

    def test_is_allowed_url(self):
        self.assertFalse(is_allowed_url(''))
        self.assertFalse(is_allowed_url('/abc/a.js'))
        self.assertFalse(is_allowed_url('/abc/a.css'))
        self.assertFalse(is_allowed_url('/abc/a.gif'))
        self.assertFalse(is_allowed_url('/abc/a.jpg'))
        self.assertFalse(is_allowed_url('/abc/a.jpeg'))
        self.assertFalse(is_allowed_url('/abc/a.bmp'))
        self.assertFalse(is_allowed_url('/abc/a.png'))
        self.assertFalse(is_allowed_url('/abc/a.ico'))
        self.assertTrue(is_allowed_url('/abc/a.html'))
        self.assertTrue(is_allowed_url('/api/list'))

    def test_get_normalized_url(self):
        self.assertEqual(get_normalized_url(''), '')
        self.assertEqual(get_normalized_url('/api/123/name'), '/api/*/name')
        self.assertEqual(get_normalized_url('/api/123ab/name'), '/api/123ab/name')
        self.assertEqual(get_normalized_url('/api/123/name/345'), '/api/*/name/345')
        self.assertEqual(get_normalized_url('/api/123/name/345/list'), '/api/*/name/*/list')




        
       