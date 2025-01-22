from htmlnode import HTMLNode




class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, value=None, children=children, props=props)


    def to_html(self):
        if self.tag is None:
            raise ValueError("missing tag")
        elif self.children is None:
            raise ValueError("missing children value")
        else:
            html_parts = []
            for child in self.children:
                # call to_html() on the child object
                child_html = child.to_html()
                # add it to our list
                html_parts.append(child_html)
            # After your loop collecting child HTML parts
            return f"<{self.tag}>{''.join(html_parts)}</{self.tag}>"
