def to_plain_text(stream_content):
    content = b""
    for chunk in stream_content:
        content += chunk

    return content.decode('utf-8')
