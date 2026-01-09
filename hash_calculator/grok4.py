import hashlib
import base64

S = input()
bytes_S = S.encode('utf-8')
sha256_hex = hashlib.sha256(bytes_S).hexdigest()
base64_str = base64.b64encode(sha256_hex.encode('utf-8')).decode('utf-8')
bytes_base64 = base64_str.encode('utf-8')
ripemd = hashlib.new('ripemd160')
ripemd.update(bytes_base64)
ripemd_hex = ripemd.hexdigest()
upper_hex = ripemd_hex.upper()
bytes_upper = upper_hex.encode('utf-8')
sha1_hex = hashlib.sha1(bytes_upper).hexdigest()
lower_hex = sha1_hex.lower()
bytes_lower = lower_hex.encode('utf-8')
sha512_digest = hashlib.sha512(bytes_lower).digest()
first32 = sha512_digest[:32]
md5_digest = hashlib.md5(first32).digest()
sha384_hex = hashlib.sha384(md5_digest).hexdigest()
print(sha384_hex)