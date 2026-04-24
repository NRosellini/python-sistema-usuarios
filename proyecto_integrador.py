#Anexo con clase de profe que pide verificar ingreso a un sistema a traves de usuario y contraseña

#Definicion de variables/listas/diccionarios.
user = "admin"
password = "uni123"
nombre_curso_alumno = [[]]

#Solicitud de datos
usuario = input("Ingrese su nombre de usuario: ")
contraseña = input("Ingrese su contraseña: ")

#Acceso al sistema
while usuario == user and contraseña == password:       # Acceso permitido al sistema
    print("Acceso permitido")
    print("""Ingrese el número de la operación que desea ejecutar:
          1 - Añadir un alumno a la lista.
          2 - Ver la lista de alumnos.
          3 - Salir.""")                                # Mostrando menu
    opcion = int(input("Ingrese una opcion: "))         # Solicitar opcion
    if opcion == 1:                                     # Opcion 1: solicitar nombre y cantidad de cursos, guardarlos en una lista y avisar al usuario que fue guardado.
        nombre_alumno = input("Ingrese el nombre del alumno: ")
        cantidad_cursos_alumno = int(input("Ingrese la cantidad de cursos: "))
        nombre_curso_alumno.append([f"{nombre_alumno} - {cantidad_cursos_alumno}"])
        print("El alumno y sus cursos fueron agregados a la lista!")
    elif opcion == 2:                                   # Opcion 2: Mostrar un listado con el nombre y cantidad de cursos de los alumnos
        if nombre_curso_alumno == "":
            for mostrar_nombres in nombre_curso_alumno:
                print(f"""Lista de alumnos:
                    {mostrar_nombres} cursos""")
        else:
            print("No hay alumnos en la lista.")        # En caso de que la lista este vacia.
    elif opcion != 3:                                   # Solicitando nuevamente la opcion en caso de que el usuario ponga un N distinto del 1 al 3.
        print(f"Opcion incorrecta")
        print(opcion)
    else:                                               # Opcion 3: salir del programa y agradecer en pantalla.
        print("Gracias por utilizar el programa!")
        break
else:                                                   # Acceso denegado al sistema
    print("Acceso denegado")