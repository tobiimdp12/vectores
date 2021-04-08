import math
class punto():
    #atributos
    def __init__(self,cord_x=0,cord_y=0):
    
            self.cord_x=cord_x
            self.cord_y=cord_y
    #metodos
    def __str__(self):
        
        return"P({},{})".format(self.cord_x,self.cord_y)
    
    def cuadrante(self):
        if(self.cord_x>0 and self.cord_y>0):
            print("{},{} nos encontramos sobre el cuadrante 1".format(self.cord_x,self.cord_y))
        elif(self.cord_x<0 and self.cord_y>0):
            print("{},{} nos encontramos sobre el cuadrante 2".format(self.cord_x,self.cord_y))
        elif(self.cord_x<0 and self.cord_y<0):
            print("{},{} nos encontramos sobre el cuadrante 3".format(self.cord_x,self.cord_y))
        elif(self.cord_x>0 and self.cord_y<0):
            print("{},{} nos encontramos sobre el cuadrante 4".format(self.cord_x,self.cord_y))
        elif(self.cord_x!=0 and self.cord_y==0):
            print("nos encontramos en el eje x")
        elif(self.cord_x==0 and self.cord_y!=0):
            print("nos encontramos en el eje y")
        else:
            print("nos encontramos sobre el origen")
    
    def vector(self,p):

        vector_resultado=(p.cord_x-self.cord_x)
        vector_resultado_2=(p.cord_y-self.cord_y)
        print("(",vector_resultado,",",vector_resultado_2,")")

    def calcular_distancia(self,p):
        d=math.sqrt(pow((p.cord_x-self.cord_x),2)+pow((p.cord_y-self.cord_y),2))
        return d
    
class Rectangulo:
    def __init__(self,inicial=punto(),final=punto()):
            self.inicial=inicial
            self.final=final
            #Como no poseemos una base definida 
            #es decir por ejemplo base =4
            #buscamos la diferencia entre los dos puntos en el eje x
            self.vBase = abs(self.final.cord_x - self.inicial.cord_x)
            #Como no poseemos una altura definida 
            #es decir por ejemplo altura =3
            #buscamos la diferencia entre los dos puntos en el eje y
            self.vAltura = abs(self.final.cord_y - self.inicial.cord_y)
            self.vArea = self.vBase * self.vAltura#calculamos el area


    def base(self):
        print("la base es->",self.vBase)
    def altura(self):
        print("la altura es->",self.vAltura)
    def area(self):
        print("el area es->",self.vArea)    

#Crea los puntos A(2, 3), B(5,5), C(-3, -1) y D(0,0) e imprimelos por pantalla.
A=punto(2,3)
B=punto(5,5)
C=punto(-3,-1)
D=punto(0,0)

print(str(A))
print(str(B))
print(str(C))
print(str(D))
#Consulta a que cuadrante pertenecen el punto A, C y D.
A.cuadrante()
C.cuadrante()
D.cuadrante()
#Consulta los vectores AB y BA
A.vector(B)
B.vector(A)
#(Optativo) Consulta la distancia entre los puntos 'A y B' y 'B y A'.
d=A.calcular_distancia(B)
print("la distancia entre los dos puntos es->",round(d, 2))
d=B.calcular_distancia(A)
print("la distancia entre los dos puntos es->",round(d, 2))

#(Optativo) Determina cual de los 3 puntos A, B o C, 
# se encuentra más lejos del origen, punto (0,0).
origen=punto(0,0)
#si la distancia entre A y origen es mayor a la de B y a la de C
if(A.calcular_distancia(origen)>B.calcular_distancia(origen)>C.calcular_distancia(origen)):
    print("A es el punto mas alejado de origen")
#si la distancia entre B y origen es mayor a la de A y a la de C
elif(B.calcular_distancia(origen)>A.calcular_distancia(origen)>C.calcular_distancia(origen)):
    print("B es el punto mas alejado de origen")

else:
    print("C es el punto mas alejado de origen")

#Crea un rectángulo utilizando los puntos A y B.
rectangulo_1=Rectangulo(A,B)

#Consulta la base, altura y área del rectángulo.
rectangulo_1.base()
rectangulo_1.altura()
rectangulo_1.area()