#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import isbn_converter


class TestIsbnConverter(unittest.TestCase):
    """
    unittest for isbn_converter module.
    """
    def setUp(self):
        """
        test data.
        """
        self.isbn_10_valid_data = [
            '754043449X',
            '7810961063',
            '7300039480',
            '7219049080'
        ]

        self.isbn_10_valid_data_converted = [
            '9787540434496',
            '9787810961066',
            '9787300039480',
            '9787219049082'
        ]

        self.isbn_13_valid_data = [
            '9787302274759',
            '9787515301723',
            '9787301199800',
            '9787302273158'
        ]

        self.isbn_13_valid_data_converted = [
            '7302274754',
            '7515301724',
            '7301199805',
            '7302273154'
        ]

        self.isbn_10_invalid_data = [
            'a1fa',
            'aaaaaaaaaa',
            '754043449x',
            '7208990898'
        ]

        self.isbn_13_invalid_data = [
            'af3jf',
            'bbbbbbbbbbbbb',
            '978730227315X',
            '9787238082399'
        ]

    def test_is_isbn10_valid(self):
        """
        unittest for isbn_converter.is_isbn10_valid().
        """
        for isbn in self.isbn_10_valid_data:
            self.assertTrue(isbn_converter.is_isbn10_valid(isbn),
                            "func:is_isbn10_valid test failed -- %s " % (isbn))
        for isbn in self.isbn_10_invalid_data:
            self.assertFalse(isbn_converter.is_isbn10_valid(isbn),
                             "func:is_isbn10_valid test failed -- %s" % (isbn))

    def test_is_isbn13_valid(self):
        """
        unittest for isbn_converter.is_isbn13_valid().
        """
        for isbn in self.isbn_13_valid_data:
            self.assertTrue(isbn_converter.is_isbn13_valid(isbn),
                            "func:is_isbn13_valid test failed -- %s" % (isbn))
        for isbn in self.isbn_13_invalid_data:
            self.assertFalse(isbn_converter.is_isbn13_valid(isbn),
                             "func:is_isbn13_valid test failed -- %s" % (isbn))

    def test_isbn13_to_isbn10(self):
        """
        unittest for isbn_converter.is_isbn13_to_isbn10().
        """
        for isbn, isbn_converted in zip(self.isbn_13_valid_data,
                                        self.isbn_13_valid_data_converted):
            self.assertEqual(isbn_converter.isbn13_to_isbn10(isbn),
                             isbn_converted)

    def test_isbn10_to_isbn13(self):
        """
        unittest for isbn_converter.is_isbn10_to_isbn13().
        """
        for isbn, isbn_converted in zip(self.isbn_10_valid_data,
                                        self.isbn_10_valid_data_converted):
            self.assertEqual(isbn_converter.isbn10_to_isbn13(isbn),
                             isbn_converted)


if __name__ == '__main__':
    unittest.main()
