import random

class Persona:

    def __init__(self, nombreP="", edadP=1, dniP="", sexoP="M", pesoP=1, alturaP=1):

        self.__nombre = nombreP

        while (edadP<=0):
            edadP = int(input("Introduce una edad correcta: "))
        self.__edad = edadP

        x=int(dniP)
        cadena= "TRWAGMYFPDXBNJZSQVHLCKE"
        self.__dni =cadena[x%23]

        while (sexoP!= "H" and sexoP!="h")and(sexoP!= "M" and sexoP!="m"):
            sexoP = input("Introduce un sexo valido: ")
        self.__sexo = sexoP

        while (pesoP<=0):
            pesoP = int(input("Introduce un peso correcto: "))
        self.__peso = pesoP

        while (alturaP<=0 or alturaP>=2.50):
            alturaP = float(input("Introduce una altura correcta: "))
        self.__altura = alturaP

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setEdad(self, edad):
        while (edad<=0):
            edad = int(input("Introduce un valor correcto: "))
        self.__edad = edad

    def setDni(self, dni):
        self.__dni = dni

    def setSexo(self, sexo):
        while (sexo!= "H" and sexo!="h")and(sexo!= "M" and sexo!="m"):
            sexo = input("Introduce un valor correcto: ")
        self.__sexo = sexo

    def setPeso(self, peso):
        while (peso<=0):
            peso = int(input("Introduce un peso correcto: "))
        self.__peso = peso

    def setAltura(self, altura):
        while (altura<=0 or altura>=2.50):
            altura = float(input("Introduce una altura correcta: "))
        self.__altura = altura

    def getPeso(self):
        return self.__peso

    def getAltura(self):
        return self.__altura

    def __str__(self):
        return "Nombre: "+self.__nombre+"; DNI: "+self.__dni+"; Edad: "+str(self.__edad)+"; Sexo: "+self.__sexo+"; Peso: "+str(self.__peso)+"; Altura: "+str(self.__altura)

    def calcularIMC(self):
        imc = self.__peso /(pow(self.__altura, 2))
        if (self.__peso == imc):
            print(imc)
            return 0
        elif(self.__peso < imc):
            print(imc)
            return -1
        else:
            print(imc)
            return 1

    def mayorEdad(self):
        if (self.__edad<18):
            return False
        else :
            return True

    def generarDNI(self):
        aleatorio = random.radint(10000000, 99999999)


print("Introduce los datos de la primera persona: ")
persona1 = Persona(input("Introduce el nombre: "),int(input("Introduce la edad: ")),input("Introduce el DNI: "), input("Introduce el sexo (H/M)"),float(input("Introduce el peso: ")),float(input("Introduce altura: ")))
print(persona1)
print(persona1.mayorEdad())
print(persona1.calcularIMC())

print("Introduce los datos de la segunda persona: ")
persona2 = Persona(input("Introduce el nombre: "),int(input("Introduce la edad: ")),input("Introduce el DNI: "), input("Introduce el sexo (H/M)"))
print(persona2)
print(persona2.mayorEdad())
print(persona2.calcularIMC())

print("Introduce los datos de la tercera persona: ")
persona3 = Persona()
persona3.setNombre(input("Introduce el nombre: "))
persona3.setEdad(int(input("Introduce la edad: ")))
persona3.setDni(input("Introduce el DNI: "))
persona3.setSexo(input("Introduce el sexo (H para hombre, M para mujer): "))
persona3.setPeso(float(input("Introduce el peso: ")))
persona3.setAltura(float(input("Introduce altura: ")))
print(persona3)
print(persona3.mayorEdad())
print(persona3.calcularIMC())