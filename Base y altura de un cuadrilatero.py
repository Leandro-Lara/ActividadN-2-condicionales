print("Bienvenido")
print("Ingrese la base de su cuadrilatero")
base=int(input())
print("ingresela altura de su cuadrilatero")
height=int(input())
area=base*height
perimetersquare=base*4
rect=base*2
angulo=height*2
perimeterrectangle=rect+angulo
if base==height:
  print("Usted tiene un cuadrado")
  print("el area de su cuadrado es:",area)
  print("el perimetro de su cuadrado es",perimetersquare)
else:
  print("usted tiene un rectangulo")
  print("El area de su rectangulo es", area)
  print("El perimetro de su rectangulo es", perimeterrectangle)