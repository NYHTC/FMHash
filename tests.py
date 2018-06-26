"""Unittest test suite."""

import unittest
from FMHash import escape, hash, unescape


class TestInputEscape(unittest.TestCase):
    """Test escaping FMHash inputs."""

    def test_escape_equal(self):
        """Test escaping string with an equal sign."""
        self.assertEqual(escape('a=b'), 'a/=b')

    def test_escape_escaped_equal(self):
        """Test escaping string with and already-escapred equal sign."""
        self.assertEqual(escape('a/=b'), 'a//=b')

    def test_escape_colon(self):
        """Test escaping string with and a colon."""
        self.assertEqual(escape('a:b'), 'a/:b')

    def test_escape_dict_open(self):
        """Test escaping string with less-than sign."""
        self.assertEqual(escape('a<b'), 'a/<b')

    def test_escape_dict_close(self):
        """Test escaping string with greater-than sign."""
        self.assertEqual(escape('a>b'), 'a/>b')

    def test_escape_empty_input(self):
        """Test escaping empty string."""
        self.assertEqual(escape(''), '')


class TestInputUnescape(unittest.TestCase):
    """Test unescaping FMHash inputs."""

    def test_unescape_equal(self):
        """Test unescaping string with equal sign."""
        self.assertEqual(unescape('a/=b'), 'a=b')

    def test_unescape_escaped_equal(self):
        """Test unescaping double-escaped equal sign."""
        self.assertEqual(unescape('a//=b'), 'a/=b')

    def test_unescape_colon(self):
        """Test unescaping string with an escaped colon."""
        self.assertEqual(unescape('a/:b'), 'a:b')

    def test_unescape_dict_open(self):
        """Test unescaping string with an escaped less-than sign."""
        self.assertEqual(unescape('a/<b'), 'a<b')

    def test_unescape_dict_close(self):
        """Test unescaping string with an escaped greater-than sign."""
        self.assertEqual(unescape('a/>b'), 'a>b')

    def test_escape_empty_input(self):
        """Test unescaping string an empty string."""
        self.assertEqual(unescape(''), '')


class TestHashKeyValuePairs(unittest.TestCase):
    """Test FMHash hash function."""

    def test_hash_key_value_pair(self):
        """Test hash function."""
        self.assertEqual(hash('name', 'bob'), '<:name:=bob:>')


if __name__ == '__main__':
    unittest.main()
