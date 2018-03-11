import hashlib
h = hashlib.new('sha')
h.update(raw_input())
print h.hexdigest()
