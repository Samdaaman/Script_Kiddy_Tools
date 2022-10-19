from hashlib import sha512
from icecream import ic
from Crypto.Util.number import getPrime, getRandomRange, isPrime, inverse, long_to_bytes, bytes_to_long
from hashlib import sha512

with open('output.txt') as fh:
    lines = [line.strip() for line in fh.readlines()]

outputs = []
for i, line in enumerate(lines):
    if line.startswith('message : '):
        message = line.split('message : ')[1]
        r, s = eval(lines[i+1].split('signature: ')[1])
        outputs.append((message, r, s))


test_arr = []


i1 = 0
i2 = 0
for i, (m1, r1, s1) in enumerate(outputs):
    for j, (m2, r2, s2) in enumerate(outputs):
        if r1 == r2 and i != j:
            i1 = i
            i2 = j
            break
    if i1 != 0:
        break

m1, r1, s1 = outputs[i1]
m2, r2, s2 = outputs[i2]

ic(m1, r1, s1)
ic(m2, r2, s2)

q = 82349764091980216703243528787846721157571379253101971061732427939554681522787
p = 22597614376179368541927291014351181151227386315855982530475290304066480549601872481125000412312232411854471891135859606462198144416258790805203892259557432117585853522644532244043882866950543772453962473369978828348563267281282352402870551728874298860312184560283971631533453430210347478794479982659822354364676170461394200151617927348650724770337556315374296708920869883704844016422867256502854967833552352244354161923370938186895496059235837548125257119775236437293842236838420824347387394024112360489719718482356279060719080630335848636921250967340335457343005624222097640480295331833551512059471129216303573167509
g = 1522212929726315022276463307120954560926577974082882818811797965963142559037271005677110576098054722157527674127902562772533441779935566082403254092732974888203331702770403906546118095393659134079664766399608052006354212408035095060235607110586791971501473747663375215625574865706205289870455822949113508277054039439561937834562865074493156250996591912564352116714825726533396169890605271470775008065174813981767038809048518345994705536020788635479039463106099323099699225053825245500316037480436011003338091199884975066597695902083102085310246580054607257558459623691521498166469718547232285924180800892984387501802
y = 10301551349126329107088362265646928131049491442403482867496980836175873288506342576259707854365987702240527285572213439531723683002024146579359208402373918640506155640001430423630072829735081526301031527635977510509965942632354962864260004282149309957641462890526767244115715946314304320419688533957853639652278917522214541525010449214567907170562229712395613781822381944931215562795920884762599015541122869232934183665333423423899053585371134224417264749221110182731383922695086302701203378645475314119934887765168566160180674997559835947912322992312116118206408320274722250233256553213251576546136974127152356743543

Hm1 = int(sha512(m1.encode('utf-8')).hexdigest(), 16)
Hm2 = int(sha512(m2.encode('utf-8')).hexdigest(), 16)

k = ((Hm1 - Hm2) * inverse(s1 - s2, q)) % q
x = ((s1 * k - Hm1) * inverse(r1, q)) % q

ic(x)
ic(pow(g, x, p) == y)


def repeating_xor_key(message, key):

    repeation = 1 + (len(message) // len(key))
    key = key * repeation
    key = key[:len(message)]
    
    msg = bytes([c ^ k for c, k in zip(message, key)])
    return msg

key = long_to_bytes(x)
ct = bytes.fromhex('caaa08c4332e5701a9105ab701cc830b9ddbe18f6612c999f82a344bdc597819fba00f81772e4001bc584cff06d287089d8085a3123bdca5e7706612d7641f66a2b6228a67336c60975719ef04e1b55edad4e6850126ee92bc25692bd15e274db3b214973f224001af5f46bb40d2930cd69bae')
print(repeating_xor_key(ct, key))


