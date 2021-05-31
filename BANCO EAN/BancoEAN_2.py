usuario="DIEGO"
passw="1234"
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