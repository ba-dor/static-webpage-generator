from textnode import *
from htmlnode import *

def main():
    test_node = TextNode("test", TextType.BOLD , "test_url")
    print(test_node)
    test_html_node = HTMLNode('p','test','children',{'"i"':'testurl'})
    print(test_html_node.props_to_html())
    print(test_html_node)
    test_leaf_node = LeafNode('p','testvalue',{'href': '"testurl"'})
    print(test_leaf_node)
    print(test_leaf_node.to_html())
    testnode = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )
    nestednode = ParentNode(
        "b",
        [testnode,testnode],
    )

    print(nestednode.to_html())

main()
