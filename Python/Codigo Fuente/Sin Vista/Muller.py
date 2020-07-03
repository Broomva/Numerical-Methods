from sympy import *
x, y, z = symbols("x,y,z")

func = raw_input("Ingrese la Funcion: \n")
func = sympify(func)

x0 = float(raw_input("Ingrese punto x0: \n"))
x1 = float(raw_input("Ingrese punto x1: \n"))
x2 = float(raw_input("Ingrese punto x2: \n"))

x0 = float(x0)
x1 = float(x1)
x2 = float(x2)

h0 = x1 - x0
h1 = x2 - x1

feval0 = func.subs(x, x0)
feval1 = func.subs(x, x1)
feval2 = func.subs(x, x2)

t0 = (feval1 - feval2)/h0
t1 = (feval2 - feval1)/h1

a = (t1-t0)/(h1+h0)
b = (a*h1)+t0
c = feval2

rz = b**2-4*a*c
if rz < 0:
  print("Raiz Compleja")
  exit()




x3plus = x2 + ((-2*c)/(b+math.sqrt(b**2-4*a*c)))
x3min = x2 + ((-2*c)/(b-math.sqrt(b**2-4*a*c)))

ifxplus = b+math.sqrt(b**2-4*a*c)
ifxmin = b-math.sqrt(b**2-4*a*c)

muller = 0

if ifxplus>ifxmin:
  muller = x3plus
  print("La respuesta es: " + str(muller))
else:
  muller = x3min
  print("La respuesta es: " + str(muller))
