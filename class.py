class Alumno:

    def inicio(self, nombre, nota):
        self.nombre = nombre 
        self.nota = nota

    def imprimir(self):
        print("Hola ",self.nombre)
        print("Tu nota final es ",self.nota)
    
    def resultado(self):
        if self.nota <= 2.9:
            print("Has reprobado la materia")
        else:
            print("Felicidades has aprobado!!")



Alumno1 = Alumno()
Alumno1.inicio("Andres", 2.8)
Alumno1.imprimir()
Alumno1.resultado()

Alumno2 = Alumno()
Alumno2.inicio("Paola", 3.7)
Alumno2.imprimir()
Alumno2.resultado()
