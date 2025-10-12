from textnode import TextNode, TextType
from image_link_extractor import extract_markdown_images, extract_markdown_links

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

def split_nodes_image(old_nodes):

    new_nodes = []
    for node in old_nodes:

        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        image_tuples = extract_markdown_images(node.text)
        if not image_tuples:
            new_nodes.append(node)
            continue

        current = node.text
        for alt, url in image_tuples:
            split_string = f"![{alt}]({url})"
            before, current = current.split(split_string, 1)
            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))

        if current:
            new_nodes.append(TextNode(current, TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes):

    new_nodes = []
    for node in old_nodes:

        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        link_tuples = extract_markdown_links(node.text)
        if not link_tuples:
            new_nodes.append(node)
            continue

        current = node.text
        for text, url in link_tuples:
            split_string = f"[{text}]({url})"
            before, current = current.split(split_string, 1)
            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(text, TextType.LINK, url))

        if current:
            new_nodes.append(TextNode(current, TextType.TEXT))

    return new_nodes

def text_to_textnodes(text):

    new_nodes = [TextNode(text, TextType.TEXT)]
    new_nodes = (split_nodes_delimiter(new_nodes, "**", TextType.BOLD))
    new_nodes = (split_nodes_delimiter(new_nodes, "_", TextType.ITALIC))
    new_nodes = (split_nodes_delimiter(new_nodes, "`", TextType.CODE))
    new_nodes = (split_nodes_image(new_nodes))
    new_nodes = (split_nodes_link(new_nodes))
    return new_nodes
