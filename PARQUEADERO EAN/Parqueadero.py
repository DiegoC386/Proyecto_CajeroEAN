"""
elif(soporte==2):
        print("\t.:MENU PARQUEADERO ๐:.")
        print("")
        print("1. Consultar dinero caja ๐ต")
        print("2. Retirar vueltas ๐ซ")
        print("3. SALIR ๐")
        print("......................................:CAJERO.EAN:..................................")
        Opcion=int(input("Digite una opcion de MENU: "))
        print("")
        if (Opcion==1):
          print("Monto total en la caja ")
          print(parqueadero)
        elif(Opcion==2):
          x=int(input("Digite la cantidad de vueltas retirar: "))
          cant500 = x // 50000
          resto500 = x % 50000 
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
          print("......................................:CAJERO.EAN:..................................")
          print(" billetes de 50000  a salir ๐ธ: ", cant500)
          print(" billetes de 20000 a salir ๐ธ: ", cant200)
          print(" billetes de 10000 a salir ๐ธ: ", cant100)
          print(" billetes de 5000 a salir ๐ธ: ", cant50)
          print(" billetes de 2000 a salir๐ธ: ", cant20)
          print(" billetes de 1000 a salir๐ธ: ", cant10)
          print(f"Operacion realizada, su saldo actual es: {parqueadero-x}")
          parqueadero=parqueadero-x
          if x>parqueadero:
            print("No tiene saldo disponible ๐")
            print("......................................:CAJERO.EAN:..................................")
            print("")
        elif(Opcion==3):
          print("Gracias por usar el Cajero EAN ๐")
          print("......................................:CAJERO.EAN:..................................")
          print("")
          break 
        else:
            print("ERROR, Opcion no valida para el cajero EAN ๐ โ")
            break
"""