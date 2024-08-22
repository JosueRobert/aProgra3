"""
name =input("Digita tu nombre: ")
if(name == "Alice"):
    if(name == "Alice"):
        print ("Hola Alice")
elif(name=="Angela"):
    print("Hola Angela")
else:
    print("Tu no eres Alice")
"""
nun1 = int(input("Escriba un numero"))
nun2 = int(input("Escriba otro numero"))
nun3 = int(input("Escriba otro numero"))

if (nun1>nun2 and nun1>nun3):
 print("El numero mayor es:{nun1}")
elif(nun2>nun1 and nun2>nun3):
  print("El numero  es{num2}")
elif(nun3>nun1 and nun3>nun2):
  print("El numero menor es{num3}")
elif(nun1==nun2 or nun2==nun3 or nun1 ==nun3 ):
  print("Hay numeros repetidos")
else:
  print("Los tres numeros son iguales") 