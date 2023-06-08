print("Bienvenido")
print("Infrese el valor de su compra")
buy=int(input())
5%buy
10%buy
15%buy
caso1=buy-5%buy
caso2=buy-10%buy
caso3=buy-15%buy
if buy<100:
  print("el descuento realizado es de:",5%buy)
  print("Y el precio final con el descuneto aplicado es de",caso1)
elif buy==100 or buy>100 and buy<200:
  print("el descuento realizado es de:",10%buy)
  print("Y el precio final con el descuneto aplicado es de",caso2)
elif buy>200:
  print("el descuento realizado es de:",15%buy)
  print("Y el precio final con el descuneto aplicado es de",caso3)