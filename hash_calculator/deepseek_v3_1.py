import hashlib
import base64

def main():
    s = input().strip()
    data = s.encode('utf-8')
    
    sha256_hash = hashlib.sha256(data).digest()
    base64_data = base64.b64encode(sha256_hash)
    ripemd160_hash = hashlib.new('ripemd160', base64_data).digest()
    hex_upper = ripemd160_hash.hex().upper()
    sha1_hash = hashlib.sha1(hex_upper.encode('utf-8')).digest()
    hex_lower = sha1_hash.hex().lower()
    sha512_hash = hashlib.sha512(hex_lower.encode('utf-8')).digest()
    first_32_bytes = sha512_hash[:32]
    md5_hash = hashlib.md5(first_32_bytes).digest()
    sha384_hash = hashlib.sha384(md5_hash).hexdigest()
    
    print(sha384_hash)

if __name__ == "__main__":
    main()