import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)


    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)


    def test_url_difference(self):
        node1 = TextNode("Click here", TextType.BOLD, "https://example.com")
        node2 = TextNode("Click here", TextType.BOLD, None)
        self.assertNotEqual(node1, node2)

        


if __name__ == "__main__":
    unittest.main()
