from enum import Enum
import re


class BlockType(Enum):
    paragraph = "paragraph"
    heading = "heading"
    code = "code"
    quote = "quote"
    unordered_list = "unordered_list"
    ordered_list = "ordered_list"

def block_to_block_type(markdown):
    heading_pattern = re.compile(r'^#{1,6} .+')
    if heading_pattern.match(markdown):
        return BlockType.heading
    elif markdown[:3] == '```' and markdown[-3:] == '```':
        return BlockType.code
    elif all(line.startswith('>') for line in markdown.split('\n')):
        return BlockType.quote
    elif all(line.startswith('- ') for line in markdown.split('\n')):
        return BlockType.unordered_list
    elif markdown.startswith('1. ') and all(line.startswith(f"{i}. ") for i, line in enumerate(markdown.split('\n'),start=1)):
        return BlockType.ordered_list
    else:
        return BlockType.paragraph
    

# md = '- alo'
# print(block_to_block_type(md))