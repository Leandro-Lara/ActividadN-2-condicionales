print("Bienvenido")
print("Digite su primer numero")
number1=int(input())
print("Digite su segundo numero")
number2=int(input())
print("Digite su tercer numero")
number3=int(input())
if number1 > number2 and number1 > number3 :
    print("El numero mayor de los 3 numeros es el primero")
elif number2 > number1 and number2 > number3:
    print("El numero mayor de los 3 numeros es el segundo")
elif number3 > number1 and number3 > number2:  
    print("El numero mayor de los 3 numeros es el tercero")
if number1 < number2 and number1 < number3 :
    print("El menor de los 3 numeros es el primero")
elif number2 < number1 and number2 < number3 :
    print("El menor de los 3 numeros es el segundo")
elif number3 < number2 and number3 < number1 :
    print("El menor de los 3 numeros es el tercero")