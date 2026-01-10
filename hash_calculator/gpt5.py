import sys
import hashlib
import base64

def main():
    s = sys.stdin.readline().rstrip('\r\n')
    b = s.encode('utf-8')
    h1 = hashlib.sha256(b).digest()
    b64 = base64.b64encode(h1)
    h2 = hashlib.new('ripemd160', b64).digest()
    h2_hex_upper = h2.hex().upper()
    h3 = hashlib.sha1(h2_hex_upper.encode('utf-8')).digest()
    h3_hex_lower = h3.hex()
    h4 = hashlib.sha512(h3_hex_lower.encode('utf-8')).digest()
    first32 = h4[:32]
    h5 = hashlib.md5(first32).digest()
    final_hash = hashlib.sha384(h5).hexdigest()
    print(final_hash)

if __name__ == "__main__":
    main()