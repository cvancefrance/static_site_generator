

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children= children
        self.props = props



    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        prop_strings = []
        for key, value in self.props.items():
            formatted_prop = f' {key}="{value}"'
            prop_strings.append(formatted_prop)
            
        return "".join(prop_strings)
        
    
    def __repr__(self):
        print(HTMLNode)


