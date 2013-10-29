#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def is_isbn10_valid(isbn):
    """
    Check ISBN-10 is valid.
    Code Implementaion from:
    http://en.wikipedia.org/wiki/International_Standard_Book_Number
    """
    if len(isbn) != 10:
        return False
    if ((not isbn[0:9].isdigit()) or
            ((isbn[-1] != 'X') and (not isbn[-1].isdigit()))):
        return False
    result = sum((10 - i) * (int(x) if x != 'X' else 10)
                 for i, x in enumerate(isbn))
    return result % 11 == 0


def is_isbn13_valid(isbn):
    """
    Check ISBN-13 is valid.
    Code Implemetation from:
    http://en.wikipedia.org/wiki/International_Standard_Book_Number
    """
    if len(isbn) != 13 or isbn.isdigit() is not True:
        return False
    check = (10 - (sum(int(digit) * (3 if idx % 2 else 1)
                       for idx, digit in enumerate(isbn[:12])) % 10)) % 10
    return check == int(isbn[-1])


def isbn13_to_isbn10(isbn13_str):
    """
    Convert ISBN-13 to ISBN-10.
    """
    num = 11 - sum((10 - i) * (int(x))
                   for i, x in enumerate(isbn13_str[3:12])) % 11
    if num == 10:
        check_digit = 'X'
    elif num == 11:
        check_digit = 0
    else:
        check_digit = num
    return isbn13_str[3:12] + str(check_digit)


def isbn10_to_isbn13(isbn10_str):
    """
    Convert ISBN-10 to ISBN-13.
    """
    check_digit = (
        10 - (sum(int(digit) * (3 if idx % 2 else 1)
                  for idx, digit in enumerate('978' + isbn10_str[:9])
                  ) % 10)) % 10
    return '978' + isbn10_str[:9] + str(check_digit)


def isbn_converter(isbn):
    """
    Convert isbn format to another format.
    """
    if is_isbn10_valid(isbn):
        result = isbn10_to_isbn13(isbn)
    elif is_isbn13_valid(isbn):
        result = isbn13_to_isbn10(isbn)
    else:
        return None
    return result


if __name__ == "__main__":
    for isbn_str in sys.argv[1:]:
        the_result = isbn_converter(isbn_str)
        if the_result:
            print the_result
        else:
            print "Bad ISBN " + isbn_str
