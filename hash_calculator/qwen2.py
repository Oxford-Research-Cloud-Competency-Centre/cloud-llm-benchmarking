import hashlib

def calculate_hash_chain(input_string):
    # Step 1: Convert input string to UTF-8 bytes
    input_bytes = input_string.encode('utf-8')

    # Step 2: Calculate SHA-256 hash
    sha256_hash = hashlib.sha256(input_bytes).hexdigest()

    # Step 3: Convert the result to Base64
    base64_hash = base64.b64encode(bytes.fromhex(sha256_hash)).decode('utf-8')

    # Step 4: Calculate RIPEMD-160 hash
    ripemd160_hash = hashlib.new('ripemd160', base64_hash.encode('utf-8')).hexdigest().upper()

    # Step 5: Convert to uppercase hex string
    uppercase_hex_hash = ripemd160_hash

    # Step 6: Calculate SHA-1 hash
    sha1_hash = hashlib.sha1(uppercase_hex_hash.encode('utf-8')).hexdigest()

    # Step 7: Convert to lowercase hex string
    lowercase_hex_hash = sha1_hash.lower()

    # Step 8: Calculate SHA-512 hash
    sha512_hash = hashlib.sha512(lowercase_hex_hash.encode('utf-8')).hexdigest()

    # Step 9: Take first 32 bytes
    first_32_bytes = sha512_hash[:64]

    # Step 10: Calculate MD5 hash
    md5_hash = hashlib.md5(first_32_bytes.encode('utf-8')).hexdigest()

    # Step 11: Calculate SHA-384 hash
    final_hash = hashlib.sha384(md5_hash.encode('utf-8')).hexdigest()

    return final_hash

# Example usage
input_string = "Hello, World!"
final_hash = calculate_hash_chain(input_string)
print(final_hash)