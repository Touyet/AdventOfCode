import hashlib

input = "ckczppom"
hash = ""
i = -1
while not hash.startswith('0'*6):
    i += 1
    h = input+str(i)
    hash = hashlib.md5(h.encode()).hexdigest()

print(i)
