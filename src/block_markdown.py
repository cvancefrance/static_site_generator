block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"
block_type_quote = "quote"



def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block):
    if (block.startswith("```") and block.endswith("```")) or (block.startswith("~~~") and block.endswith("~~~")):
        return "code"
    lines = block.split("\n")
    if all(line.startswith(">") for line in lines):
            return "quote"
    if all(line.startswith("* ") or line.startswith("- ") for line in lines):
        return "unordered_list"
    num = 1
    for line in lines:
        if not line.startswith(f"{num}."):
            break
        num += 1
    else:
        return "ordered_list"
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return "heading"
    else:
        return "paragraph"
    