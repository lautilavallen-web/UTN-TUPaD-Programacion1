#Ejercicio 1
#Solicito el nombre del cliente
nombre = input("Cliente nombre: ").strip()

#Valido que se ingrese un nombre y que solo contenga letras
while nombre == "" or not nombre.isalpha():
    print("Error. Por favor ingrese un nombre en letras y sin vacios")
    nombre = input("Cliente nombre: ").strip()

#Defino una variable para la cantidad de productos
cant_str = input("Ingresa cantidad de productos: ").strip()

#Valido que el usuario ingrese un entero mayor a cero
while not cant_str.isdigit() or int(cant_str) <= 0:
    print("Error. Por favor ingrese un número entero mayor a 0")
    cant_str = input("Ingresa cantidad de productos: ").strip()

#Paso a número el string de la variable
cant_int = int(cant_str)

#Solicito el precio del producto
for i in range (1, cant_int+1):
    precio_str = input(f"Producto {i}  - Precio: $").strip()
    

#Valido la condición del precio como número entero mayor a cero
    while not precio_str.isdigit() or int(precio_str) <=0:
        print("Error. Por favor ingrese un número entero mayor a 0")
        precio_str = input(f"Producto {i}  - Precio: $ ").strip()

#Convierto el string en número
    precio_int = int(precio_str)

#Defino variables descuento
    total_sindesc = 0
    total_condesc = 0

    desc = input("Tiene descuento? Responda S/N: ").strip().lower()

#Valido que solo se pueda contestar S/N
    while desc != "s" and desc != "n":
        print("Error. Por favor conteste S para si o N para no")
        desc = input("Tiene descuento? Responda S/N: ").strip().lower()

    total_sindesc = precio_int

#Calculo el precio con descuento    
    if desc == "s":
        precio_final = precio_int * 0.9
    else:
        precio_final = precio_int

    total_condesc += precio_final

ahorro = total_sindesc - total_condesc
promedio = total_condesc / cant_int

print()
print(f"Total sin descuento: ${total_sindesc:.2f}")
print(f"Total con descuento: ${total_condesc:.2f}")
print(f"Ahorro total: ${ahorro:.2f}")
print(f"Promedio: {promedio:.2f}")


#------------------------------------
#Ejercicio 2
#Defino valores para las variables
usuario_correcto = "alumno"
clave_correcta = "python123"
intentos = 0
max_intentos = 3

#Solicito datos para el ingreso utilizando el contador de intentos
while intentos < max_intentos:
    usuario = input("Ingrese usuario: ").strip().lower()
    clave = input("Ingrese clave: ").strip()

#Fijo la condición que las variables sean true
    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido")

        #Si se ingresan bien los datos, se pasa al menú
        while True:
            print("")
            print("1) Estado")
            print("2) Cambiar clave")
            print("3) Mensaje")
            print("4) Salir")

            opcion = input("Opción: ")

            #Valido que sea número
            if not opcion.isdigit():
                print("Error: ingrese un número válido.")
                continue

            opcion = int(opcion)

            # Valido que elija dentro del rango
            if opcion < 1 or opcion > 4:
                print("Error: opción fuera de rango.")
                continue

            #Opciones del menú
            if opcion == 1:
                print("Estado: Inscripto")

            elif opcion == 2:
                nueva_clave = input("Ingrese nueva clave: ")
                confirmar = input("Confirme nueva clave: ")

                #Si elige esta opción valido el valor de la nueva clave
                if len(nueva_clave) < 6:
                    print("Error: la clave debe tener al menos 6 caracteres")
                elif nueva_clave != confirmar:
                    print("Error: las claves no coinciden")
                else:
                    clave_correcta = nueva_clave
                    print("Clave cambiada con éxito")

            elif opcion == 3:
                print("¡Vamos que ya queda menos!")

            elif opcion == 4:
                print("Ha salido del sistema.")
                break #Para salir del sistema

        break #Para salir del login

#Si no se cumplen las condiciones de ingreso, muestro la cantidad de intentos
#Vuelvo a solicitar los valores
    else:
        intentos += 1
        restantes = max_intentos - intentos

        if restantes > 0:
            print(f"Incorrecto, le quedan {restantes} intentos")
        else:
            print("Cuenta bloqueada") #se cumplieron la cantidad de intentos


#-----------------------------------------------
#Ejercicio 3
#Solicito nombre y defino la condición de solo letras
operador = input("Indique su nombre: ").strip()

while not operador.isalpha():
    print("Error. Ingrese solo letras: ")
    operador = input("Ingrese su nombre: ").strip()

lunes1 = lunes2 = lunes3 = lunes4 = ""
martes1 = martes2 = martes3 = ""
opción = ""

