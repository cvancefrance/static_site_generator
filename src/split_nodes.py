from textnode import TextType, TextNode
from extract_markdown import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            if not find_delimiter_pairs(node.text, delimiter):
                raise Exception("invalid Markdown syntax")

            pieces = node.text.split(delimiter)
            for i in range(len(pieces)):
                
                if i % 2 == 0:
                    new_nodes.append(TextNode(pieces[i], TextType.TEXT))
                else:
                    new_nodes.append(TextNode(pieces[i], text_type))
    return new_nodes


def find_delimiter_pairs(text, delimiter):
     index = 0
     while index < len(text):
          start = text.find(delimiter, index)
          if start == -1:
               return True
          end = text.find(delimiter, start + len(delimiter))
          if end == -1:
               return False
          index = end + len(delimiter)






def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            images = extract_markdown_images(node.text)
            if not images:
                new_nodes.append(node)
            else:
                text = node.text
                for alt_text, url in images:
                    sections = text.split(f"![{alt_text}]({url})", 1)
                    if sections[0]:
                        new_nodes.append(TextNode(sections[0], TextType.TEXT))
                    new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
                    text = sections[1]

                if text:
                    new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes






def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            links = extract_markdown_links(node.text)
            if not links:
                new_nodes.append(node)
            else:
                text = node.text
                for link, url in links:
                    sections = text.split(f"[{link}]({url})", 1)
                    if sections[0]:
                        new_nodes.append(TextNode(sections[0], TextType.TEXT))
                    new_nodes.append(TextNode(link, TextType.LINK, url))
                    text = sections[1]

                if text:
                    new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes