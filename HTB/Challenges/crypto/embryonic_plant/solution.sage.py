

# This file was *autogenerated* from the file solution.sage
from sage.all_cmdline import *   # import sage library

_sage_const_953212452632162415623854742466108898886257018761981737488515480124784784754313403541058723530771941185648440076953890845364164881753643355212476926626742101375422468157394494383915186197027584298810203766388023131196821200163753827759350781726289328080241887775877824351482527440834821313689834438591567613042759531267263403394331824891899899505726815540209695860955058659042180466101027165453544129867565132811217413181292156021136184504130428910065116301275284964237087553827437109939035287527986380535446925078275313404977210504275217640523278087762041948497195357622678060873426815474421439984697128135689500335385151376561597600186415289317989920506634067994928935237389715706143172780083 = Integer(953212452632162415623854742466108898886257018761981737488515480124784784754313403541058723530771941185648440076953890845364164881753643355212476926626742101375422468157394494383915186197027584298810203766388023131196821200163753827759350781726289328080241887775877824351482527440834821313689834438591567613042759531267263403394331824891899899505726815540209695860955058659042180466101027165453544129867565132811217413181292156021136184504130428910065116301275284964237087553827437109939035287527986380535446925078275313404977210504275217640523278087762041948497195357622678060873426815474421439984697128135689500335385151376561597600186415289317989920506634067994928935237389715706143172780083); _sage_const_107663563520221758967681052016945344894135463272720867342404293429418113761640130338846143415694339846703472327422471509923932434685628383794998869995327761272087050985560474031629673883432008583476972873462387774454021532562638911 = Integer(107663563520221758967681052016945344894135463272720867342404293429418113761640130338846143415694339846703472327422471509923932434685628383794998869995327761272087050985560474031629673883432008583476972873462387774454021532562638911); _sage_const_375715892557297364364744701696307763009546269920835800827316473134718210911604668305115761037621526838903749589794728067744014884724708180550902913867595275270476040258585551516530116122396379615935241551413224529146764536011818960 = Integer(375715892557297364364744701696307763009546269920835800827316473134718210911604668305115761037621526838903749589794728067744014884724708180550902913867595275270476040258585551516530116122396379615935241551413224529146764536011818960); _sage_const_1142431136128743680237588635513380046580339971378804783979851430431837015880156204447030433004896454182104721893126547029880672333914367506184442229874405762062665597996081499892502200704128255903361177726702376303206644325660472696 = Integer(1142431136128743680237588635513380046580339971378804783979851430431837015880156204447030433004896454182104721893126547029880672333914367506184442229874405762062665597996081499892502200704128255903361177726702376303206644325660472696); _sage_const_696181402062958907421352186902458487367420124659441418095569426735447880619442484035499857372339751543528153083380619139649590779544110176169319718082842863368788080781170847125373363885050864587076550882230251633851030744318779877 = Integer(696181402062958907421352186902458487367420124659441418095569426735447880619442484035499857372339751543528153083380619139649590779544110176169319718082842863368788080781170847125373363885050864587076550882230251633851030744318779877); _sage_const_1090087409231264760633243725379604084008037546075358826209944877794280528534452761945892984736121167182908072643369909923239008686694491992033132238021506681618226619691505113704791978765000558863195023783700460638272869374754376211 = Integer(1090087409231264760633243725379604084008037546075358826209944877794280528534452761945892984736121167182908072643369909923239008686694491992033132238021506681618226619691505113704791978765000558863195023783700460638272869374754376211); _sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_0x10001 = Integer(0x10001)
from icecream import ic
from sage.all import *
from Crypto.Util.number import long_to_bytes
from Crypto.Cipher import AES
from hashlib import sha256


n = _sage_const_953212452632162415623854742466108898886257018761981737488515480124784784754313403541058723530771941185648440076953890845364164881753643355212476926626742101375422468157394494383915186197027584298810203766388023131196821200163753827759350781726289328080241887775877824351482527440834821313689834438591567613042759531267263403394331824891899899505726815540209695860955058659042180466101027165453544129867565132811217413181292156021136184504130428910065116301275284964237087553827437109939035287527986380535446925078275313404977210504275217640523278087762041948497195357622678060873426815474421439984697128135689500335385151376561597600186415289317989920506634067994928935237389715706143172780083 
s = [
    _sage_const_107663563520221758967681052016945344894135463272720867342404293429418113761640130338846143415694339846703472327422471509923932434685628383794998869995327761272087050985560474031629673883432008583476972873462387774454021532562638911 ,
    _sage_const_375715892557297364364744701696307763009546269920835800827316473134718210911604668305115761037621526838903749589794728067744014884724708180550902913867595275270476040258585551516530116122396379615935241551413224529146764536011818960 ,
    _sage_const_1142431136128743680237588635513380046580339971378804783979851430431837015880156204447030433004896454182104721893126547029880672333914367506184442229874405762062665597996081499892502200704128255903361177726702376303206644325660472696 ,
    _sage_const_696181402062958907421352186902458487367420124659441418095569426735447880619442484035499857372339751543528153083380619139649590779544110176169319718082842863368788080781170847125373363885050864587076550882230251633851030744318779877 ,
    _sage_const_1090087409231264760633243725379604084008037546075358826209944877794280528534452761945892984736121167182908072643369909923239008686694491992033132238021506681618226619691505113704791978765000558863195023783700460638272869374754376211 
]
enc_flag = bytes.fromhex('d3587442177b157fa0cecb6dd880872d86e15a50e3f05ecfeea8b90f5cfca22835a59d9c4f23e87a68317d4ccabe1bf3aa2e6cdf0a9ef1ada0a2e83d8da0bff2b739cf0e2b2b779958d9b1154a6f3698')

lhs = (s[_sage_const_3 ] - s[_sage_const_2 ])*(s[_sage_const_1 ] - s[_sage_const_0 ])
rhs = (s[_sage_const_2 ] - s[_sage_const_1 ]) ** _sage_const_2 
diff = abs(lhs - rhs)
r = gcd(n, diff)
ic(r)

xgcd_s = xgcd(s[_sage_const_1 ] - s[_sage_const_0 ], r)[_sage_const_1 ]
assert (xgcd_s * (s[_sage_const_1 ] - s[_sage_const_0 ])) % r == _sage_const_1 
p = ((s[_sage_const_2 ] - s[_sage_const_1 ]) * xgcd_s) % r
assert (p * (s[_sage_const_1 ] - s[_sage_const_0 ])) % r == (s[_sage_const_2 ] - s[_sage_const_1 ]) % r
ic(p)

q = n // p // r
ic(q)

assert n == p * q * r

phi = (p-_sage_const_1 ) * (q-_sage_const_1 ) * (r-_sage_const_1 )
d = pow(_sage_const_0x10001 , -_sage_const_1 , phi)
key = sha256(long_to_bytes(d)).digest()
cipher = AES.new(key, AES.MODE_ECB)
flag = cipher.decrypt(enc_flag)
ic(flag)

