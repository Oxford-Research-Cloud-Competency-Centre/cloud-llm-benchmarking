import hashlib
import base64

def hash_chain(S):
    utf8_bytes = S.encode('utf-8')
    sha256_hash = hashlib.sha256(utf8_bytes).digest()
    base64_hash = base64.b64encode(sha256_hash).decode('utf-8')
    ripemd160_hash = hashlib.new('ripemd160', base64_hash.encode('utf-8')).digest()
    uppercase_hex = ripemd160_hash.hex().upper()
    sha1_hash = hashlib.sha1(uppercase_hex.encode('utf-8')).digest()
    lowercase_hex = sha1_hash.hex().lower()
    sha512_hash = hashlib.sha512(lowercase_hex.encode('utf-8')).digest()
    first_32_bytes = sha512_hash[:32]
    md5_hash = hashlib.md5(first_32_bytes).digest()
    sha384_hash = hashlib.sha384(md5_hash).hexdigest()
    
    return sha384_hash

S = input().strip()
print(hash_chain(S))