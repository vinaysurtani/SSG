
from markdown_to_blocks import markdown_to_blocks
from block_types import block_to_block_type, BlockType
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html_node, text_to_textnodes


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.paragraph:
        return paragraph_to_html_node(block)
    if block_type == BlockType.heading:
        return heading_to_html_node(block)
    if block_type == BlockType.code:
        return code_to_html_node(block)
    if block_type == BlockType.ordered_list:
        return olist_to_html_node(block)
    if block_type == BlockType.unordered_list:
        return ulist_to_html_node(block)
    if block_type == BlockType.quote:
        return quote_to_html_node(block)
    raise ValueError("invalid block type")


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def paragraph_to_html_node(block):
    print(block)
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    text = block[4:-3]
    raw_text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(raw_text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])


def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)


# my implementation
# def markdown_to_html_node(markdown):
#     print(markdown)
#     blocks = markdown_to_blocks(markdown)
#     all_nodes = []
#     #print(blocks)
#     for block in blocks:
#         print(block,type(block))
#         block_type = block_to_block_type(block)
#         match block_type:
#             case BlockType.heading:
#                 head_size = block.count('#')
#                 tag = f"h{head_size}"
#                 content = block[head_size:].strip()
#                 children = text_to_children(content)
#                 all_nodes.append(ParentNode(tag, children, {}))
#             case BlockType.code:
#                 if block.startswith("```") and block.endswith("```"):
#                     actual_code = block[3:-3].strip()
#                     text_node = TextNode(content, TextType.TEXT)
#                     code_node = text_node_to_html_node(text_node)
#                     pre_node = ParentNode("pre", None, [LeafNode("code", None, [code_node])])
#                     all_nodes.append(pre_node)
#                 #print(block)
#                 #lines = block.split('\n')
#                 #print(lines)
#                 # if lines and lines[0].strip() == '```':
#                 #     lines = lines[1:]
#                 #     #print(lines)
#                 # if lines and lines[-1].strip() == '```':
#                 #     lines = lines[:-1]
#                 # actual_code =  '\n'.join(lines)
#                 # #print(actual_code)
#                 # code_node = LeafNode("code", actual_code, {})
#                 # pre_node = ParentNode("pre", [code_node], {})
#                 #all_nodes.append(pre_node)
#             case BlockType.quote:
#                 lines = block.split('\n')
#                 content = ''
#                 for line in lines:
#                     if line.startswith('>'):
#                         content += line[1:].strip() + " "
#                     else:
#                         content += line.strip() + " "
#                 content = content.strip()
#                 children = text_to_children(content)
#                 all_nodes.append(ParentNode("blockquote", children, {}))
#             case BlockType.unordered_list:
#                 lines = block.split('\n')
#                 list_items = []
#                 for line in lines:
#                     if line.strip():
#                         line_content = line.strip()
#                         if line_content.startswith('- '):
#                             line_content = line_content[2:]
#                         children = text_to_children(line_content.strip())
#                         list_items.append(ParentNode("li", children, {}))
#                 all_nodes.append(ParentNode("ul", list_items, {}))
#             case BlockType.ordered_list:
#                 lines = block.split('\n')
#                 list_items = []
#                 for line in lines:
#                     if line.strip():
#                         line_content = line.strip()
#                         dota = line_content.find('.')
#                         if dota != -1 and all(c.isdigit() for c in line_content[:dota]):
#                             line_content = line_content[dota+1:].strip()
#                         children = text_to_children(line_content)
#                         list_items.append(ParentNode("li", children, {}))
#                 all_nodes.append(ParentNode("ol", list_items, {}))
#             case BlockType.paragraph:
#                 children = text_to_children(block.strip())
#                 all_nodes.append(ParentNode("p", children, {}))
#             case _:
#                 raise Exception("put correct blocktype")
#     return ParentNode("div",all_nodes,{})
        
# def text_to_children(text):
#     text_nodes = text_to_textnodes(text)
#     html_nodes = []
#     for node in text_nodes:
#         html_node = text_node_to_html_node(node)
#         html_nodes.append(html_node)
#     return html_nodes