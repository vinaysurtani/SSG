import unittest
from markdown_parser import extract_markdown_images, extract_markdown_links

class TestMDParser(unittest.TestCase):
    def test_eq(self):
        test_text = """
                    Here's a normal [link](url.com)
                    Here's an ![image](img.com)
                    Here's a [link with [brackets]](url.com)
                    Here's a [link with (parentheses)](url.com)
                    Here's a [broken [link](url.com)
                    """
        self.assertEqual(extract_markdown_images(test_text),[('image','img.com')])
        self.assertEqual(extract_markdown_links(test_text),[('link', 'url.com'), ('link with (parentheses)', 'url.com'), ('link', 'url.com')])

if __name__ == "__main__":
    unittest.main()