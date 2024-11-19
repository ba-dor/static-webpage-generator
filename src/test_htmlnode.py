import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("a","value","",{"i":"test"})
        print(node)
        print(node.props_to_html())
    def test_eq1(self):
        node = HTMLNode("b","boldvalue","",{"i":"tester"})
        print(node)
        print(node.props_to_html())
    def test_eq2(self):
        node = HTMLNode("p","this is dummy text","",{"href":"https://test.be"})
        print(node)
        print(node.props_to_html())



if __name__ == "__main__":
    unittest.main()
