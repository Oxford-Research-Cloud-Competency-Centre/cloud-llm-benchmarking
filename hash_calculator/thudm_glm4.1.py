import hashlib
import base64

S = input().strip()
bytes_data = S.encode('utf-8')

# Step 3: Calculate SHA-256 hash (bytes)
sha256_hash = hashlib.sha256(bytes_data).digest()

# Step 4: Convert to Base64
base64_encoded = base64.b64encode(sha256_hash).decode('utf-8')

# Step 5: Calculate RIPEMD-160 hash (bytes) from base64 encoded string
ripemd160_hash = hashlib.new('ripemd160').update(base64_encoded.encode('utf-8')).digest()

# Step 6: Convert to uppercase hex string
ripemd160_hex_upper = ripemd160_hash.hex().upper()

# Step 7: Calculate SHA-1 hash (bytes) from ripemd160_hash
sha1_hash = hashlib.sha1(ripemd160_hash).digest()

# Step 8: Convert to lowercase hex string
sha1_hex_lower = sha1_hash.hex().lower()

# Step 9: Calculate SHA-512 hash (bytes) from original bytes_data
sha512_hash = hashlib.sha512(bytes_data).digest()

# Step 10: Take first 32 bytes
first_32_bytes = sha512_hash[:32]

# Step 11: Calculate MD5 hash (bytes) from first_32_bytes
md5_hash = hashlib.md5(first_32_bytes).digest()

# Step 12: Calculate SHA-384 hash (bytes) from md5_hash
sha384_hash = hashlib.sha384(md5_hash).digest()

# Convert to hex string (lowercase, as per problem)
final_hex = sha384_hash.hex()

print(final_hex)