class Estudiante:     #self es para referirse a todos los elementos de la clase
    def __init__(self,nombre):
        self.nombre=nombre
        self.apellido='perez'
        self.edad=30

e=Estudiante('Ana')
print e.nombre
