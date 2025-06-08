from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType

def text_node_to_html_node(text_node):
    """
    Converts a TextNode to an HTMLNode.
    
    Args:
        text_node (TextNode): The TextNode to convert.
        
    Returns:
        HTMLNode: The corresponding HTMLNode.
    """
    if text_node.node_type == TextType.TEXT:
        return LeafNode(value=text_node.text)
    elif text_node.node_type == TextType.BOLD:
        return LeafNode(tag="b", value=text_node.text)
    elif text_node.node_type == TextType.ITALIC:
        return LeafNode(tag="i", value=text_node.text)
    elif text_node.node_type == TextType.CODE:
        return LeafNode(tag="code", value=text_node.text)
    elif text_node.node_type == TextType.LINK:
        return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
    elif text_node.node_type == TextType.IMAGE:
        return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(f"Unsupported TextType: {text_node.node_type}")

'''
It takes a list of "old nodes", a delimiter, and a text type. It should return a new list of nodes, where any "text" type nodes in the input list are (potentially) split into multiple nodes based on the syntax. For example, given the following input:

node = TextNode("This is text with a `code block` word", TextType.TEXT)
new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

new_nodes becomes:

[
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" word", TextType.TEXT),
]
'''
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.node_type == TextType.TEXT and delimiter in node.text:
            parts = node.text.split(delimiter)
            for i, part in enumerate(parts):
                if i % 2 == 0:  # Even index: regular text
                    new_nodes.append(TextNode(part, TextType.TEXT))
                else:  # Odd index: code block
                    new_nodes.append(TextNode(part, text_type))
        else:
            new_nodes.append(node)
    return new_nodes
