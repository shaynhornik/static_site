class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props == None or self.props == {}:
            return ""
        string_to_return = ""
        for k, v in self.props.items():
            string_to_return += f' {k}="{v}"'
        return string_to_return

    def __repr__(self):
        cls = self.__class__.__name__
        children_count = len(self.children) if self.children else 0
        return f"{cls}(tag={self.tag}, value={self.value}, children={children_count}, props={self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError
        if not self.tag:
            return f"{self.value}"
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, None, props)
        self.children = children
        self.props = props if props is not None else {}

    def to_html(self):
        if not self.tag:
            raise ValueError("No tag")
        if not self.children:
            raise ValueError("No children")
        open_tag = f'<{self.tag}{self.props_to_html()}>'
        middle = ''.join(child.to_html() for child in self.children)
        close_tag = f'</{self.tag}>'
        return open_tag + middle + close_tag
