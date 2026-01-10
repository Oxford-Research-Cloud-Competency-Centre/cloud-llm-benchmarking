import base64
import hashlib

def hash_chain(s):
    # Convert to UTF-8 bytes
    utf8_bytes = s.encode('utf-8')
    # SHA-256 hash
    sha256_hash = hashlib.sha256(utf8_bytes)
    # Base64 encode
    base64_encoded = base64.b64encode(sha256_hash.digest())
    # RIPEMD-160 hash
    ripemd160_hash = hashlib.new('ripemd160', base64_encoded).digest()
    # Convert to uppercase hex string
    uppercase_hex = ripemd160_hash.hex().upper()
    # SHA-1 hash
    sha1_hash = hashlib.sha1(uppercase_hex.encode('utf-8'))
    # Convert to lowercase hex string
    lowercase_hex = sha1_hash.hexdigest()
    # SHA-512 hash
    sha512_hash = hashlib.sha512(lowercase_hex.encode('utf-8'))
    # Take first 32 bytes
    first_32_bytes = sha512_hash.digest()[:32]
    # MD5 hash
    md5_hash = hashlib.md5(first_32_bytes)
    # SHA-384 hash
    sha384_hash = hashlib.sha384(md5_hash.digest())
    # Return the final hash
    return sha384_hash.hexdigest()

# Example input
input_string = "Hello, World!"
print(hash_chain(input_string))