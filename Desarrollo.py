"""
#Entradas
Usuario-->input-->U
Contraseña-->input-->C
Opcion 1-->int-->1
Opcion 2-->int-->2
Opcion 3-->int-->3
Opcion 3-->int-->4
#Salidas
Operaciones-->float-->O.realizadas
"""
print("......................................:CAJERO.EAN:..................................")
print("Por la seguridad del usuario solo es permitido 3 intentos para ingresar a su cuenta")
#CAJERO EAN
print("")
contador=1
lista=["BancoEAN","1234"]
while contador <=3:
  u=input("Digite su usuario: ")
  c=input("Digite contraseña: ") 
  if (u==lista[0]):
    if(c==lista[1]):
      Saldoban=100000
      print("Bienvenido a cajero EAN: ")
      contador==4
      print(".....................................EAN.................................")
    else:
      print("contraseña incorrecta ")
  else:
       print("usuario no recococido")
       if contador==3:
           print("comuniquese con el administrrador")
  contador=contador +1
  break
print("\t.:MENU:.")
print("")
print("1. consultar saldo")
print("2. Retirar dinero")
print("3. transferir dinero a otra cuenta")
print("4. SALIR")
print(".....................................EAN.................................")
Opcion=int(input("Digite una opcion de MENU: "))
print("")
if(Opcion==2):
    Retiro=float(input("Digite la cantidad que desea retirar: "))
    print(f"Operacion realizada, su saldo actual es: {Saldoban-Retiro}")
    if Retiro>Saldoban:
      print("noTIENE el saldo digitado")
    else:
      print(f"Dinero en la cuenta es: {Saldoban-Retiro}")
      print(".....................................EAN.................................") 
elif(Opcion==1):
  print(f"Dinero en la cuenta es: {Saldoban-Retiro}")
  print(".....................................EAN.................................")
  print("")
elif(Opcion==3):
 Cuenta2=float(input("Ingrese el numero de cuenta a quien desea tranferir: "))
 if(Cuenta2==12345):
      trans=float(input("Digite la cantidad que desea  tranferir: "))
      print(f"Operacion realizada, su saldo actual es: {Saldoban-trans}")
      if trans>Saldoban:
        print("noTIENE el saldo digitado")
        print(".....................................EAN.................................")
        print("")
elif(Opcion==4):
  print("gracias por usar el cajero EAN")
  print(".....................................EAN.................................")
  print("")
else:
  print("ERROR, Opcion no valida para el cajero EAN")

    
  
    
    




