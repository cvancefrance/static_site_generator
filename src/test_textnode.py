import unittest

from textnode import TextNode, TextType, text_node_to_html_node


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

    def test_text_node_to_html_node_text(self):
        text_node = TextNode("Regular text", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "")
        self.assertEqual(html_node.value, "Regular text")

    def test_text_node_to_html_node_bold(self):
        text_node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold text")

    def test_text_node_to_html_node_italic(self):
        text_node = TextNode("Italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Italic text")
        
    def test_text_node_to_html_node_code(self):
        text_node = TextNode("coding", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "coding")

    def test_text_node_to_html_node_link(self):
        text_node = TextNode("link_text", TextType.LINK, "www.google.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "link_text")
        self.assertEqual(html_node.props, {"href": "www.google.com"})

    def test_text_node_to_html_node_image(self):
        text_node = TextNode("", TextType.IMAGE, "www.google.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "www.google.com", "alt": ""})



if __name__ == "__main__":
    unittest.main()
