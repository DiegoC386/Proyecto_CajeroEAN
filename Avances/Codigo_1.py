usuario="DIEGO"
passw="1234"
saldo=500000
saldo2=100000
cont=0
conectado=bool;
while cont<3:
    us=input("Ingrese usuario: ");
    co=input("Ingrese contraseña: ");
    if us==usuario and passw==co:
        print ("Bienvenido al sistema")
        conectado=True
    else:
        cont=cont+1;
        print ("Usuario y contraseña incorrecta")
        conectado=False
        break
while conectado==True:
    print ("Que operacion desea utilizar?: ")
    print ("1.- Retirar")
    print ("2.- Deposito")
    print ("3.- Traspaso")
    print ("4.- Consulta Saldo")
    print ("0.- Para cerrar")
    OP=int(input("Ingrese opcion:"))
    if OP==1:
        monto=int(input("Ingrese monto a Retirar:"))    
        saldo=saldo-monto
        print ("Ha retirado " , monto)
    elif OP==2:
        monto=int(input("Ingrese monto a Depositar:"))          
        saldo=saldo+monto
        print ("Su nuevo saldo es", saldo)
    elif OP==3:
        cu2=input("Ingrese cuenta a depositar")    
        monto=int(input("Ingrese monto a Transferir:"))
        saldo=saldo-monto
        saldo2=saldo2+monto
        print ("Se han transferido", monto,"pesos a la cuenta",cu2)
        print ("El nuevo saldo es:",saldo2)
    elif OP==4:
        print ("Su saldo es:", saldo)
    elif OP==0:
        break
   "Esto es una mierda"
"Esto es una mierda"
