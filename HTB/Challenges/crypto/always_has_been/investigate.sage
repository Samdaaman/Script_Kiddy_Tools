from debug import KEY_SBOX, SecureHash
from icecream import ic
from sage.crypto.sbox import SBox
from sage.crypto.sboxes import AES
from sage.all import *

flag = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

hash = SecureHash(flag).digest()
ic(hash.hex())

sbox = SBox(KEY_SBOX)
# print(sbox.autocorrelation_table())
# print(sbox.boomerang_uniformity())
# print(sbox.boomerang_connectivity_table())
# print(sbox.differential_branch_number())
ic(AES.has_linear_structure())
ic(sbox.has_linear_structure())
ic(AES.linearity())
ic(sbox.linearity())
ic(AES.nonlinearity())
ic(sbox.nonlinearity())
ic(AES.min_degree())
ic(sbox.min_degree())
ic(AES.max_degree())
ic(sbox.max_degree())
ic(AES.fixed_points())
ic(sbox.fixed_points())
# ic(AES.interpolation_polynomial())
ic(sbox.interpolation_polynomial())
with open('sbox_lat.txt', 'w') as fh:
    fh.write(sbox.linear_approximation_table().str())
    


poly = sbox.interpolation_polynomial()
ic(poly(1))
# ic(sbox.linear_structures())
# print(sbox.min_degree())
# print(sbox.nonlinearity())
# print(sbox.solutions())
