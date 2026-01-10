import hashlib

def sha_256(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()[:10]

def ripemd_160(s):
    return hashlib.new('ripemd160').update(s.encode('utf-8')).hexdigest()[:20]

def sha1(s):
    return hashlib.sha1(s.encode('utf-8')).hexdigest()[:10]

def sha512(s):
    return hashlib.sha512(s.encode('utf-8')).hexdigest()[:32]

def md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()[:16]

def sha384(s):
    return hashlib.sha3_256(s.encode('utf-8')).hexdigest()[:4]

s = "Hello, World!"

print("{:0>64}".format(sha_256(s).upper()))
print("{:0>64}".format(sha_256(s).lower()))
print("{:0>64}".format(sha512(sha_256(s).encode('utf-8'))[:32]))
print("{:0>64}".format(md5(sha_256(s).encode('utf-8'))))
print("{:0>64}".format(sha384(sha_256(s).encode('utf-8'))))