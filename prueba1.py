parte 1
print("Evaluación N°1 Redes Avanzadas I")
print("Integrantes:")
print("Samuel Lugo")
print("Jonathan Leiva")
print()
print()
#parte 2
while True:
    # Solicitamos la información al usuario
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    codigo_seccion = input("Ingrese su código de sección: ")
    sede = input("Ingrese su sede: ")

    # Mostramos la información en pantalla con subtítulos
    print("La información ingresada es la siguiente:")
    print("----------------------------------------")
    print("Nombre: " + nombre)
    print("Apellido: " + apellido)
    print("Código de sección: " + codigo_seccion)
    print("Sede: " + sede)

    # Preguntamos si se desea ingresar nuevos datos o salir
    opcion = input("Presione cualquier tecla para ingresar nuevos datos, o escriba 'EXIT' para salir: ")
    if opcion.lower() == "exit":
        break

#parte 3
print()
print()
print()
while True:
    aclNum = input("Ingresa el número IPv4 ACL : ")
    try:
        if aclNum.lower() == 'exit':
            break
        aclNum = int(aclNum)
        if aclNum >= 1 and aclNum <= 99:
            print(f"El ACL {aclNum} es un ACL IPv4 estándar.")
        elif aclNum >=100 and aclNum <= 199:
            print(f"El ACL {aclNum} es una ACL IPv4 extendida.")
        else:
            print(f"El valor {aclNum} no es un número válido de ACL IPv4.")
    except ValueError:
        print("El valor ingresado no es un número válido.")

    confirmacion = input("Escribe 'exit' para salir, o cualquier otra cosa para continuar: ")
    if confirmacion.lower() == 'exit':
        break
