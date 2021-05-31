"""
#Entradas
Usuario-->input-->U
Contraseña-->input-->C
Opcion 1-->int-->1
Opcion 2-->int-->2
Opcion 3-->int-->3
Opcion 4-->int-->4
#Salidas
Operaciones-->float-->O.realizadas
"""
from datetime import datetime
ahora=datetime.now()
print(ahora.strftime('%Y-%m-%d %H:%M:%S'))
Cuentas=[]
print("......................................:CAJERO.EAN:..................................")
print("Por la seguridad del usuario solo es permitido 3 intentos para ingresar a su cuenta 😎")
#CAJERO EAN
usuario="1818"
passw="2027"
cont=0
saldo=500000
parqueadero=1795000
restaurante=1795000
conectado=bool;
caja=1795000
while cont<3:
    us=input("Ingrese usuario 🙍 : ");
    co=input("Ingrese contraseña 🔑 : ");
    if us==usuario and passw==co:
        print("......................................:CAJERO.EAN:..................................")
        print ("Bienvenido al sistema 💰 ")
        print ("Escoja el soporte a solicitar:")
        print("1. BANCO EAN 💰 ")
        print("2. PARQUEADERO EAN 🚗")
        print("3. RESTAURANTE EAN 🍽️")
        print("......................................:CAJERO.EAN:..................................")
        soporte=int(input("Digite una opcion de MENU: "))
        conectado=True
        break
    else:
        cont=cont+1;
        print ("Usuario y contraseña incorrecta ❌")
        conectado=False
