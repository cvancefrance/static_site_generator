from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url


    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url ==other.url:
            return True
        return False
        
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    

def text_node_to_html_node(text_node):
    if not isinstance(text_node.text_type, TextType):
        raise Exception("not a TextType")
    elif text_node.text_type is TextType.TEXT:
        return LeafNode("", text_node.text)
    elif text_node.text_type is  TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type is TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type is TextType.CODE:
        return LeafNode("code", text_node.text)  
    elif text_node.text_type is TextType.LINK:
        props = {"href": text_node.url}
        return LeafNode("a", text_node.text, props=props)
    elif text_node.text_type is TextType.IMAGE:
        props = {"src": text_node.url, "alt": text_node.text}
        return LeafNode("img", "", props=props)      




