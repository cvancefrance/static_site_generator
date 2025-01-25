from htmlnode import HTMLNode, ParentNode, LeafNode


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
    

def markdown_to_html_node(markdown):
    parent_node = ParentNode(tag="div")
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == "code":
             parent_node.children.append(handle_code_block(block))
        elif block_type == "quote":
            parent_node.children.append(handle_blockquote(block))
        elif block_type == "unordered_list":
            parent_node.children.append(handle_unordered_list(block))
        elif block_type == "ordered_list":
            parent_node.children.append(handle_ordered_list(block))
        elif block_type == "heading":
            parent_node.children.append(handle_heading(block))
        elif block_type == "paragraph":
            parent_node.children.append(handle_paragraph(block))
        else:
            raise ValueError(f"Unhandled block type: {block_type}")
    return parent_node


def text_to_children(text):
    children = []  # Store all nodes in this list

    while "**" in text:  # Continuously process until no bold markers remain
        start = text.find("**")  # Find the first occurrence of `**`

        # Handle plain text before the bold marker
        if start > 0:
            children.append(LeafNode(text=text[:start]))  # Add plain text as a LeafNode
            text = text[start:]  # Trim processed plain text

        # Now the remaining text starts with `**`
        end = text.find("**", 2)  # Find the matching closing bold marker
        bold_text = text[2:end]  # Extract the bold content
        children.append(
            ParentNode(tag="b", children=[LeafNode(text=bold_text)])  # Create a bold ParentNode
        )
        text = text[end + 2:]  # Trim the processed bold text

    # Handle any remaining plain text after the last bold marker
    if text:
        children.append(LeafNode(text=text))  # Add remaining plain text as a LeafNode

    return children


def handle_heading(block):
    # Step 1: Determine the heading level (e.g., "###" means <h3>)
    level = block.count("#", 0, block.find(" "))  # Count '#' before the first space
    tag = f"h{level}"

    # Step 2: Extract the heading text (trim '#' and spaces)
    text = block[level:].strip()  # Skip the '#' characters and strip whitespace

    # Step 3: Create the HTMLNode
    node = ParentNode(tag=tag)
    node.children.extend(text_to_children(text))

    return node

def handle_blockquote(block):
    text = block[2:]
    node = ParentNode(tag="blockquote")
    node.children.extend(text_to_children(text))
    return node
    
def handle_code_block(block):
    # Code blocks surround code with <pre><code>
    node = ParentNode(tag="pre")
    code_node = ParentNode(tag="code")
    code_node.children.append(LeafNode(text=block))  # Add the raw text inside <code>
    node.children.append(code_node)  # Add <code> as a child of <pre>
    
    return node

def handle_paragraph(block):
    node = ParentNode(tag="p")  # Surround the text with <p> tags
    node.children.extend(text_to_children(block.strip()))  # Inline markdown handling
    return node


def handle_unordered_list(block):
    # Step 1: Create the <ul> node
    ul_node = ParentNode(tag="ul")

    # Step 2: Split the block into individual list items (typically one per line)
    items = block.split("\n")
    for item in items:
        # Step 3: Remove "- " or "* " notation at the start of each item
        text = item[2:].strip()

        # Step 4: Create an <li> node for each list item
        li_node = ParentNode(tag="li")
        li_node.children.extend(text_to_children(text))  # Handle inline formatting

        # Step 5: Add the <li> node to the <ul> node
        ul_node.children.append(li_node)

    return ul_node

def handle_ordered_list(block):
    # Step 1: Create the <ol> node
    ol_node = ParentNode(tag="ol")

    # Step 2: Split the block into individual list items
    items = block.split("\n")
    for item in items:
        # Step 3: Remove "1. ", "2. ", etc., at the start of each item
        text = item[item.find(" ") + 1:].strip()

        # Step 4: Create an <li> node for each list item
        li_node = ParentNode(tag="li")
        li_node.children.extend(text_to_children(text)) #Handle inline formatting

        #Step 5: Add the <li> node to the <ol> node
        ol_node.children.append(li_node)
    
    return ol_node