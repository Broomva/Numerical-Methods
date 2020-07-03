from sympy import *

x, y, z = symbols("x,y,z,")

func = raw_input("Ingrese Funcion: \n")
a = raw_input("Ingrese Punto a \n")
b = raw_input("Ingrese Punto b \n")
tol = 0.00000001

a = float(a)
b = float(b)

func = sympify(func)
evala = func.subs(x, a)
evalb = func.subs(x, b)

while abs(evalb) > tol:
  xm = b - ((b - a) / (evalb - evala) * evalb)
  pb = xm
  evalb = func.subs(x, pb)

xm = str(xm)[:6]
print(str(xm))
