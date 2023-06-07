import requests
import zlib

__all__ = ['download_gzip']


def decompress_stream(stream):
    o = zlib.decompressobj(16 + zlib.MAX_WBITS)

    for chunk in stream:
        yield o.decompress(chunk)

    yield o.flush()


def download_gzip(url):
    r = requests.get(url, stream=False)
    return decompress_stream(r.iter_content(chunk_size=1024*1024))