#Se despliega el menú para el usuario y valido que solo pueda poner un número
while opción != "5":
    print("\n MENÚ: ")
    print("1- Reservar turno")
    print("2- Cancelar turno")
    print("3- Ver agenda del día")
    print("4- Ver resumen general")
    print("5- Cerrar sistema")

#Valido que la opción ingresada sea válida
    opción = input("Opción: ").strip()
    while not opción.isdigit() or int(opción) < 1 or int(opción) > 5:
        opción = input("Error. Ingrese una opción del 1 al 5: ")

#Defino variables para la opción 1
    if opción == "1":
        dia = input("Ingrese 1 para Lunes, 2 para Martes: ").strip()
        while dia not in ["1", "2"]:
            dia = input("Error, indique 1 para Lunes o 2 para Martes").strip()

        nombre = input("Indique su nombre: ").strip()
        while not nombre.isalpha():
            nombre = input("Error. Ingrese solo letras: ").strip()

#Asigno los turnos según el día elegido
        asignado = False #bandera para agregar un mensaje de turno asignado
        if dia == "1": #día lunes
            if nombre in (lunes1, lunes2, lunes3, lunes4):
                    print("El paciente ya tiene turno ese día.")
            elif lunes1 == "":
                    lunes1 = nombre
                    asignado = True
            elif lunes2 == "":
                    lunes2 = nombre
                    asignado = True
            elif lunes3 == "":
                    lunes3 = nombre
                    asignado = True
            elif lunes4 == "":
                    lunes4 = nombre
                    asignado = True
            else:
                    print("No hay turnos disponibles.")
   
        else: #día martes
            if nombre in (martes1, martes2, martes3):
                    print("El paciente ya tiene turno ese día.")
            elif martes1 == "":
                    martes1 = nombre
                    asignado = True
            elif martes2 == "":
                    martes2 = nombre
                    asignado = True
            elif martes3 == "":
                    martes3 = nombre
                    asignado = True
            else:
                    print("No hay turnos disponibles.")
  
        if asignado: #Mensaje agregado
                    print("Turno asignado correctamente.")
    #Opción para cancelar turnos
    elif opción == "2": #valido que pueda ingresar 1 o 2
        dia = input("Ingrese 1 para Lunes, 2 para Martes: ").strip()
        while dia not in ["1", "2"]:
            dia = input("Error. Indique 1 para Lunes o 2 para Martes: ").strip()
        
        #valido que solo pueda ingresar letras
        nombre = input("Nombre: ").strip()
        while not nombre.isalpha():
            nombre = input("Error. Ingrese solo letras: ").strip()
        #Asignación del día
        cancelado = False #bandera para mensaje de cancelación
        if dia == "1": #dia lunes
            if lunes1 == nombre:
                lunes1 = ""
                cancelado = True
            elif lunes2 == nombre:
                lunes2 = ""
                cancelado = True
            elif lunes3 == nombre:
                lunes3 = ""
                cancelado = True
            elif lunes4 == nombre:
                lunes4 = ""
                cancelado = True
        
        else: #dia martes
            if martes1 == nombre:
                martes1 = ""
                cancelado = True
            elif martes2 == nombre:
                martes2 = ""
                cancelado = True
            elif martes3 == nombre:
                martes3 = ""
                cancelado = True
    
        if not cancelado:
             print("Nombre no encontrado.")
        else:
             print("Turno cancelado.")
    
    #Opción de ver agenda
    elif opción == "3": #valido que solo pueda ingresar 1 o 2
        dia = input("Ingrese 1 para Lunes, 2 para Martes: ").strip()
        while dia not in ["1", "2"]:
            dia = input("Error. Indique 1 para Lunes o 2 para Martes: ").strip()

        #Muestro la agenda con el nombre del turno ocupado, sino que se encuentra "Libre"
        if dia == "1":
            print("Lunes: ")
            print("1:", lunes1 if lunes1 else "(Libre)")
            print("2:", lunes2 if lunes2 else "(Libre)")
            print("3:", lunes3 if lunes3 else "(Libre)")
            print("4:", lunes4 if lunes4 else "(Libre)")
        else:
            print("Martes: ")
            print("1:", martes1 if martes1 else "(Libre)")
            print("2:", martes2 if martes2 else "(Libre)")
            print("3:", martes3 if martes3 else "(Libre)")

    #Promedio de ocupación de turnos
    elif opción == "4":
        ocup_lunes = (lunes1 != "") + (lunes2 != "") + (lunes3 != "") + (lunes4 != "")
        ocup_martes = (martes1 != "") + (martes2 != "") + (martes3 != "")

        print("Lunes:", ocup_lunes, "ocupados,", 4 - ocup_lunes, "libres")
        print("Martes:", ocup_martes, "ocupados,", 3 - ocup_martes, "libres")

        if ocup_lunes > ocup_martes:
            print("Más turnos: Lunes")
        elif ocup_martes > ocup_lunes:
            print("Más turnos: Martes")
        else:
            print("Igual cantidad.")

    #Opción de cerrar el sistema
    elif opción == "5":
        print("Cerrando sistema.")



