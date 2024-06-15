import requests

import magic
from data.parser.text import to_plain_text

IPFS_GATEWAY_URL = 'https://gateway.ipfs.cybernode.ai/ipfs'


def fetch_mime_and_stream(url):
    response = requests.get(url, stream=True)
    response.raise_for_status()

    # Initialize a bytes object to store the first chunk
    first_chunk = next(response.iter_content(chunk_size=1024))

    # Use the magic library to detect the content type from the first chunk
    mime = magic.Magic(mime=True)
    content_type = mime.from_buffer(first_chunk)

    def stream_content():
        yield first_chunk
        for chunk in response.iter_content(chunk_size=1024):
            yield chunk

    return content_type, stream_content()


def read_text_from_cid(cid):
    url = f'{IPFS_GATEWAY_URL}/{cid}'
    content_type, stream = fetch_mime_and_stream(url)
    if not content_type.startswith('text'):
        raise Exception(f'{cid} content type {content_type}, is not supported yet.')

    text =  to_plain_text(stream)

    return text


