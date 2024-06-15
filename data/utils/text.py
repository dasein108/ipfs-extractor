import re


def remove_links(text):
    # Regular expression to match URLs
    url_pattern = re.compile(r'https?://\S+|www\.\S+')

    cleaned_text = url_pattern.sub('', text)
    return cleaned_text


def remove_markdown(text):
    # Remove headers
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)

    # Remove emphasis (bold, italic, strikethrough)
    text = re.sub(r'(\*\*|__)(.*?)\1', r'\2', text)
    text = re.sub(r'(\*|_)(.*?)\1', r'\2', text)
    text = re.sub(r'(~~)(.*?)\1', r'\2', text)

    # Remove inline code and code blocks
    text = re.sub(r'`{1,3}[^`](.*?)`{1,3}', r'\1', text)
    text = re.sub(r'```[\s\S]*?```', '', text)

    # Remove blockquotes
    text = re.sub(r'^\s{0,3}>\s?', '', text, flags=re.MULTILINE)

    # Remove images
    text = re.sub(r'!\[(.*?)\]\(.*?\)', r'\1', text)

    # Remove links
    text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', text)

    # Remove horizontal rules
    text = re.sub(r'^-{3,}$', '', text, flags=re.MULTILINE)

    # Remove unordered lists
    text = re.sub(r'^\s*[-+*]\s+', '', text, flags=re.MULTILINE)

    # Remove ordered lists
    text = re.sub(r'^\s*\d+\.\s+', '', text, flags=re.MULTILINE)

    # Remove extra spaces and new lines
    text = re.sub(r'\n{2,}', '\n\n', text)
    text = text.strip()

    return text
