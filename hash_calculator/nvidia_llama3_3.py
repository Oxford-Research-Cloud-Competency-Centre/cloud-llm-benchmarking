import hashlib
import base64

S = input().strip()

s_bytes = S.encode('utf-8')
sha256 = hashlib.sha256(s_bytes).digest()
base64_b64 = base64.b64encode(sha256)
ripemd160 = hashlib.new('ripemd160', base64_b64).digest()
ripemd160_hex = ripemd160.hex().upper()
sha1_input = ripemd160_hex.encode('utf-8')
sha1 = hashlib.sha1(sha1_input).digest()
sha1_hex = sha1.hex().lower()
sha512_input = sha1_hex.encode('utf-8')
sha512 = hashlib.sha512(sha512_input).digest()
first_32 = sha512[:32]
md5 = hashlib.md5(first_32).digest()
sha384 = hashlib.sha384(md5).digest()
final_hex = sha384.hex()
print(final_hex)