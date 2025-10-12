import unittest
from textnode import TextNode, TextType
from node_delimiter import split_nodes_delimiter, extract_markdown_images, extract_markdown_links

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_simple_code(self):
        nodes = [TextNode("hello `x` world", TextType.TEXT)]
        out = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(
            out,
            [TextNode("hello ", TextType.TEXT),
             TextNode("x", TextType.CODE),
             TextNode(" world", TextType.TEXT)]
        )

    def test_multiple_pairs(self):
        nodes = [TextNode("a `x` b `y` c", TextType.TEXT)]
        out = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(
            out,
            [TextNode("a ", TextType.TEXT),
             TextNode("x", TextType.CODE),
             TextNode(" b ", TextType.TEXT),
             TextNode("y", TextType.CODE),
             TextNode(" c", TextType.TEXT)]
        )

    def test_unmatched_raises(self):
        nodes = [TextNode("bad `x y", TextType.TEXT)]
        with self.assertRaises(ValueError):
            split_nodes_delimiter(nodes, "`", TextType.CODE)

    def test_no_delimiter_passthrough(self):
        nodes = [TextNode("no specials here", TextType.TEXT)]
        out = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(out, [TextNode("no specials here", TextType.TEXT)])

    def test_non_text_nodes_unchanged(self):
        nodes = [
            TextNode("already bold", TextType.BOLD),
            TextNode("and `code` here", TextType.TEXT),
        ]
        out = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(
            out,
            [TextNode("already bold", TextType.BOLD),
             TextNode("and ", TextType.TEXT),
             TextNode("code", TextType.CODE),
             TextNode(" here", TextType.TEXT)]
        )

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

if __name__ == "__main__":
    unittest.main()

