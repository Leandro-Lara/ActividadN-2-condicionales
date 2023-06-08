print("Bienvenido")
signo =  ["capricornio", "acuario", "piscis", "aries", "tauro", "geminis", "cancer", "leo" , "virgo" , "libra" , "Escopio", "sagitario"] 
fecha =   [20, 19, 20, 21, 21, 22, 22, 22, 22, 22, 21]
print("ingrese el numero de su mes de nacimiento")
mes=int(input())
print("Ingrese su dia de nacimiento")
dia=int(input())
mes = mes-1
if dia > fecha[mes]:
  mes = mes + 1
if mes == 12:
  mes = 0
print("Su signo zodiacal es", signo[mes])