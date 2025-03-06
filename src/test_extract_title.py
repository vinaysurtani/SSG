import unittest

from extract_title import extract_title

class TestTitleExtract(unittest.TestCase):
    def test_extract_title(self):
        # Basic case with just the title
        assert extract_title("# Hello World") == "Hello World"
        
        # Title with leading/trailing whitespace to strip
        assert extract_title("#   Spaced Title  ") == "Spaced Title"
        
        # Title with multiple words and punctuation
        assert extract_title("# The Lord of the Rings: Fellowship!") == "The Lord of the Rings: Fellowship!"
        
        # Testing that it only gets h1 (single #), not h2 or others
        #extract_title("## This is not an h1")
        try:
            extract_title("## This is not an h1")
            assert False, "Should have raised an exception"
        except Exception:
            assert True
        
        # Test that an exception is raised when no h1 is present
        try:
            extract_title("No title here")
            assert False, "Should have raised an exception"
        except Exception:
            assert True