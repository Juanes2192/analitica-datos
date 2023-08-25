print("Bienvenido al juego AHORCADO.")

def ahorcado():
  cadena = str(input("Ahora Digite una palabra: "))
  cadenaMayuscula=cadena.upper()

  lista = list(cadenaMayuscula)

  return lista

palabraFija=ahorcado()

palabraOculta=[]

for i in range(0,len(palabraFija)):
  palabraOculta.append("_")

contador=0
vidas=5


x=1

while x!=0:
  print("Tienes ",vidas," vidas.")
  print(palabraOculta)
  letra=str(input("Digite una letra: "))[0]
  letraMayuscula=letra.upper()

  if letraMayuscula in palabraFija:
    print("La letra '",letraMayuscula,"' esta en la palabra.")

    for i in range(0,len(palabraFija)):
      if letraMayuscula == palabraFija[i]:
        palabraOculta[i]=palabraFija[i]
        contador+=1
        if contador==len(palabraFija):
          x=0
          print("Muy bien, lograste adivinar la palabra: ",palabraFija)

  else:
    vidas-=1
    print("La letra '",letraMayuscula,"' no esta en la palabra.")
    print("Te quedan ",vidas," vidas restantes  PILAS!!!.")
    if vidas==0:
      x=0
      print("Estas ahorcado lo siento...")

  print("\n")