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
        for item in self.props:
            html_string = f'{html_string}{item.replace('"','')}:{self.props[item]} '
        return html_string

    
