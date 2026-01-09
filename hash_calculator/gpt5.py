import sys
import hashlib
import base64

def main():
    s = sys.stdin.readline()
    if s.endswith('\n'):
        s = s[:-1]

    b = s.encode('utf-8')

    sha256_hex = hashlib.sha256(b).hexdigest()

    b64 = base64.b64encode(sha256_hex.encode('ascii'))

    ripemd = hashlib.new('ripemd160', b64).digest()

    ripemd_hex_upper_bytes = ripemd.hex().upper().encode('ascii')