import ConfigParser

interprete=ConfigParser.ConfigParser()
interprete.read('mapa.map')

print interprete.get('nivel','origen')
#print interprete.get('nivel','mapa')
mapa=interprete.get('nivel','mapa')
mapa=mapa.split('\n')
print mapa
for i in mapa[1]:
    print i, interprete.get(i, 'x')
print interprete.get('.','tipo')
