from enum import Enum
from htmlnode import LeafNode
from markdown_parser import extract_markdown_images,extract_markdown_links

class TextType(Enum):
    TEXT = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, node):
        if self.text == node.text and self.text_type == node.text_type and self.url == node.url:
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node):
    match (text_node.text_type):
        case TextType.TEXT:
            return LeafNode(None,text_node.text)
        case TextType.BOLD:
            return LeafNode("b",text_node.text)
        case TextType.ITALIC:
            return LeafNode("i",text_node.text)
        case TextType.CODE:
            return LeafNode("code",text_node.text)
        case TextType.LINK:
            return LeafNode("a",text_node.text,{"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img","",{"src":text_node.url, "alt":text_node.text})
        case _:
            raise Exception
        
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    #print(old_nodes)
    result = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            if delimiter not in node.text:
                result.append(node)
            else:
                first = node.text.find(delimiter)
                second = node.text.find(delimiter, first + len(delimiter))
                if second == -1:
                    raise Exception("no closing delimiter found")
                if node.text[:first]:
                    result.append(TextNode(node.text[:first], TextType.TEXT))
                result.append(TextNode(node.text[first+len(delimiter):second], text_type))
                if node.text[second+len(delimiter):]:
                    #result.append(TextNode(node.text[second+1:], TextType.TEXT))
                    remaining_node = TextNode(node.text[second+len(delimiter):], TextType.TEXT)
                    result.extend(split_nodes_delimiter([remaining_node], delimiter, text_type))
        else:
            result.append(node)
    #print(result)
    return result

def split_nodes_image(old_nodes):
    result = []
    for node in old_nodes:
        if extract_markdown_images(node.text) == []:
            result.append(node)
        else:
            val = extract_markdown_images(node.text)
            #print(val)
            spli = node.text.split(f"![{val[0][0]}]({val[0][1]})",1)
            #print(spli)
            if spli[0] != "":
                result.append(TextNode(spli[0], TextType.TEXT))
            result.append(TextNode(val[0][0], TextType.IMAGE, val[0][1]))
            if spli[1] != "":
                remaining_node = TextNode(spli[1],TextType.TEXT)
                #print(remaining_node)
                result.extend(split_nodes_image([remaining_node]))
    return result

# node1 = TextNode("This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",TextType.TEXT,)
# node2 = TextNode("![first](url1)![second](url2)",TextType.TEXT)
# node3 = TextNode("![first](url1)middle![second](url2)",TextType.TEXT)
# node4 = TextNode("Start ![](url1) end",TextType.TEXT)
# node5 = TextNode("![My Cool Image!](https://example.com/image?size=large&format=png)",TextType.TEXT)
# node6 = TextNode("![incomplete](no closing",TextType.TEXT)
# new_nodes = split_nodes_image([node1])
# print(new_nodes)


def split_nodes_link(old_nodes):
    result = []
    for node in old_nodes:
        if extract_markdown_links(node.text) == []:
            result.append(node)
        else:
            val = extract_markdown_links(node.text)
            #print(val)
            spli = node.text.split(f"[{val[0][0]}]({val[0][1]})",1)
            #print(spli)
            if spli[0] != "":
                result.append(TextNode(spli[0], TextType.TEXT))
            result.append(TextNode(val[0][0], TextType.LINK, val[0][1]))
            if spli[1] != "":
                remaining_node = TextNode(spli[1],TextType.TEXT)
                #print(remaining_node)
                result.extend(split_nodes_link([remaining_node]))
    return result


# res_list = split_nodes_delimiter(
#     [TextNode("Hello `code` and `more code`", TextType.TEXT)
#      ,TextNode("Just plain text", TextType.TEXT)
#      ,TextNode("**hello world**", TextType.BOLD)]
#     ,"`",TextType.CODE)
# print(res_list)

# res = split_nodes_delimiter([TextNode("Broken `code", TextType.TEXT)],"`",TextType.CODE)
# print(res)

# nodes = [TextNode("This is `code` and **bold**", TextType.TEXT)]
# # Process code first
# nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
# print("first split: ",nodes)
# # Then process bold
# nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
# print("second split: ",nodes)

# What happens if you process bold first, then code?
# nodes = [TextNode("This is `code` and **bold**", TextType.TEXT)]
# nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
# print("first split: ",nodes)
# nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
# print("second split: ",nodes)

# nodes = [TextNode("**bold** and **more bold**", TextType.TEXT)]
# print("first split: ",nodes)
# nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
# print("second split: ",nodes)

def text_to_textnodes(text):
    node = [TextNode(text,TextType.TEXT)]
    # print("After initial:", node)
    node = split_nodes_delimiter(node,"**",TextType.BOLD)
    # print("After bold:", node)
    node = split_nodes_delimiter(node,"_",TextType.ITALIC)
    node = split_nodes_delimiter(node,"*",TextType.ITALIC)
    # print("After italic:", node)
    node = split_nodes_delimiter(node,"`",TextType.CODE)
    # print("After code:", node)
    node = split_nodes_image(node)
    # print("After image:", node)
    node = split_nodes_link(node)
    # print("After link:", node)
    return node

# text1 = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
# text2 = "This has *two* different *italic* words"
# print(text_to_textnodes(text1))