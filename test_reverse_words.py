import pytest
from reverse_words import Solution
import unittest

def test_reverseWords():
    s = "  hello world  "
    obj= Solution()
    reverse_string=obj.reverseWords(s)
    assert("world hello", reverse_string)