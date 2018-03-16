import bencode
import hashlib
import base64
import sys

def bt2magnet(f):
    # 计算meta数据
    metadata = bencode.bdecode(f)
    hashcontents = bencode.bencode(metadata['info'])
    digest = hashlib.sha1(hashcontents).digest()
    b32hash = base64.b32encode(digest)
    return 'magnet:?xt=urn:btih:%s' % b32hash

