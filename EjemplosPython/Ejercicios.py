'''
Capturar 2 numeros y mostrar el mayor y la diferencia entre ellos

a=raw_input('digite el numero 1: ')
b=raw_input('digite el numero 2: ')

if a>b:
    print 'El numero mayor es: ',a
else:
    print 'El numero mayor es', b

c=int(a)-int(b)
print 'Su diferencia es: ', c
'''

lista=[]
for i in range(5):
    i=raw_input('Digite el numero: ')
    lista.append(int(i))
