from textnode import TextType, TextNode



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