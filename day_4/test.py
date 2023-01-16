import hashlib

# Create an MD5 hash object
md5 = hashlib.md5()

# Create a string to hash
string = "ckczppom117946"

# Hash the string
md5.update(string.encode())

# Get the hexadecimal representation of the hash
hash_hex = md5.hexdigest()

# Print the hash
print(hash_hex)
