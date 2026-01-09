import sys
import hashlib
import base64

def main():
    s = sys.stdin.readline()
    if s.endswith('\n'):
        s = s[:-1]

    data = s.encode('utf-8')

    sha256_digest = hashlib.sha256(data).digest()

    b64_encoded = base64.b64encode(sha256_digest)

    ripemd160_digest = hashlib.new('ripemd160', b64_encoded).digest()

    upper_hex = ripemd160_digest.hex().upper()

    sha1_hex_lower = hashlib.sha1(upper_hex.encode('utf-8')).hexdigest().lower()

    sha512_digest = hashlib.sha512(sha1_hex_lower.encode('utf-8')).digest()

    first_32_bytes = sha512_digest[:32]

    md5_digest = hashlib.md5(first_32_bytes).digest()

    final_hash = hashlib.sha384(md5_digest).hexdigest().lower()

    print(final_hash)

if __name__ == "__main__":
    main()