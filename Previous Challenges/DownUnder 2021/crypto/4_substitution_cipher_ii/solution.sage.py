

# This file was *autogenerated* from the file solution.sage
from sage.all_cmdline import *   # import sage library

_sage_const_1 = Integer(1); _sage_const_6 = Integer(6)
from string import ascii_lowercase, digits
from sage.all import *
from icecream import ic

CHARSET = "DUCTF{}_!?'" + ascii_lowercase + digits
n = len(CHARSET)

def challenge():
    def encrypt(msg, f):
        ct = ''
        for c in msg:
            ct += CHARSET[f.substitute(CHARSET.index(c))]
        return ct

    # P.<x> = PolynomialRing(GF(n))
    P = PolynomialRing(GF(n), names=('x',)); (x,) = P._first_ngens(_sage_const_1 )
    f = P.random_element(_sage_const_6 )

    FLAG = open('./flag.txt', 'r').read().strip()
    enc = encrypt(FLAG, f)

    ic(f)
    ic(enc)
    return enc


def main(ct: str):
    ic(enc)
    to_int = lambda i: CHARSET.index(i)
    known_pt = 'DUCTF{}'
    known_ct = ct[:len(known_pt)-_sage_const_1 ] + ct[-_sage_const_1 ]
    ic(known_pt)
    ic(known_ct)

    points = [(to_int(a), to_int(b)) for a, b in zip(known_pt, known_ct)]
    ic(points)

    P = PolynomialRing(GF(n), 'x'); (x,) = P._first_ngens(_sage_const_1 )
    ic(P)
    poly = P.lagrange_polynomial(points)
    ic(poly)

    inverse_subs = {}
    for i in range(n):
        y = poly.substitute(i)
        if y not in inverse_subs.keys():
            inverse_subs[y] = i
    ic(inverse_subs)

    pt = ''.join(CHARSET[inverse_subs[to_int(c)]] for c in ct)
    ic(pt)


if __name__ == '__main__':
    # enc = challenge()
    enc = open('./output.txt', 'r').read().strip()
    main(enc)


