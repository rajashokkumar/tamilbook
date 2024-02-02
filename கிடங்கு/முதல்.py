# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 11:28:37 2024

@author: asrajend
"""


data = bytes([0xe0,0xae,0xa4,0xe0,0xae,0xae,0xe0,0xae,0xbf,0xe0,0xae,0xb4,0xe0,0xae,0x82])
print(data.decode())

new_data="தமிழஂ"
arr = []
for c in new_data:
    arr.append(ord(c))
    print(c.encode())
     
print(arr)
for a in arr:
    print(chr(a),end="")
print()

print(chr(0xba4),end="")
print(chr(0xbae),end="")
print(chr(0xbbf),end="")
print(chr(0xbb4),end="")
print(chr(0xb82))

print('த')
print(ord('த'))
print(chr(ord('த')))
print(hex(ord('த')))
print(chr(0xba4))


str_original = input('Please enter string data:\n')

bytes_encoded = str_original.encode('utf-8')

str_decoded = bytes_encoded.decode('utf-8')

print('Encoded bytes =', bytes_encoded)
print(type(bytes_encoded))
print('Decoded String =', str_decoded)
print(type(str_decoded))
print('str_original equals str_decoded =', str_original == str_decoded)

