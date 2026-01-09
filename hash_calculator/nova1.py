import hashlib
import base64

def hash_chain(s):
    utf8_bytes = s.encode('utf-8')
    sha256_hash = hashlib.sha256(utf8_bytes).digest()
    base64_str = base64.b64encode(sha256_hash)
    ripemd160_hash = hashlib.new('ripemd160', base64_str).digest().hex().upper()
    sha1_hash = hashlib.sha1(ripemd160_hash.encode()).hexdigest().lower()
    sha512_hash = hashlib.sha512(sha1_hash.encode()).digest()[:32]
    md5_hash = hashlib.md5(sha512_hash).hexdigest()
    final_hash = hashlib.sha384(md5_hash.encode()).hexdigest()
    return final_hash

input_str = input().strip()
print(hash_chain(input_str))