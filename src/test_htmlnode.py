from htmlnode import HTMLNode

def test_props_to_html_with_props():
	node = HTMLNode(tag="a", props={"href": "https://x.com", "target": "_blank"})
	out = node.props_to_html()
	assert out == ' href="https://x.com" target="_blank"'

def test_props_to_html_empty():
	node = HTMLNode(tag="p", props=None)
	assert node.props_to_html() == ""

def test_repr_children_count():
	parent = HTMLNode(tag="div", children=[HTMLNode(tag="p"), HTMLNode(tag="a")])
	rep = repr(parent)
	assert "children=2" in rep

def test_leaf_to_html_p(self):
	node = LeafNode("p", "Hello, world!")
	self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

def test_leaf_to_html_a(self):
	node = LeafNode("a", "Click me!", {"href": "https://www.boot.dev"})
	self.assertEqual(node.to_html(), '<a href="https://www.boot.dev">Click me!</a>')

def test_leaf_to_html_tag_none(self):
    node = LeafNode(None, "Hello, world!")
    self.assertEqual(node.to_html(), "Hello, world!")

def test_leaf_to_html_value_none(self):
    node = LeafNode("p", None)
    self.assertRaises(ValueError, node.to_html)

def test_to_html_with_children(self):
	child_node = LeafNode("span", "child")
	parent_node = ParentNode("div", [child_node])
	self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

def test_to_html_with_grandchildren(self):
	grandchild_node = LeafNode("b", "grandchild")
	child_node = ParentNode("span", [grandchild_node])
	parent_node = ParentNode("div", [child_node])
	self.assertEqual(
		parent_node.to_html(),
		"<div><span><b>grandchild</b></span></div>",
	) 
