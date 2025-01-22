import unittest
from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_no_delimiter(self):
        node = TextNode("plain text", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "plain text")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)

    def test_one_code_delimiter(self):
        node = TextNode("hello `code` world", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "hello ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text, "code")
        self.assertEqual(nodes[1].text_type, TextType.CODE)
        self.assertEqual(nodes[2].text, " world")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)

    def test_one_bold_delimiter(self):
        node = TextNode("hello **bold** world", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "hello ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text, "bold")
        self.assertEqual(nodes[1].text_type, TextType.BOLD)
        self.assertEqual(nodes[2].text, " world")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)

    def test_two_bold_delimiter(self):
        node = TextNode("hello **bold** world **bolder** universe", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(nodes), 5)
        self.assertEqual(nodes[0].text, "hello ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text, "bold")
        self.assertEqual(nodes[1].text_type, TextType.BOLD)
        self.assertEqual(nodes[2].text, " world ")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)
        self.assertEqual(nodes[3].text, "bolder")
        self.assertEqual(nodes[3].text_type, TextType.BOLD)
        self.assertEqual(nodes[4].text, " universe")
        self.assertEqual(nodes[4].text_type, TextType.TEXT)

    def test_invalid_markdown_unclosed(self):
        node = TextNode("hello `code", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_invalid_markdown_unopened(self):
        node = TextNode("hello code`", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_invalid_markdown_mismatched(self):
        node = TextNode("hello *bitallic?**", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)
