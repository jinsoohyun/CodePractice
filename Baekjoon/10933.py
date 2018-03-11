import hashlib
h = hashlib.new('ripemd160')
h.update(raw_input())
print h.hexdigest()
