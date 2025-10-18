from markdown_blocks import markdown_to_blocks, block_to_block_type
from textnode import TextType, TextNode, text_node_to_html_node

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_types = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type != IMAGE or LINK:
            node = TextNode(block, block_type)
        if block_type == IMAGE or LINK:
            node = TextNode(block, block_type, url)
            