while conectado:
  if (soporte==1): 
        print("......................................:CAJERO.EAN:..................................") 
        print("\t.:MENU BANCO:.")
        print("")
        print("1. Consultar saldo🔍")
        print("2. Retirar dinero 💵")
        print("3. Transferir 💸")
        print("4. SALIR 🔚")
        print("......................................:CAJERO.EAN:..................................")
        Opcion=int(input("Digite una opcion de MENU: "))
        print("")
        if(Opcion==1):
          print ("Su saldo es:", saldo)
          print("")
        elif(Opcion==2):
          Retiro=int(input("Digite la cantidad que desea retirar: "))
          cant500 = Retiro // 50000
          resto500 = Retiro % 50000 
          cant200 = resto500 // 20000
          resto200 = resto500 % 20000
          cant100 = resto200 // 10000
          resto100 = resto200 % 10000
          cant50 = resto100 // 5000
          resto50 = resto100 % 5000
          cant20 = resto50 // 2000
          resto20 = resto50 % 2000
          cant10 = resto20 // 1000
          resto10 = resto20 % 1000
          cant5 = resto10 // 500
          resto5 = resto10 % 500
          cant2 = resto5 // 200
          resto2 = resto5 % 200
          cant1 = resto2 // 100
          resto1 = resto2 % 100
          cantcin = resto1 // 50
          restocin = resto1 % 50
          print("......................................:CAJERO.EAN:..................................")
          print(" billetes de 50000  a salir 💸: ", cant500)
          print(" billetes de 20000 a salir 💸: ", cant200)
          print(" billetes de 10000 a salir 💸: ", cant100)
          print(" billetes de 5000 a salir 💸: ", cant50)
          print(" billetes de 2000 a salir💸: ", cant20)
          print(" billetes de 1000 a salir💸: ", cant10)
          print(" monedas de 500 a salir💸: ", cant5)
          print(" monedas de 200 a salir💸: ", cant2)
          print(" monedas de 100 a salir💸: ", cant1)
          print(" monedas de 50 a salir💸: ", cantcin)
          print(f"Operacion realizada, su saldo actual es: {saldo-Retiro}")
          saldo=saldo-Retiro
          if Retiro>saldo:
            print("No tiene saldo disponible 🙁")
            print("......................................:CAJERO.EAN:..................................")
            print("")
        elif(Opcion==3):
            cu2=input("Ingrese cuenta a Depositar: ")
            Cuentas.append(cu2)    
            monto=int(input("Ingrese monto a Transferir: "))
            saldo=saldo-monto
            saldo2=saldo
            print ("Se han transferido", monto,"pesos a la cuenta",cu2, "✔")
            print ("El nuevo saldo es:",saldo)
            print("")
        elif(Opcion==4):
          print("Gracias por usar el Cajero EAN 🙌")
          print("......................................:CAJERO.EAN:..................................")
          print("")
          break 
        else:
            print("ERROR, Opcion no valida para el cajero EAN 🛑 ❌")
            break
  elif(soporte==2):
        print("\t.:MENU PARQUEADERO 🚗:.")
        print("")
        print("1. Consultar dinero caja 💵")
        print("2. Retirar vueltas 🎫")
        print("3. SALIR 🔚")
        print("......................................:CAJERO.EAN:..................................")
        Opcion=int(input("Digite una opcion de MENU: "))
        print("")
        if (Opcion==1):
          print("Monto total en la caja ")
          print(parqueadero)
        elif(Opcion==2):
          x=int(input("Digite la cantidad de vueltas retirar: "))
          cant500 = Retiro // 50000
          resto500 = Retiro % 50000 
          cant200 = resto500 // 20000
          resto200 = resto500 % 20000
          cant100 = resto200 // 10000
          resto100 = resto200 % 10000
          cant50 = resto100 // 5000
          resto50 = resto100 % 5000
          cant20 = resto50 // 2000
          resto20 = resto50 % 2000
          cant10 = resto20 // 1000
          resto10 = resto20 % 1000
          cant5 = resto10 // 500
          resto5 = resto10 % 500
          cant2 = resto5 // 200
          resto2 = resto5 % 200
          cant1 = resto2 // 100
          resto1 = resto2 % 100
          cantcin = resto1 // 50
          restocin = resto1 % 50
          print("......................................:CAJERO.EAN:..................................")
          print(" billetes de 50000  a salir 💸: ", cant500)
          print(" billetes de 20000 a salir 💸: ", cant200)
          print(" billetes de 10000 a salir 💸: ", cant100)
          print(" billetes de 5000 a salir 💸: ", cant50)
          print(" billetes de 2000 a salir💸: ", cant20)
          print(" billetes de 1000 a salir💸: ", cant10)
          print(" monedas de 500 a salir💸: ", cant5)
          print(" monedas de 200 a salir💸: ", cant2)
          print(" monedas de 100 a salir💸: ", cant1)
          print(" monedas de 50 a salir💸: ", cantcin)
          print(f"Operacion realizada, su saldo actual es: {parqueadero-x}")
          parqueadero=parqueadero-x
          if x>parqueadero:
            print("No tiene saldo disponible 🙁")
            print("......................................:CAJERO.EAN:..................................")
            print("")
        elif(Opcion==3):
          print("Gracias por usar el Cajero EAN 🙌")
          print("......................................:CAJERO.EAN:..................................")
          print("")
          break 
        else:
            print("ERROR, Opcion no valida para el cajero EAN 🛑 ❌")
            break
  elif (soporte==3):
        print("")
        print("\t.:MENU RESTAURANTE EAN 🍽️:.")
        print("")
        print("1. Consultar dinero caja 💵")
        print("2. Retirar vueltas 🎫")
        print("3. SALIR 🔚")
        print("......................................:CAJERO.EAN:..................................")
        Opcion=int(input("Digite una opcion de MENU: "))
        print("")
        if (Opcion==1):
          print("Monto total en la caja ")
          print(restaurante)
        elif(Opcion==2):
          x=int(input("Digite la cantidad de vueltas retirar: "))
          cant500 = Retiro // 50000
          resto500 = Retiro % 50000 
          cant200 = resto500 // 20000
          resto200 = resto500 % 20000
          cant100 = resto200 // 10000
          resto100 = resto200 % 10000
          cant50 = resto100 // 5000
          resto50 = resto100 % 5000
          cant20 = resto50 // 2000
          resto20 = resto50 % 2000
          cant10 = resto20 // 1000
          resto10 = resto20 % 1000
          cant5 = resto10 // 500
          resto5 = resto10 % 500
          cant2 = resto5 // 200
          resto2 = resto5 % 200
          cant1 = resto2 // 100
          resto1 = resto2 % 100
          cantcin = resto1 // 50
          restocin = resto1 % 50
          print("......................................:CAJERO.EAN:..................................")
          print(" billetes de 50000  a salir 💸: ", cant500)
          print(" billetes de 20000 a salir 💸: ", cant200)
          print(" billetes de 10000 a salir 💸: ", cant100)
          print(" billetes de 5000 a salir 💸: ", cant50)
          print(" billetes de 2000 a salir💸: ", cant20)
          print(" billetes de 1000 a salir💸: ", cant10)
          print(" monedas de 500 a salir💸: ", cant5)
          print(" monedas de 200 a salir💸: ", cant2)
          print(" monedas de 100 a salir💸: ", cant1)
          print(" monedas de 50 a salir💸: ", cantcin)
          print(f"Operacion realizada, su saldo actual es: {restaurante-x}")
          restaurante=restaurante-x
          if x>restaurante:
            print("No tiene saldo disponible 🙁")
            print("......................................:CAJERO.EAN:..................................")
            print("")
        elif(Opcion==3):
          print("Gracias por usar el Cajero EAN 🙌")
          print("......................................:CAJERO.EAN:..................................")
          print("")
          break 
        else:
            print("ERROR, Opcion no valida para el cajero EAN 🛑 ❌")
            break