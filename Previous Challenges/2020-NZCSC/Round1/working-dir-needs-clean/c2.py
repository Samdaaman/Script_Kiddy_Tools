import math
d1 = '678371118371108371038371148379783711683711783710883797837116837105837111837110837115837338373283789837111837117837328371048379783711883710183732837115837117837998379983710183711583711583710283711783710883710883712183732837102837111837117837110837100837328371168371048371018373283710283710883797837103837588375683797837998375383710283756837558379783750837558375583753'
d2 = []
n = 3

# for i in range(math.floor(len(d1) / n)):
#     r = ''
#     for j in range(n):
#         r += d1[i*n+j]
#     d2.append(r)

# for i in range(math.floor(len(d1) / n)):
#     r = 0
#     for j in range(n):
#         r += int(d1[i*n+j])
#     d2.append(r)

def dec(s):
    return chr(int(s))

c1 = d1.replace('837', '-')
l1 = c1.split('-')

print(''.join(map(dec, l1)))

c1 = '-' + '-'.join([str(i).rjust(2, '0') for i in d2]) + '-'
c2 = c1
g = [
    ('11', ' '),
    ('15', 'a')
]
for r1, r2 in g:
    c2 = c2.replace(r1, r2.rjust(2, ' '))

print(c1)
print(c2)
