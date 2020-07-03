from sympy import *

x, y, z = symbols("x y z")

func = raw_input("Ingrese la Funcion: \n")
func = sympify(func)

xn = raw_input("Ingrese el valor de xm: \n")
func = func.subs(x, xn)
funcdff = diff(func,x)
funcdff = funcdff.subs(x, xn)
if funcdff == 0:
  funcdff += 0.01

res = float(xn) - (float(func)/float(funcdff))
print("La raiz es: " + str(res))