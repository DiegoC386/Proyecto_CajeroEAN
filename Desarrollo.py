"""
Entradas
Usuario-->input-->U
Contraseña-->int-->C
Opcion 1-->int-->1
Opcion 2-->int-->2
Opcion 3-->int-->3
Salidas
Operacion realizada-->float-->OR
"""
lista=["7890","2345"]
while True:
  u=input("digite usuario: ")
  c=input("digite cintraseña: ") 
  if (u==lista[0]):
    if(c==lista[1]):
      print("Bienvenido a cajero EAN: ")
      break 
  Retirar dinero=1
  Consultar saldo=2
  Transferir dinero=3

  O=int(input("Digite según la operación que desea realizar: Retirar dinero (1), consultar saldo (2), transferir dinero a otra cuenta (3)"))

  if(O==1):
    Cantidad a retirar=float(input("Digite la cantidad que desea retirar."))
    print("Operacion realizada")
   
  elif(O==2):
   consultar=int(input("Si requiere consultar el saldo en su cuenta digite (6)"))
    if(verificar==6):

      #Según el monto de cada dependencia 
      monto=10000000
      saldo=monto-cantidad a retirar
      print("Saldo actual: "+str(saldo))

  elif(0==3):
    Cuenta2=float(input("Ingrese el numero de cuenta a quien desea tranferir: "))
    
    Cuenta2=x

    if(cuenta2==x):
      print("Digite el dinero a transferir: ")
    
    
  

    
  
    
    




