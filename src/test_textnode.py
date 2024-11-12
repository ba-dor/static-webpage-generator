import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_eq1(self):
        node = TextNode("This is a text node", TextType.CODE,"testurl")
        node2 = TextNode("This is a text node", TextType.CODE,"testurl")
        self.assertEqual(node, node2)
    def test_eq2(self):
        node = TextNode("test italic", TextType.ITALIC)
        node2 = TextNode("test italic", TextType.ITALIC)
        self.assertEqual(node, node2)
    def test_eq3(self):
        node = TextNode("test2", TextType.NORMAL)
        node2 = TextNode("test2", TextType.NORMAL)
        self.assertEqual(node, node2)
    def test_neq(self):
        node = TextNode("test1",TextType.NORMAL)
        node2 = TextNode("test2",TextType.NORMAL)
        self.assertNotEqual(node,node2)




if __name__ == "__main__":
    unittest.main()
