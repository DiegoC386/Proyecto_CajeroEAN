
usuario=["DIEGO","nada"]
passw=["1234","222"]
ingreso = False
saldo=500000
saldo2=100000
ua=1
iniciar = True
def validarUsuario(usuario, clave) :
   global ingreso
   if (usuario == usuario and clave == passw ) :
     ingreso = True
     return True
   return False
def login() :
   global ingreso
   if (ingreso) :
     return True
   usuario = input("Ingrese usuario 🙍 : ")
   clave = input("Ingrese contraseña 🔑 : ")
   return validarUsuario(usuario, clave)
def retirar(valor) :
   global saldo
   if (valor > saldo) :
     return False, saldo
   saldo = saldo - valor
   return True, saldo
def transferir (valor) :
   global saldo
   saldo = saldo - valor
   return True, saldo
def consultarSaldo() :
   return True, saldo
def accion(opcion) :
   if (opcion == 1) :
     valor = int(input("Digite el valor a transferir: "))
     ua = int(input("ingrese usuario a transferir DINERO: "))
     return transferir(valor)
   if (opcion == 2) :
     valor = int(input("Digite el valor a retirar 🔚: "))
     cant500 = valor // 50000
     resto500 = valor % 50000 
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
     print(" billetes de 500  a salir 💸: ", cant500)
     print(" billetes de 200 a salir 💸: ", cant200)
     print(" billetes de 100 a salir 💸: ", cant100)
     print(" billetes de 50 a salir 💸: ", cant50)
     print(" billetes de 20 a salir💸: ", cant20)
     print(" billetes de 10 a salir💸: ", cant10)
     return retirar(valor)
   if (opcion == 3) :
     return consultarSaldo() 
   return False, saldo
def ejecutar() :
   if not login() :
     print("usuario o contraseña inválido 🛑 ❌")
     return 
   print("......................................:CAJERO.EAN:..................................")
   print("\t.:MENU:.")
   print("")
   print("1. transferir💸")
   print("2. Retirar dinero 💵")
   print("3. Consultar saldo 🔍")
   print("......................................:CAJERO.EAN:..................................")
   opcion=int(input("Digite una opcion de MENU: "))
   print("")
   ok, saldo = accion(opcion)
   if not ok :
     print("No se realizó la acción, saldo:", saldo)
   else:
     print("Acción realizada correctamente, saldo:", saldo)
from datetime import datetime
ahora=datetime.now()
print(ahora.strftime('%Y-%m-%d %H:%M:%S'))
Cuentas=[]
print("......................................:CAJERO.EAN:..................................")
print("Bienvenido al sistema 💰")
print("......................................:CAJERO.EAN:..................................")
while (iniciar == True) :
  while (iniciar == True) :
   ejecutar()
   print("......................................:CAJERO.EAN:..................................")
   respuesta = input("¿Deseas realizar otra operación? dijite 1. si ✔ o dijite 2. No ❌ : ")
   if (respuesta == "1" ) :
     iniciar = True
   else:
     iniciar = False
     print("Gracias por usar el Cajero EAN 🙌...")
