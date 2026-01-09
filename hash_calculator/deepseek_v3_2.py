import hashlib
import base64

def main():
    S = input().strip()
    
    # Step 1-2: Convert S to UTF-8 bytes
    data = S.encode('utf-8')
    
    # Step 3: Calculate SHA-256 hash
    sha256_hash = hashlib.sha256(data).digest()
    
    # Step 4: Convert the result to Base64
    base64_data = base64.b64encode(sha256_hash)
    
    # Step 5: Calculate RIPEMD-160 hash
    ripemd160_hash = hashlib.new('ripemd160', base64_data).digest()
    
    # Step 6: Convert to uppercase hex string
    hex_upper = ripemd160_hash.hex().upper()
    
    # Step 7: Calculate SHA-1 hash
    sha1_hash = hashlib.sha1(hex_upper.encode('utf-8')).digest()
    
    # Step 8: Convert to lowercase hex string
    hex_lower = sha1_hash.hex().lower()
    
    # Step 9: Calculate SHA-512 hash
    sha512_hash = hashlib.sha512(hex_lower.encode('utf-8')).digest()
    
    # Step 10: Take first 32 bytes
    first_32_bytes = sha512_hash[:32]
    
    # Step 11: Calculate MD5 hash
    md5_hash = hashlib.md5(first_32_bytes).digest()
    
    # Step 12: Finally, calculate SHA-384 hash
    sha384_hash = hashlib.sha384(md5_hash).hexdigest()
    
    print(sha384_hash)

if __name__ == "__main__":
    main()