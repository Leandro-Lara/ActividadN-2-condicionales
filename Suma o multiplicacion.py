print("Bienvendio")
print("digite su primer numero")
number1=int(input())
print("Digite su segundo numero")
number2=int(input())
multiplication=number1*number2
addition=number1+number2
if number1<0 or number2 <0 :
  print("La suma entre estos dos numeros es:", addition)
elif number1>0 and number2 >0 :
  print("El resultado de multiplicar los dos numeros es:", multiplication)