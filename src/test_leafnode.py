import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("a","value",{"i":"test"})
        print(node)
        print(node.to_html())
    def test_eq1(self):
        node = LeafNode("b","boldvalue",{"i":"tester"})
        print(node)
        print(node.to_html())
    def test_eq2(self):
        node = LeafNode("p","this is dummy text",{"href":"https://test.be"})
        print(node)
        print(node.to_html())
    def test_eq3(self):
        node = LeafNode("p","this is dummy text")
        print(node)
        print(node.to_html())




if __name__ == "__main__":
    unittest.main()
