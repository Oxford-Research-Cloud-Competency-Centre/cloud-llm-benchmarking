import hashlib
import base64

s = input()
utf8_bytes = s.encode('utf-8')
sha256_hash = hashlib.sha256(utf8_bytes).digest()
base64_encoded = base64.b64encode(sha256_hash).decode('utf-8')
ripemd160 = hashlib.new('ripemd160', base64_encoded.encode('utf-8')).hexdigest()
upper_hex = ripemd160.upper()
sha1_hash = hashlib.sha1(upper_hex.encode('utf-8')).hexdigest()
lower_hex = sha1_hash.lower()
sha512_hash = hashlib.sha512(lower_hex.encode('utf-8')).digest()
first_32_bytes = sha512_hash[:32]
md5_hash = hashlib.md5(first_32_bytes).digest()
sha384_hash = hashlib.sha384(md5_hash).hexdigest()
print(sha384_hash)