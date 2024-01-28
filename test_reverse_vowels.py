import pytest
from reverse_vowels import Solution
import unittest

def test_reverseVowels():
    s = "hello"
    obj= Solution()
    reverse_string=obj.reverseVowels(s)
    assert("holle", reverse_string)