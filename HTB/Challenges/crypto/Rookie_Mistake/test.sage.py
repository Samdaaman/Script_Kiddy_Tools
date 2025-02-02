

# This file was *autogenerated* from the file test.sage
from sage.all_cmdline import *   # import sage library

_sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_2 = Integer(2); _sage_const_8 = Integer(8); _sage_const_3 = Integer(3); _sage_const_64 = Integer(64); _sage_const_0x69420 = Integer(0x69420); _sage_const_12345 = Integer(12345); _sage_const_41 = Integer(41); _sage_const_7 = Integer(7); _sage_const_12 = Integer(12); _sage_const_8101 = Integer(8101); _sage_const_6 = Integer(6); _sage_const_7531 = Integer(7531); _sage_const_14082041 = Integer(14082041); _sage_const_17985707 = Integer(17985707); _sage_const_4052059 = Integer(4052059)
from sage.all import *
from icecream import ic
from Crypto.Util.number import getPrime
from random import randint
import itertools


def pohlig_hellman_old(p, g, h):
    factors = factor(p - _sage_const_1 )
    F = GF(p)
    g = F(g)
    h = F(h)
    ic(factors)
    residuals = []
    modului = []
    for pi, ki in factors:
        x_arr = []
        beta_arr = [h]
        for j in range(ki):
            if j > _sage_const_0 :
                divisor = g ** (pi**(j-_sage_const_1 ) * x_arr[j-_sage_const_1 ])
                s = xgcd(divisor, h)[_sage_const_1 ]
                ic((pi**(j-_sage_const_1 ) * x_arr[j-_sage_const_1 ]), divisor, s, beta_arr[j-_sage_const_1 ] * s)
                beta_arr.append(beta_arr[j-_sage_const_1 ] * s)

            beta = beta_arr[j]
            lhs = beta ** ((p-_sage_const_1 ) // pi**(j+_sage_const_1 ))
            rhs = g ** ((p-_sage_const_1 ) // pi)
            x = discrete_log(lhs, rhs)
            x_arr.append(x)
            ic(pi, j, x)

        x = sum([pi**j * x_arr[j] for j in range(ki)])
        ic(pi, x)
        if x != _sage_const_0 :
            residuals.append(x)
            modului.append(pi ** ki)

    ic(residuals)
    ic(modului)
    return crt(residuals, modului)


def pohlig_hellman(p, g, h):
    factors = factor(p - _sage_const_1 )
    F = GF(p)
    g = F(g)
    h = F(h)
    ic(factors)
    residuals_options = []
    modului = []
    for pi, ki in factors:
        lhs = h ** ((p-_sage_const_1 ) // pi)
        rhs = g ** ((p-_sage_const_1 ) // pi)
        x = discrete_log(lhs, rhs)
        ic(pi, x)
        if lhs == _sage_const_1  and rhs == _sage_const_1 :
            residuals_options.append(list(range(pi)))
            print(f'Increasing result size by a {pi} times')
        else:
            residuals_options.append([x])
        modului.append(pi ** ki)

    return set(crt(list(residuals), modului) for residuals in itertools.product(*residuals_options))


def gen_prime():
    while True:
        pm1 = _sage_const_2  * getPrime(_sage_const_8 ) * getPrime(_sage_const_8 ) * getPrime(_sage_const_8 )
        if is_prime(pm1 + _sage_const_1 ) and not any(k > _sage_const_1  for p, k in factor(pm1)):
            return pm1 + _sage_const_1 


def test1():
    while True:
        p = gen_prime()
        # p = getPrime(16)
        g = _sage_const_3 
        x = randint(_sage_const_0 , p//_sage_const_2 )
        h = pow(g, x, p)
        ic(h)
        ic(p)
        ic(x)
        t = pohlig_hellman(p, g, h)
        if x not in t:
            ic(t)
            break


def test2():
    p = getPrime(_sage_const_64 )
    q = getPrime(_sage_const_64 )
    n = p*q
    g = _sage_const_0x69420 
    x = _sage_const_12345 
    h = pow(g, x, n)
    cf = gcd(p-_sage_const_1 , q-_sage_const_1 )
    x_pm1 = pohlig_hellman(p, g, h)
    x_qm1 = pohlig_hellman(q, g, h, cf=cf)

    x_phi = crt(x_pm1, x_qm1, p-_sage_const_1 , q-_sage_const_1 )
    ic(x_phi)


def test3():
    p = _sage_const_41 
    g = _sage_const_7 
    h = _sage_const_12 
    x = pohlig_hellman(p, g, h)
    ic(x)
    ic(pow(g, x, p))


def test4():
    p = _sage_const_8101 
    g = _sage_const_6 
    h = _sage_const_7531 
    x = pohlig_hellman(p, g, h)
    ic(x)
    ic(pow(g, x, p))


def test5():
    h = _sage_const_14082041 
    p = _sage_const_17985707 
    g = _sage_const_3 
    x1 = _sage_const_4052059 
    x2 = pohlig_hellman(p, g, h)
    ic(pow(g, x1, p))


if __name__ == '__main__':
    test1()

