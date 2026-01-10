import hashlib
import base64

def calculate_hash_chain(S):
    S = S.encode('utf-8')

    S = hashlib.sha256(S).digest()

    S = base64.b64encode(S)

    S = hashlib.new('ripemd160', S).digest()

    S = S.hex().upper()

    S = hashlib.sha1(S.encode('utf-8')).digest()

    S = S.hex().lower()

    S = hashlib.sha512(S.encode('utf-8')).digest()

    S = S[:32]

    S = hashlib.md5(S).digest()

    S = hashlib.sha384(S).hexdigest()

    return S

S = input().strip()
print(calculate_hash_chain(S))