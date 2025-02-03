"""


"""
# Variable global declarada fuera de cualquier función
frase = "Ecuador país de Sudamérica"  # Variable global

def presentar_mensaje():
    """
    Función que modifica la variable global 'frase'.
    Para cambiar su valor dentro de la función, se usa la palabra clave 'global',
    lo que permite modificar la variable global en lugar de crear una nueva variable local.
    """
    global frase  # Se indica que se trabajará con la variable global
    frase = "Ecuador país donde el mundo se une en un solo paisaje"  # Se modifica la variable global
    print(frase)  # Se imprime el nuevo valor de la variable global

# Punto de entrada principal del script
if __name__ == "__main__":
    
    # Se imprime la variable global antes de llamar a la función
    print(frase)  # Salida: "Ecuador país de Sudamérica"
    
    # Se invoca la función, que modificará la variable global
    presentar_mensaje()  # Salida: "Ecuador país donde el mundo se une en un solo paisaje"
    
    # Se vuelve a imprimir la variable global, que ahora ha cambiado su valor
    print(frase)  # Salida: "Ecuador país donde el mundo se une en un solo paisaje"
