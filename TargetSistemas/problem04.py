sp = float(67.83643)
rj = float(36.67866)
mg = float(29.22988)
es = float(27.16548)
out = float(19.84953)
total = float(sp + rj + mg + es + out)
print(total)
psp = ((sp*total)/100)
prj = ((rj*total)/100)
pmg = ((mg*total)/100)
pes = ((es*total)/100)
pout = ((out*total)/100)

print('Porcentagem de SP {}'.format(psp))
print('Porcentagem de RJ {}'.format(prj))
print('Porcentagem de MG {}'.format(pmg))
print('Porcentagem de ES {}'.format(pes))
print('Porcentagem de OUT {}'.format(pout))