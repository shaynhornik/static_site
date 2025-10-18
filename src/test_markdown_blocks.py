import unittest
from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType, extract_title


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.ULIST)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.OLIST)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_extract_title_single_h1(self):
        md = """
# This is a title

This is just a regular paragraph
** This is bold text**
"""
        self.assertEqual(extract_title(md), "This is a title")

    def test_extract_title_multiple_h1(self):
        md = """
# This is a title
# This is a second title

This is just a regular paragraph
"""
        with self.assertRaises(Exception) as cm:
            extract_title(md)
        self.assertIn("Multiple Titles", str(cm.exception))


    def test_extract_title_no_h1(self):
        md = """
This is not a title
There is no title
lolololol
"""
        with self.assertRaises(Exception) as cm:
            extract_title(md)
        self.assertIn("No Title", str(cm.exception))

    def test_extract_title_no_space(self):
        md = """
#There is no space for this title
"""

        with self.assertRaises(Exception) as cm:
            extract_title(md)
        self.assertIn("No Title", str(cm.exception))

    def test_extract_title_double_hashtags(self):
        md = """
##This is an invalid title
"""

        with self.assertRaises(Exception) as cm:
            extract_title(md)
        self.assertIn("No Title", str(cm.exception))

    def test_extract_title_double_hashtags_and_space(self):
        md = """
## This is an invalid title
"""

        with self.assertRaises(Exception) as cm:
            extract_title(md)
        self.assertIn("No Title", str(cm.exception)) 