#--------------------------
#Ejercicio 4
#Definición de variables
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

#condición antispam
racha_forzar = 0

#solicitud del nombre
agente = input("Nombre del agente: ").strip()

while not agente.isalpha():
    agente = input("Error. Ingrese solo letras: ").strip()

#Comienzo del juego
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

    #Bloquear por alarma
    if alarma and tiempo <= 3:
        print("DERROTA (bloqueo)")
        break

    print("\n--- ESTADO ---")
    print("Energía:", energia)
    print("Tiempo:", tiempo)
    print("Cerraduras abiertas:", cerraduras_abiertas)
    print("Alarma:", alarma)

    print("\n1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    #solicito opción y valido que sea del 1 al 3
    opcion = input("Opción: ")

    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        opcion = input("Error. Indique una opción válida: ")

    #opción 1
    if opcion == "1":
        energia -= 20
        tiempo -= 2
        racha_forzar += 1

        # regla anti-spam
        if racha_forzar == 3:
            alarma = True
            print("¡La cerradura se trabó! Alarma activada.")
            continue

        #riesgo de alarma
        if energia < 40:
            num = input("Riesgo! Elija número (1-3): ")
            while not num.isdigit() or int(num) < 1 or int(num) > 3:
                num = input("Error. Elija un número del 1 al 3: ")

            if num == "3":
                alarma = True
                print("Se activó la alarma!")

        #abrir cerradura
        if not alarma:
            cerraduras_abiertas += 1
            print("Cerradura abierta!")

    #Opción 2
    elif opcion == "2":
        energia -= 10
        tiempo -= 3
        racha_forzar = 0  #corta la racha

        print("Hackeando")

        for i in range(4):
            codigo_parcial += "A"
            print("Progreso:", codigo_parcial)

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            codigo_parcial = ""
            print("Cerradura abierta por hackeo")

    # opcion 3
    elif opcion == "3":
        tiempo -= 1
        energia += 15

        if energia > 100:
            energia = 100

        if alarma:
            energia -= 10
        #para cortar racha
        racha_forzar = 0 

        print("Descansaste.")

#Resultados
if cerraduras_abiertas == 3:
    print("VICTORIA. ¡Abriste la bóveda!")
elif energia <= 0 or tiempo <= 0:
    print("DERROTA. Te quedaste sin recursos.")



#-------------------------------------
#Ejercicio 5
#Solicito nombre y valido que tenga solo letras
print("\n--- BIENVENIDO A LA ARENA ---")
nombre = input("\nNombre del Gladiador: ").strip()

while not nombre.isalpha():
    nombre = input("Error: Solo se permiten letras. ").strip()

#Defino las variables del juego
vida_jugador = 100
vida_enemigo = 100
pociones = 3
danio_jugador = 15
danio_enemigo = 12

print("\n === INICIO DEL COMBATE ===")
#defino condición base ganar/perder
while vida_jugador > 0 and vida_enemigo > 0:
    #mensaje con hp
    print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    
    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    opcion = input("Opción: ")
    #condicional opción del 1 al 3
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("Error: Ingrese un número válido.")
        opcion = input("Opción: ")

    #para ataque pesado (sin uso de ñ)
    if opcion == "1":
        if vida_enemigo < 20:
            danio = int(danio_jugador * 1.5)  #para evitar decimales
        else:
            danio = danio_jugador

        vida_enemigo -= danio
        print(f"¡Atacaste al enemigo por {danio} puntos de daño!")

    #para ráfaga veloz
    elif opcion == "2":
        print(">> ¡Inicias una ráfaga de golpes!")
        for i in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")

    #para curar
    elif opcion == "3":
        if pociones > 0:
            vida_jugador = min(vida_jugador + 30, 100) #para no superar los 100 HP
            pociones -= 1
            print("Te curaste 30 puntos de vida")
        else:
            print("¡No quedan pociones!")

    #ataque enemigo
    if vida_enemigo > 0:
        vida_jugador -= danio_enemigo
        print(f">> ¡El enemigo contraataca por {danio_enemigo} puntos!")
    #Mensaje de turno
    if vida_jugador > 0 and vida_enemigo > 0:
        print("=== NUEVO TURNO ===")

#resultado
if vida_jugador > 0:
    print(f"\n¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("\nDERROTA. Has caído en combate.")