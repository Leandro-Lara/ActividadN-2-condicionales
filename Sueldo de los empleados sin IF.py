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
multiplicationhe = extrahours1_employee*8
sueldot=multiplication+multiplicationhe
multiplication2 = hours2_employee*4 
multiplicationhe2 = extrahours2_employee*8
sueldot2=multiplication2+multiplicationhe2
print("El sueldo de las horas trabajadas del primer empleado es:",multiplication)
print("El sueldo de las horas extra trabajadas del primer empleado es:",multiplicationhe)
print("El sueldo total de el primer empleado es:",sueldot)
print("El sueldo de las horas trabajadas del segundo empleado es:",multiplication2)
print("El sueldo de las horas extra trabajadas del segundo empleado es:",multiplicationhe2)
print("El sueldo total de el segundo empleado es:",sueldot2)