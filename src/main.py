from textnode import *
from htmlnode import *

def main():
    test_node = TextNode("test", TextType.BOLD , "test_url")
    print(test_node)
    test_html_node = HTMLNode('p','test','children',{'"i"':'testurl'})
    print(test_html_node.props_to_html())
    print(test_html_node)


main()
