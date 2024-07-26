def switch_case(validar):
    pedro = {
        1: "Seleccionaste la opción 1: Cocinar: Carne y ensalada",
        2: "Seleccionaste la opción 2: Jugar: Fútbol y natación",
        3: "Seleccionaste la opción 3: barrer y limpiar",
        4: "Seleccionaste Salir del programa",
}
    return pedro.get(validar, "opción no valida")
 
def main():
    print("Selecciona una opción: ")
    print("La opción 1 es: Cocinar ")
    print("La opción 2 es: Jugar ")
    print("La opción 3 es: Oficio ")
    print("Opción 4: Salir")
   
    try:
        opcion = int(input("Ingresa una opción entre (1-4): "))
        resul = switch_case(opcion)
        print(resul)
    except ValueError:
        print("Por favor, debes ingresar un número válido.")
main()
   


    