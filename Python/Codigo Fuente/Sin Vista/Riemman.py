from sympy import *

x, y, z = symbols("x,y,z")

func = raw_input("Ingrese la Funcion: \n")
pa = raw_input("Ingrese el limite superior: \n")
pb = raw_input("Ingrese el limite inferior: \n")

pa = float(pa)
pb = float(pb)

func = sympify(func)
fevala = func.subs(x,pa)
fevalb = func.subs(x,pb)

fint = integrate(func,x)

area = float(func.subs(x, pa))-float(func.subs(x,pb))

print("El area bajo la curva es: " +str(area))

plot(fevala, fevalb, fint)

