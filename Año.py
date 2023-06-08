print("Bienvenido")
print("Ingrese la cantidad ias que tiene el año")
year=int(input())
if year==366:
  print("El año es bicisesto")
elif year==365:
  print("el año es normal")
else:
  print("un año no tiene esa cantidad de dia, intente nuevamente con otra cantidad de dias")