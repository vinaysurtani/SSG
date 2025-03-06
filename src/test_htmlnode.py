import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_node(self):
        node = HTMLNode(tag='a', 
                        props={"href": "https://example.com", "target": "_blank"})
        #print(node.__repr__())
        self.assertEqual(node.__repr__(),"HTMLNode(a, None, None, {'href': 'https://example.com', 'target': '_blank'})")

    def test_props_to_html(self):
        node = HTMLNode(tag="a", props={"href": "https://example.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(),' href="https://example.com" target="_blank"')

    def test_parent_node(self):
        node = ParentNode(tag='div',
                          children = [
                            LeafNode("span", "Hello"),
                            ParentNode("div", [
                                LeafNode("p", "Nested text"),
                                LeafNode("",'yes'),
                            ]),
                            LeafNode("br", "")
                            ])
        #print(node.to_html())
        self.assertEqual(node.to_html(),'<div><span>Hello</span><div><p>Nested text</p>yes</div><br></br></div>')

    def test_leaf_node(self):
        node = LeafNode("p","Hello, world!")
        self.assertEqual(node.to_html(),"<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

if __name__ == "__main__":
    unittest.main()