from sympy import *

x, y, z = symbols("x,y,z")

func = raw_input("Ingrese la Funcion: \n")
pa = raw_input("Ingrese el punto: \n")
tol = 0.0001

func = sympify(func)

fdiff = diff(func, x)
ev = 1
resu = 0
ite = 0

if fdiff.subs(x, 0.4) < 1:

  while ev > 0.1:

    ite += 1
    fevala = func.subs(x, pa)
    eu = abs(pa - fevala)

    if eu < tol:
      ev = 0
      print(str(resu))

    elif ite == 100:
      print("No hay Punto Fijo")
      ev = 0

    else:
      pa = fevala
    resu = pa 
    
else:
  print ("No converge en el punto dado")