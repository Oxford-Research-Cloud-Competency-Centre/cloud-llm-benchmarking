import hashlib
import base64

s = input().strip()

# Step 1: Convert to UTF-8 bytes
data = s.encode('utf-8')

# Step 2: SHA-256 hash
sha256 = hashlib.sha256(data).digest()

# Step 3: Convert to Base64
b64 = base64.b64encode(sha256).decode('utf-8')

# Step 4: RIPEMD-160 hash
ripemd = hashlib.new('ripemd160', b64.encode('utf-8')).digest()

# Step 5: Convert to uppercase hex string
uppercase_hex = ripemd.hex().upper()

# Step 6: SHA-1 hash
sha1 = hashlib.sha1(uppercase_hex.encode('utf-8')).digest()

# Step 7: Convert to lowercase hex string
lowercase_sha1_hex = sha1.hex().lower()

# Step 8: SHA-512 hash
sha512 = hashlib.sha512(lowercase_sha1_hex.encode('utf-8')).digest()

# Step 9: Take first 32 bytes
step10_data = sha512[:32]

# Step 10: MD5 hash
md5 = hashlib.md5(step10_data).digest()

# Step 11: SHA-384 hash
final_hash = hashlib.sha384(md5).hexdigest()

print(final_hash)