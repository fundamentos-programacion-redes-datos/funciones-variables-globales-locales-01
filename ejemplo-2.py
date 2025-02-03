"""


"""
# Variable global declarada fuera de cualquier función
frase = "Ecuador país de Sudamérica"  # Variable global

def presentar_mensaje():
    """
    Función que imprime el valor de la variable global 'frase'.
    Como no se define una variable local con el mismo nombre dentro de la función,
    Python automáticamente usa la variable global.
    """
    print(frase)  # Se accede y muestra el valor de la variable global

# Punto de entrada principal del script
if __name__ == "__main__":
    
    # Se imprime la variable global antes de llamar a la función
    print(frase)  # Salida: "Ecuador país de Sudamérica"
    
    # Se invoca la función, que imprimirá la variable global
    presentar_mensaje()  # Salida: "Ecuador país de Sudamérica"
    
    # Se vuelve a imprimir la variable global, sin haber sido modificada
    print(frase)  # Salida: "Ecuador país de Sudamérica"
