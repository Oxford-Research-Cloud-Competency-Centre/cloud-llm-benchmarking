import hashlib
import base64

def main():
    import sys
    input_str = sys.stdin.read().strip()
    
    # Step 1: Convert to UTF-8 bytes
    data = input_str.encode('utf-8')
    
    # Step 2: SHA-256 hash
    sha256_hash = hashlib.sha256(data).digest()
    
    # Step 3: Convert to Base64
    base64_result = base64.b64encode(sha256_hash).decode('utf-8')
    
    # Step 4: RIPEMD-160 hash
    ripemd160_hash = hashlib.new('ripemd160', base64_result.encode('utf-8')).digest()
    
    # Step 5: Convert to uppercase hex string
    hex_ripemd = ripemd160_hash.hex().upper()
    
    # Step 6: SHA-1 hash
    sha1_hash = hashlib.sha1(hex_ripemd.encode('utf-8')).digest()
    
    # Step 7: Convert to lowercase hex string
    hex_sha1 = sha1_hash.hex().lower()
    
    # Step 8: SHA-512 hash
    sha512_hash = hashlib.sha512(hex_sha1.encode('utf-8')).digest()
    
    # Step 9: Take first 32 bytes
    first_32_bytes = sha512_hash[:32]
    
    # Step 10: MD5 hash
    md5_hash = hashlib.md5(first_32_bytes).digest()
    
    # Step 11: SHA-384 hash
    final_hash = hashlib.sha384(md5_hash).hexdigest()
    
    print(final_hash)

if __name__ == "__main__":
    main()