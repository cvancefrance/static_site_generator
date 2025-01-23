import re


def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches



def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches



text = """
Here's a [regular link](https://example.com) and an image: 
![alt text](https://image.com/pic.png). Here's a second 
link [another link](https://another-example.com) and 
![another image](https://another-image.com/img.jpg).
"""

# Checking links
print(extract_markdown_links(text))
# Expected output:
# [('regular link', 'https://example.com'), ('another link', 'https://another-example.com')]

# Checking images
print(extract_markdown_images(text))
# Expected output:
# [('alt text', 'https://image.com/pic.png'), ('another image', 'https://another-image.com/img.jpg')]