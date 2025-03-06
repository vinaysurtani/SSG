# def markdown_to_blocks(markdown):
#     #list1 = markdown.split('\n\n')
#     #list1[:] = [val.strip() for val in list1 if val != '']
#     list1 = [block.strip() for block in markdown.split('\n\n') if block.strip()]
#     for i,block in enumerate(list1):
#         while "\n " in block:
#             a = block.find('\n ')
#             #print(a)
#             if a != -1:
#                 b = block.find('\n',a+1)
#                 #print(b)
#                 if b == -1:
#                     block = block.replace("\n ","")
#                 else:
#                     k = block[a:b].strip()
#                     block = block[:a]+k+block[b:].strip()
#                 #print(block)
#                 list1[i]=block
#     #print(list1)
#     return list1


# def markdown_to_blocks(markdown):
#     # Pre-process to protect code blocks
#     code_blocks = []
#     in_code_block = False
#     lines = markdown.split('\n')
#     protected_markdown = []
#     current_code_block = []
    
#     for line in lines:
#         if line.strip() == "```":
#             in_code_block = not in_code_block
#             if in_code_block:
#                 # Starting a code block
#                 current_code_block = [line]
#             else:
#                 # Ending a code block
#                 current_code_block.append(line)
#                 code_blocks.append('\n'.join(current_code_block))
#                 protected_markdown.append(f"CODE_BLOCK_{len(code_blocks)-1}")
#                 current_code_block = []
#             continue

#         if in_code_block:
#             current_code_block.append(line)
#         else:
#             protected_markdown.append(line)
    
#     # Process the non-code blocks with your original logic
#     temp_markdown = '\n'.join(protected_markdown)
#     list1 = [block.strip() for block in temp_markdown.split('\n\n') if block.strip()]
    
#     # Clean up non-code blocks using your original logic
#     for i, block in enumerate(list1):
#         if block.startswith("CODE_BLOCK_"):
#             # This is a placeholder for a code block, leave it alone
#             continue
#         while "\n " in block:
#             a = block.find('\n ')
#             if a != -1:
#                 b = block.find('\n', a+1)
#                 if b == -1:
#                     block = block.replace("\n ", "")
#                 else:
#                     k = block[a:b].strip()
#                     block = block[:a] + k + block[b:].strip()
#                 list1[i] = block
    
#     # Replace code block placeholders with actual code blocks
#     final_blocks = []
#     for block in list1:
#         if block.startswith("CODE_BLOCK_"):
#             # Extract the code block index
#             index = int(block.replace("CODE_BLOCK_", ""))
#             final_blocks.append(code_blocks[index])
#         else:
#             final_blocks.append(block)
    
#     return final_blocks

def markdown_to_blocks(markdown):
    # Step 1: Split Markdown into raw blocks by double newlines, strip whitespace
    blocks = [block.strip() for block in markdown.split("\n\n") if block.strip()]
    
    # Step 2: Process each block and clean up extraneous spaces or formatting
    final_blocks = []
    for block in blocks:
        # Handle multiliner blocks (join lines, ensuring cleanliness)
        if "\n" in block:
            lines = block.split("\n")
            cleaned_lines = [line.strip() for line in lines if line.strip()]
            final_blocks.append("\n".join(cleaned_lines))
        else:
            # For single-line blocks, just clean and append
            final_blocks.append(block.strip())
    
    return final_blocks


# md1 = '''
# # This is a heading

#     This is a paragraph of text. It has some **bold** and _italic_ words inside of it.



# - This is the first list item in a list block
# - This is a list item
# - This is another list item
# '''


# md2 = """
# # Title

#    This is some text with extra spaces    
   
# - A list item
# - A list item
# """

# md3 = """
# This is a heading

# This is a paragraph that
# continues on a new line

# - This is a list
# - with items
# """
# print(markdown_to_blocks(md1))


# md = """
# ```
# This is text that _should_ remain
# the **same** even with inline stuff
# ```
# """
# print(markdown_to_blocks(md))