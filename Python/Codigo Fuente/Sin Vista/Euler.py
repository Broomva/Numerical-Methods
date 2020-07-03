from sympy import * 

x, y, z = symbols("x,y,z")

func = raw_input("Ingrese la Ecuacion Diferencial: \n")
px = raw_input("Ingrese el valor de x: \n")
py = raw_input("Ingrese el valor de y: \n")
h = raw_input("Ingrese el valor de h: \n")
n = raw_input("Ingrese el de iteraciones: \n")

px = float(px)
py = float(py)
h = float(h)
n = int(n)



func = sympify(func)
fdiff = diff(func, x, y) #dx/dy

print("Funcion Derivada" + str(fdiff))

i = 1

for i in range(n):
  s = h + px
  y1 = fdiff.subs([(x, px), (y, py)])
  hy1 = h*y1
  y2 = py + hy1
  y3 = fdiff.subs([(x, s), (y, y2)])
  hy2 = y3*h
  yn = py+((hy1+hy2)/2)
  py = yn
  px = px + h
  print ("Punto x: " + str(px))
  print ("Punto y: " + str(py)) 
  print ("Punto hy1: " + str(hy1)) 
  print ("Punto y2: " + str(y2)) 
  print ("Punto hy2: " + str(hy2))
  print ("Punto yn: " + str(yn)) 
  plot(x, hy1,x, y1)
