import hashlib
import base64

S = input()

# Step 1-2: Start with input string S and convert to UTF-8 bytes
data = S.encode('utf-8')

# Step 3: Calculate SHA-256 hash
data = hashlib.sha256(data).digest()

# Step 4: Convert the result to Base64
data = base64.b64encode(data)

# Step 5: Calculate RIPEMD-160 hash
data = hashlib.new('ripemd160', data).digest()

# Step 6: Convert to uppercase hex string
data = data.hex().upper().encode('utf-8')

# Step 7: Calculate SHA-1 hash
data = hashlib.sha1(data).digest()

# Step 8: Convert to lowercase hex string
data = data.hex().lower().encode('utf-8')

# Step 9: Calculate SHA-512 hash
data = hashlib.sha512(data).digest()

# Step 10: Take first 32 bytes
data = data[:32]

# Step 11: Calculate MD5 hash
data = hashlib.md5(data).digest()

# Step 12: Finally, calculate SHA-384 hash
data = hashlib.sha384(data).hexdigest()

print(data)