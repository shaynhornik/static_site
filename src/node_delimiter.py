from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError("Invalid Markdown syntax")
        for i in range(0, len(parts)):
            if parts[i] == "":
                continue
            elif i % 2 == 0:
                new_nodes.append(TextNode(parts[i], TextType.TEXT))
            elif i % 2 == 1:
                new_nodes.append(TextNode(parts[i], text_type))
    return new_nodes

