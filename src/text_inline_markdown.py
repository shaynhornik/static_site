import text_to_textnodes from inline_markdown

# language: python
import unittest

from inline_markdown import text_to_textnodes
from textnode import TextNode, TextType

class TestInlineMarkdown(unittest.TestCase):
    def test_mixed_content(self):
        text = "This is **bold** and _ital_ and `code` and ![alt](img) and [link](url)"
        nodes = text_to_textnodes(text)

        self.assertIsInstance(nodes, list)
        self.assertGreater(len(nodes), 0)

        # types present
        types = {n.text_type for n in nodes}
        self.assertIn(TextType.BOLD, types)
        self.assertIn(TextType.ITALIC, types)
        self.assertIn(TextType.CODE, types)
        self.assertIn(TextType.IMAGE, types)
        self.assertIn(TextType.LINK, types)

        # spot checks
        self.assertTrue(any(n.text == "bold" and n.text_type == TextType.BOLD for n in nodes))
        self.assertTrue(any(n.text == "ital" and n.text_type == TextType.ITALIC for n in nodes))
        self.assertTrue(any(n.text == "code" and n.text_type == TextType.CODE for n in nodes))
        self.assertTrue(any(n.text == "alt" and n.text_type == TextType.IMAGE and n.url == "img" for n in nodes))
        self.assertTrue(any(n.text == "link" and n.text_type == TextType.LINK and n.url == "url" for n in nodes))

        # no empty TEXT nodes
        self.assertFalse(any(n.text_type == TextType.TEXT and n.text == "" for n in nodes))

    def test_plain_text(self):
        text = "No formatting here."
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, [TextNode("No formatting here.", TextType.TEXT)])

    def test_unmatched_delimiters_does_not_crash(self):
        text = "Bad **bold and `_code"
        try:
            nodes = text_to_textnodes(text)
        except Exception as e:
            self.fail(f"text_to_textnodes raised unexpectedly: {e}")
        self.assertIsInstance(nodes, list)
        self.assertGreater(len(nodes), 0)

if __name__ == "__main__":
    unittest.main()
