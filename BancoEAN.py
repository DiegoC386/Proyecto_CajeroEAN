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
from datetime import datetime
ahora=datetime.now()
print(ahora.strftime('%Y-%m-%d %H:%M:%S'))
Cuentas=[]
print("......................................:CAJERO.EAN:..................................")
print("Por la seguridad del usuario solo es permitido 3 intentos para ingresar a su cuenta 😎")
#CAJERO EAN
usuario="DIEGO"
passw="1234"
saldo=500000
saldo2=100000
cont=0
conectado=bool;
while cont<3:
    us=input("Ingrese usuario 🙍 : ");
    co=input("Ingrese contraseña 🔑 : ");
    if us==usuario and passw==co:
        print("......................................:CAJERO.EAN:..................................")
        print ("Bienvenido al sistema 💰")
        conectado=True
        break
    else:
        cont=cont+1;
        print ("Usuario y contraseña incorrecta ❌")
        conectado=False
while conectado:
        print("......................................:CAJERO.EAN:..................................") 
        print("\t.:MENU:.")
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
          print(f"Operacion realizada, su saldo actual es: {saldo-Retiro}")
          if Retiro>saldo:
            print("No tiene saldo disponible 🙁")
            print("......................................:CAJERO.EAN:..................................")
            print("")
        elif(Opcion==3):
            cu2=input("Ingrese cuenta a Depositar: ")
            Cuentas.append(cu2)    
            monto=int(input("Ingrese monto a Transferir: "))
            saldo=saldo-monto
            saldo2=saldo2+monto
            print ("Se han transferido", monto,"pesos a la cuenta",cu2, "✔")
            print ("El nuevo saldo es:",saldo2)
            print("")
        elif(Opcion==4):
          print("Gracias por usar el Cajero EAN 🙌")
          print("......................................:CAJERO.EAN:..................................")
          print("")
          break 
        else:
            print("ERROR, Opcion no valida para el cajero EAN 🛑 ❌")
            break
            
