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
y=1
conectado=bool;
#INVENTARIO BILLETES Y MONEDAS
monedas50=20
monedas100=20
monedas200=20
monedas500=20
monedas1000=20
billetes1000=20
billetes2000=20
billetes5000=20
billetes10000=20
billetes20000=20
billetes50000=10
billetes100000=5
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
  elif (soporte==2):
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
          print(caja)
        elif(Opcion==2):
          print("Ingrese billetes/monedas a tomar: \n")
          print("1. monedas de 50 \n2. monedas de 100 \n3. monedas de 200 \n4. monedas de 500 \n5. monedas de 1000 \n6. billetes de 1000 \n7. billetes de 2000 \n8. billetes de 5000 \n9. billetes de 10000 \n10. billetes de 20000 \n11. billetes de 50000 \n")
          totalvueltas=0
          while y==1:
            VueltasCaja = int(input("INGRESE NUMERO 1 A 11 \n"))
            if (VueltasCaja==1):
              x = int(input("cantidad de monedas a tomar? \n")) 
              if (x<=monedas50):
                totalvueltas =(totalvueltas+(50*x))
                monedas50=monedas50-x
              else:
                print("cantidad en la caja insuficiente")    
            elif(VueltasCaja==2):
              x = int(input("cantidad de monedas a tomar? \n"))
              if (x<=monedas100):
                totalvueltas =(totalvueltas+(100*x))
                monedas100=monedas100-x 
              else:
                print("cantidad en la caja insuficiente")   
            elif (VueltasCaja==3):
              x = int(input("cantidad de monedas a tomar? \n"))
              if (x<=monedas200):
                totalvueltas =(totalvueltas+(200*x))
                monedas200=monedas200-x 
              else:
                print("cantidad en la caja insuficiente")   
            elif (VueltasCaja==4):
              x = int(input("cantidad de monedas a tomar?\n"))
              if (x<=monedas500):
                totalvueltas =(totalvueltas+(500*x))
                monedas500=monedas500-x 
              else:
                print("cantidad en la caja insuficiente")   
            elif (VueltasCaja==5): 
              x = int(input("cantidad de monedas a tomar? \n"))
              if (x<=monedas1000):
                totalvueltas =(totalvueltas+(1000*x))
                monedas1000=monedas1000-x 
              else:
                print("cantidad en la caja insuficiente")         
            elif (VueltasCaja==6):
              x = int(input("cantidad de billetes a tomar? \n"))
              if (x<=billetes1000):
                totalvueltas =(totalvueltas+(1000*x))
                billetes1000=billetes1000-x 
              else:
                print("cantidad en la caja insuficiente")         
            elif (VueltasCaja==7): 
              x = int(input("cantidad de billetes a tomar? \n"))
              if (x<=billetes2000):
                totalvueltas =(totalvueltas+(2000*x))
                billetes2000=billetes2000-x            
            elif (VueltasCaja==8):
              x = int(input("cantidad de billetes a tomar? \n"))
              if (x<billetes5000):
                totalvueltas =(totalvueltas+(5000*x))
                billetes5000=billetes5000-x 
            elif (VueltasCaja==9):
              x = int(input("cantidad de billetes a tomar? \n"))
              if (x<=billetes10000):
                totalvueltas =(totalvueltas+(10000*x))
                billetes10000=billetes10000-x      
            elif (VueltasCaja==10):
              x = int(input("cantidad de billetes a tomar? \n"))
              totalvueltas =(totalvueltas+(20000*x))
              if (x<=billetes20000):
                totalvueltas =(totalvueltas+(20000*x))
                billetes20000=billetes20000-x                       
            elif (VueltasCaja==11):
              x = int(input("cantidad de billetes a tomar? \n"))
              if (x<=billetes50000):
                totalvueltas =(totalvueltas+(50000*x))
                billetes50000=billetes50000-x   
            print ("desea retirar mas cambio?") 
            y = int(input("1) Si \n2) No \n")) 
          print("cambio retirado:")
          print(totalvueltas)
          print("Nuevo saldo caja")
          print(caja-totalvueltas)
          caja=caja-totalvueltas
          y=1
        elif(Opcion==3):
          print("Gracias por usar el Cajero EAN 🙌")
          print("......................................:CAJERO.EAN:..................................")
          print("")
          break 
  elif (soporte==3):
        print("\t.:MENU RESTAURANTE 🍽️:.")
        print("")
        print("1. Consultar dinero caja 💵")
        print("2. Retirar vueltas 🎫")
        print("3. SALIR 🔚")
        print("......................................:CAJERO.EAN:..................................")
        Opcion=int(input("Digite una opcion de MENU: "))
        print("")
        if (Opcion==1):
          print("Monto total en la caja ")
          print(caja)
        elif(Opcion==2):
          print("Ingrese billetes/monedas a tomar: \n")
          print("1. monedas de 50 \n2. monedas de 100 \n3. monedas de 200 \n4. monedas de 500 \n5. monedas de 1000 \n6. billetes de 1000 \n7. billetes de 2000 \n8. billetes de 5000 \n9. billetes de 10000 \n10. billetes de 20000 \n11. billetes de 50000 \n")
          totalvueltas=0
          while y==1:
            VueltasCaja = int(input("INGRESE NUMERO 1 A 11 \n"))
            if (VueltasCaja==1):
              x = int(input("cantidad de monedas a tomar? \n")) 
              if (x<=monedas50):
                totalvueltas =(totalvueltas+(50*x))
                monedas50=monedas50-x
              else:
                print("cantidad en la caja insuficiente")    
            elif(VueltasCaja==2):
              x = int(input("cantidad de monedas a tomar? \n"))
              if (x<=monedas100):
                totalvueltas =(totalvueltas+(100*x))
                monedas100=monedas100-x 
              else:
                print("cantidad en la caja insuficiente")   
            elif (VueltasCaja==3):
              x = int(input("cantidad de monedas a tomar? \n"))
              if (x<=monedas200):
                totalvueltas =(totalvueltas+(200*x))
                monedas200=monedas200-x 
              else:
                print("cantidad en la caja insuficiente")   
            elif (VueltasCaja==4):
              x = int(input("cantidad de monedas a tomar?\n"))
              if (x<=monedas500):
                totalvueltas =(totalvueltas+(500*x))
                monedas500=monedas500-x 
              else:
                print("cantidad en la caja insuficiente")   
            elif (VueltasCaja==5): 
              x = int(input("cantidad de monedas a tomar? \n"))
              if (x<=monedas1000):
                totalvueltas =(totalvueltas+(1000*x))
                monedas1000=monedas1000-x 
              else:
                print("cantidad en la caja insuficiente")         
            elif (VueltasCaja==6):
              x = int(input("cantidad de billetes a tomar? \n"))
              if (x<=billetes1000):
                totalvueltas =(totalvueltas+(1000*x))
                billetes1000=billetes1000-x 
              else:
                print("cantidad en la caja insuficiente")         
            elif (VueltasCaja==7): 
              x = int(input("cantidad de billetes a tomar? \n"))
              if (x<=billetes2000):
                totalvueltas =(totalvueltas+(2000*x))
                billetes2000=billetes2000-x            
            elif (VueltasCaja==8):
              x = int(input("cantidad de billetes a tomar? \n"))
              if (x<=billetes5000):
                totalvueltas =(totalvueltas+(5000*x))
                billetes5000=billetes5000-x 
            elif (VueltasCaja==9):
              x = int(input("cantidad de billetes a tomar? \n"))
              if (x<=billetes10000):
                totalvueltas =(totalvueltas+(10000*x))
                billetes10000=billetes10000-x      
            elif (VueltasCaja==10):
              x = int(input("cantidad de billetes a tomar? \n"))
              totalvueltas =(totalvueltas+(20000*x))
              if (x<=billetes20000):
                totalvueltas =(totalvueltas+(20000*x))
                billetes20000=billetes20000-x                       
            elif (VueltasCaja==11):
              x = int(input("cantidad de billetes a tomar? \n"))
              if (x<=billetes50000):
                totalvueltas =(totalvueltas+(50000*x))
                billetes50000=billetes50000-x   
            print ("desea retirar mas cambio?") 
            y = int(input("1) Si \n2) No \n")) 
          print("cambio retirado:")
          print(totalvueltas)
          print("Nuevo saldo caja")
          print(caja-totalvueltas)
          caja=caja-totalvueltas
          y=1
        elif(Opcion==3):
          print("Gracias por usar el Cajero EAN 🙌")
          print("......................................:CAJERO.EAN:..................................")
          print("")
          break 
  else: 
        print("ERROR, Opcion no valida para el cajero EAN 🛑 ❌")
        break