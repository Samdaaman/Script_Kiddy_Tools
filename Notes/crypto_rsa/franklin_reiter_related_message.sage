from sage.all import *
from Crypto.Util.number import bytes_to_long, long_to_bytes


def attack(n: int, e: int, r: int, ct1: int, ct2: int):
    """
    Franklin and Reiter identified an attack against RSA when multiple related messages are encrypted: If two messages differ only by a known fixed difference between the two messages and are RSA-encrypted under the same RSA modulus {\displaystyle N}N, then it is possible to recover both of them.
    The attack was originally described with public exponent {\displaystyle e=3}e=3, but it works more generally (with increasing cost as {\displaystyle e}e grows).
    
    Conditions:
    Two messages with some known linear difference (this implementation uses just a constant difference `r` but a difference function of `ax+b` is also possible)
    """
    # https://en.wikipedia.org/wiki/Coppersmith%27s_attack#Franklin%E2%80%93Reiter_related-message_attack
    # https://github.com/ValarDragon/CTF-Crypto/blob/master/RSA/FranklinReiter.sage

    # GCD is not implemented for rings over composite modulus in Sage
    # so we do our own implementation. Its the exact same as standard GCD, but with
    # the polynomials monic representation
    def composite_modulus_gcd(a, b):
        if(b == 0):
            return a.monic()
        else:
            return composite_modulus_gcd(b, a % b)

    # Inputs are modulus, known difference, ciphertext 1, ciphertext2.
    # Ciphertext 1 corresponds to smaller of the two plaintexts. (The one without the fixed difference added to it)
    # R.<X> = Zmod(n)[]
    R = Zmod(n)['X']; (X,) = R._first_ngens(1)
    f1 = X^e - ct1
    f2 = (X + r)^e - ct2
    # coefficient 0 = -m, which is what we wanted!
    return int(n-(composite_modulus_gcd(f1,f2)).coefficients()[0])


def __test():
    # From Hackthebox "Lost Modulus Again" crypto challenge
    n = 17239653555729308464049438184920371089879081148402291800380594759517665804698359052648921465219887554469533537465122062104900480567488997794605293481770139146098702102563250193298500864238250949982552595159802814788612573898410252974926866757617491510437384709301937357695288829868010397984533999482461397333141208905813094732501385628605554793978927603376904138986551086256407424185029648833489655496424708493511895902919181646372064531235987733921846952446773365611469842532440322381367711369625814351911101284458643213930109512205598526068165522864217435748337932540742524768583448250580752519750464577065964352977
    e = 3
    r = 17239653555729308464049438184920371089879081148402291800380594759517665804698359052648921465219887554469533537465122062104900480567488997794605293481770139146098702102563250193298500864238250949982552595159802814788612573898410252974926866757617491510437384709301937357695288829868010397984533999482461397333141208905813094732501385628605554793978927603376904138986551086256407424185029648833489655496424708493511895902919181646372064531235987733921846952446773365611469842532440322381367711369625814351911101284458643213930109512205598526068165522864217435748337932540742524768288846483820791076371295960930657614594
    ct1 = int('685dba88de1ecf0b4ae5bc84b7ee87f63eb37f697ca9a5ab6af9359341a2fbbf53b9502477cabb1658fdf775a34a0712b04d0fd2679b47ec088e0ab3c0a9a866198077a496bb1de138cd165ca28722dee7c4cc81ac0a3a179095f11981e9c7bcd590576169ed877b5692f42a7d9845bdb7c0bffd4e97541b65321de83e4083c1c8cc93eec59933f42655d7c0ad170ed9a3ea418b582e09a2692fc1965d8372cac678f0dabe1b0cbda93ac9b484feb9d2e96f3ab7e2fc6430da1931281c1870c637866be7fcd69c1b067e001887bb17a57ccd77532ea9dfaa0be1390db5511771dc9e03593e344bf0647ddac395b1fe80a86ad4ea4606fdb8a82fdcf9c846114c', 16)
    ct2 = int('356f7e82071f321361075ee85f9b42922662559ed64b253c64ff37b52fe8dcf3ab3163079bc9a12e951f84d2f7a911cbf1b1e8d7cd759a128f21a89b625b07ded33443a2888ca9a455198fd5b4a3fb307f34c704b7dcad88685263f4c3f4cf37f1099f2bd188de72533308c25fc18948dda220e3693b7f3edb689ee489c14e7624932ee8928370c9c1d59b06d1071a259d64c38735b1b586082099919713b669a79e43329f0c20508620982d95b774a57d009540c2ef2835887d229273223272f86fb0b1740937d3fc83d7556ffe634a16fb1faf6125878b06f5d537c21260014e2e67ae47636cbce899c463a3669954253aac3aa89a1c800d3251cf6a36badf', 16)

    pt1 = attack(n, e, r, ct1, ct2)
    print(long_to_bytes(pt1))
    assert bytes_to_long(b'HTB{Fr4nk1ln_r3t1t3r_sh0rt_p4d_4tt4ck!4nyw4ys_n3v3r_us3_sm0l_3xp_f0r_rs4!1s_th1s_Msg_g01ng_l4rg3r?_0h_y3s_cuz_1_h4v3_t0_Pr3v3nt_Cub3_r00t_4tt4ck}\xf5V\x87\x06EC\xd8\xa8\xcaS\xc7?\xb3\xfcN\xce') == pt1


if __name__ == '__main__':
    __test()
