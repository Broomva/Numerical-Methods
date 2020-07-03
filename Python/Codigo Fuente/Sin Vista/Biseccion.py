from sympy import * 

x, y, z = symbols("x,y,z")

ecuacion = raw_input("Ingrese la Ecuacion: \n")
pa = raw_input("Ingrese el Punto a: \n")
pb = raw_input("Ingrese el Punto b: \n")

ec = sympify(ecuacion)
evala = ec.subs(x, pa)
evalb = ec.subs(x, pb)

if evala*evalb<0:
  pmedioab = 0.1

  while pmedioab<0.00000001:

    pmedio = (pa+pb)/2
    evala = ec.subs(x,pa)
    evalb = ec.subs(x,pb)
    evalpmedio = ec.subs(x,pmedio)

    if evala*evalpmedio<0:
      pb = pmedio

    elif evala*evalpmedio<0:
      pa = pmedio

    pmedioab = abs(evalpmedio)
    resultado = pmedio

  print(str(resultado))

else:
  print("No existe raiz en ese intervalo")