import unittest
from htmlnode import HTMLNode
from leafnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_empty(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")
        
    
    def test_props_to_html_one_prop(self):
        node = HTMLNode(props={"href": "https://google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://google.com"')
        
    
    def test_props_to_html_multiple_props(self):
        node = HTMLNode(props={"href": "https://google.com","target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://google.com" target="_blank"')





    def test_leaf_node(self):
    # test basic tag with value
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    # test with props
        node_with_props = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node_with_props.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")

    # test with no tag
        text_node = LeafNode(None, "Just some text")
        self.assertEqual(text_node.to_html(), "Just some text")

    # test with no value (should raise ValueError)
        with self.assertRaises(ValueError):
            invalid_node = LeafNode("p", None)
            invalid_node.to_html()

if __name__ == "__main__":
    unittest.main()
