import zlib

s = b"hello world!hello world!hello world!hello world!"

s1 = zlib.compress(s)
s2 = zlib.decompress(s1)
print(s1)
print(s2)