print("Bienvenido")
print("¿Cuantas horas trabaja el primer empleado?")
hours1_employee = int (input())
print("¿Cuantas horas extra trabaja el primer empleado?")
extrahours1_employee = int(input())
print("¿Cuantas horas trabaja el segundo empleado?")
hours2_employee = int (input())
print("¿Cuantas horas extra trabaja el segundo empleado?")
extrahours2_employee = int(input())
multiplication = hours1_employee*4 
m2=extrahours1_employee*8
suma=multiplication+m2
multiplication2 = hours2_employee*4 
m23=extrahours2_employee*8
suma2=multiplication2+m23
if hours1_employee >0 : 
    print("el sueldo de las horas trabajas del primer empleado es de:",multiplication)
    print("El sueldo de las horas extra trabajadas por el primer empleado es de:", m2)
    print("En total el sueldo obtenido por las horas trabajadas del primer empleado es de:",suma)
else:
    print("El empleado no a trabajado ni una hora por lo que no a ganado nada")
if hours2_employee >0 : 
    print("el sueldo de las horas trabajas del segundo empleado es de:",multiplication2)
    print("El sueldo de las horas extra trabajadas por el segundo empleado es de:", m23)
    print("En total el sueldo obtenido por las horas trabajadas del segundo empleado es de:",suma2)
else:
    print("El empleado no a trabajado ni una hora por lo que no a ganado nada")
