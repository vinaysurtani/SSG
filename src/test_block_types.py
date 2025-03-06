import unittest

from block_types import BlockType, block_to_block_type

class TestBlockTypes(unittest.TestCase):
    def test_paragraph(self):
        # Regular paragraph
        self.assertEqual(block_to_block_type("This is a regular paragraph."), BlockType.paragraph)
        # Empty string
        self.assertEqual(block_to_block_type(""), BlockType.paragraph)
        # Single word
        self.assertEqual(block_to_block_type("Hello"), BlockType.paragraph)

    def test_heading(self):
        # Level 1 heading
        self.assertEqual(block_to_block_type("# Heading 1"), BlockType.heading)
        # Level 3 heading
        self.assertEqual(block_to_block_type("### Heading 3"), BlockType.heading)
        # Level 6 heading
        self.assertEqual(block_to_block_type("###### Heading 6"), BlockType.heading)
        # Invalid heading (no space after #)
        self.assertEqual(block_to_block_type("#NoSpace"), BlockType.paragraph)
        # Invalid heading (too many #)
        self.assertEqual(block_to_block_type("####### Too many"), BlockType.paragraph)

    def test_code(self):
        # Simple code block
        self.assertEqual(block_to_block_type("```\ncode here\n```"), BlockType.code)
        # Multi-line code block
        self.assertEqual(block_to_block_type("```\nline 1\nline 2\n```"), BlockType.code)
        # Code block with language specified
        self.assertEqual(block_to_block_type("```python\ndef hello():\n    print('hello')\n```"), BlockType.code)
        # Not a valid code block (only opening backticks)
        self.assertEqual(block_to_block_type("```\nunclosed code"), BlockType.paragraph)

    def test_quote(self):
        # Simple quote
        self.assertEqual(block_to_block_type(">This is a quote"), BlockType.quote)
        # Multi-line quote
        self.assertEqual(block_to_block_type(">Line 1\n>Line 2\n>Line 3"), BlockType.quote)
        # Quote with spaces after >
        self.assertEqual(block_to_block_type("> This is a quote with space"), BlockType.quote)
        # Not a valid quote (missing > on second line)
        self.assertEqual(block_to_block_type(">Line 1\nLine 2"), BlockType.paragraph)

    def test_unordered_list(self):
        # Simple unordered list
        self.assertEqual(block_to_block_type("- Item 1"), BlockType.unordered_list)
        # Multi-item unordered list
        self.assertEqual(block_to_block_type("- Item 1\n- Item 2\n- Item 3"), BlockType.unordered_list)
        # Not a valid unordered list (missing space after -)
        self.assertEqual(block_to_block_type("-Item 1"), BlockType.paragraph)
        # Not a valid unordered list (inconsistent format)
        self.assertEqual(block_to_block_type("- Item 1\nItem 2"), BlockType.paragraph)

    def test_ordered_list(self):
        # Simple ordered list
        self.assertEqual(block_to_block_type("1. Item 1"), BlockType.ordered_list)
        # Multi-item ordered list
        self.assertEqual(block_to_block_type("1. Item 1\n2. Item 2\n3. Item 3"), BlockType.ordered_list)
        # Not a valid ordered list (doesn't start with 1)
        self.assertEqual(block_to_block_type("2. Item 2"), BlockType.paragraph)
        # Not a valid ordered list (incorrect sequence)
        self.assertEqual(block_to_block_type("1. Item 1\n3. Item 3"), BlockType.paragraph)
        # Not a valid ordered list (non-sequential)
        self.assertEqual(block_to_block_type("1. Item 1\n2. Item 2\n4. Item 4"), BlockType.paragraph)
        # Not a valid ordered list (inconsistent format)
        self.assertEqual(block_to_block_type("1. Item 1\nItem 2"), BlockType.paragraph)