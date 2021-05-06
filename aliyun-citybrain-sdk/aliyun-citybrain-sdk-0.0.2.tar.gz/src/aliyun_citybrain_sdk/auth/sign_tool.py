import base64
import hashlib
import hmac
import json
import uuid


def get_uuid4():
    return str(uuid.uuid4())


def other_to_str(data):
    if isinstance(data, (dict, list, tuple)):
        return json.dumps(data).replace(": ", ":")
    return str(data)


def ensure_bytes(s, encoding='utf-8'):
    if isinstance(s, str):
        return bytes(s, encoding=encoding)
    if isinstance(s, bytes):
        return s
    if isinstance(s, bytearray):
        return bytes(s)
    raise ValueError("Expected str or bytes or bytearray, received %s." % type(s))


def ensure_string(s):
    if isinstance(s, str):
        return s
    if isinstance(s, (bytes, bytearray)):
        return str(s, encoding='utf-8')
    raise ValueError("Expected str or bytes or bytearray, received %s." % type(s))


def to_md5_base64(string):
    content_bytes = ensure_bytes(string)
    md5_bytes = hashlib.md5(content_bytes).digest()
    return ensure_string(base64.b64encode(md5_bytes))


def to_hmac(sk, string):
    sk_byte = ensure_bytes(sk)
    source_bytes = ensure_bytes(string)
    h_bytes = hmac.new(sk_byte, source_bytes, digestmod=hashlib.sha1).digest()
    return ensure_string(base64.b64encode(h_bytes).strip())


def to_hash_sha256(source, secret):
    sk_byte = ensure_bytes(secret)
    source_bytes = ensure_bytes(source)
    h_bytes = hmac.new(sk_byte, source_bytes, digestmod=hashlib.sha256).digest()
    return ensure_string(base64.b64encode(h_bytes).strip())
    # h = hmac.new(secret.encode("utf-8"), source.encode("utf-8"), hashlib.sha256)
    # signature = base64.encodestring(h.digest()).strip()
    # return signature


if __name__ == '__main__':
    def to_md5(string):
        content_bytes = ensure_bytes(string)
        md5_bytes = hashlib.md5(content_bytes).hexdigest()
        return ensure_string(md5_bytes)

    test_md5 = to_md5("path/vm/qryVmDetailtimestamp1613983164506version1.0.07b15f1db3ac8ddb1b9f5d6087f817206")
    print(test_md5)