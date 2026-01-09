import hashlib
import base64

def main():
    S = input().strip()
    data = S.encode('utf-8')
    
    sha256_hash = hashlib.sha256(data).digest()
    base64_data = base64.b64encode(sha256_hash)
    ripemd160_hash = hashlib.new('ripemd160', base64_data).digest()
    hex_upper = ripemd160_hash.hex().upper()
    sha1_hash = hashlib.sha1(hex_upper.encode('utf-8')).hexdigest().lower()
    sha512_hash = hashlib.sha512(sha1_hash.encode('utf-8')).digest()
    first_32_bytes = sha512_hash[:32]
    md5_hash = hashlib.md5(first_32_bytes).hexdigest()
    final_hash = hashlib.sha384(md5_hash.encode('utf-8')).hexdigest()
    
    print(final_hash)

if __name__ == "__main__":
    main()