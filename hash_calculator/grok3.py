import hashlib
import base64

def calculate_hash_chain(input_str):
    data = input_str.encode('utf-8')
    
    data = hashlib.sha256(data).digest()
    
    data = base64.b64encode(data)
    
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(data)
    data = ripemd160.digest()
    
    data = data.hex().upper().encode('utf-8')
    
    data = hashlib.sha1(data).digest()
    
    data = data.hex().lower().encode('utf-8')
    
    data = hashlib.sha512(data).digest()
    
    data = data[:32]
    
    data = hashlib.md5(data).digest()
    
    final_hash = hashlib.sha384(data).hexdigest()
    
    return final_hash

input_string = input().strip()

result = calculate_hash_chain(input_string)
print(result)