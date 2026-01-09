import hashlib
import base64
import sys

def main():
    s = sys.stdin.readline().strip()

    current_data_bytes = s.encode('utf-8')

    current_data_str = hashlib.sha256(current_data_bytes).hexdigest()

    current_data_bytes = base64.b64encode(current_data_str