class HTMLNode():
    def __init__(self, tag:str = None, value:str = None, children:list= None, props:dict() = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __repr__(self):
        return f"HTMLNode(tag:{self.tag},value:{self.value},children:{self.children},props:{{{self.props_to_html()}}})" 

    def to_html(self):
        raise NotImplemented("This function is not implemented and should be overridden by its children")
    
    def props_to_html(self):
        html_string = ""
        if isinstance(self.props,dict) and len(self.props) > 0:
            for item in self.props:
                html_string = f' {html_string}{item.replace('"','')}:{self.props[item]}'
        return html_string

class LeafNode(HTMLNode):
    def __init__(self, tag ,value , props=None):
        if value == None or value == "":
            raise ValueError("every LeafNode should have a value")
        super().__init__(tag,value,None,props)

    def to_html(self):
        if self.value == None or self.value == "":
            raise ValueError("every LeafNode should have a value")
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag,None,children,props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("A ParentNode should have a tag")
        if self.children == None:
            raise ValueError("A ParentNode should have children")
        string = ""
        if isinstance(self.children, list):
            for child in self.children:
                string += child.to_html()
            return f"<{self.tag}>{string}</{self.tag}>"

        
