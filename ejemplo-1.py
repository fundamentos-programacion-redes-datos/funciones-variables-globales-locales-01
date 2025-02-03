"""


"""
# Variable global declarada fuera de cualquier función
frase = "Ecuador país de Sudamérica"  # Variable global

def presentar_mensaje():
    """
    Función que define una variable local con el mismo nombre que la global.
    Esta variable local solo existe dentro de la función.
    """
    # Se define una variable local con el mismo nombre que la global
    frase = "Ecuador país con cuatro regiones naturales"  # Variable local
    print(frase)  # Imprime la variable local dentro de la función

# Punto de entrada principal del script
if __name__ == "__main__":
    
    # Se imprime la variable global
    print(frase)  # Salida: "Ecuador país de Sudamérica"
    
    # Se llama a la función que tiene una variable local con el mismo nombre
    presentar_mensaje()  # Salida: "Ecuador país con cuatro regiones naturales"
    
    # Se vuelve a imprimir la variable global, su valor no ha cambiado
    print(frase)  # Salida: "Ecuador país de Sudamérica"

