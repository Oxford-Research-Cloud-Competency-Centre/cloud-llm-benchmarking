import hashlib
import base64

def main():
    input_string = input().strip()
    utf8_bytes = input_string.encode('utf-8')
    sha256_hash = hashlib.sha256(utf8_bytes).digest()
    base64_encoded = base64.b64encode(sha256_hash)
    ripemd160_hash = hashlib.new('ripemd160', base64_encoded).digest()
    uppercase_hex = ripemd160_hash.hex().upper().encode('utf-8')
    sha1_hash = hashlib.sha1(uppercase_hex).digest()
    lowercase_hex = sha1_hash.hex().lower().encode('utf-8')
    sha512_hash = hashlib.sha512(lowercase_hex).digest()
    first_32_bytes = sha512_hash[:32]
    md5_hash = hashlib.md5(first_32_bytes).digest()
    sha384_hash = hashlib.sha384(md5_hash).hexdigest()
    print(sha384_hash)

if __name__ == "__main__":
    main()