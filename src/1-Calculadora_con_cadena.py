
# Librerías utilizadas
import math
from itertools import product


# Función principal: solicita los datos y controla el flujo del programa
def main():
    print("""
    BIENVENIDO AL PROGRAMA DE ANÁLISIS COMBINATORIO

    Seleccione la operación que desea realizar:
    1. Combinación ordinaria
    2. Permutación sin repetición
    3. Permutación con repetición
    """)

    try:
        option = int(input("Seleccione una opción: "))

        if option == 1:
            n = int(input("Ingrese el valor de n: "))
            m = int(input("Ingrese el valor de m: "))

            # Validación de los valores de entrada
            if n < 0 or m < 0 or m > n:
                print("Error: los valores deben cumplir 0 <= m <= n.")
                return

            operations_comb(n, m)



        elif option == 2:
            n = int(input("Ingrese el valor de n: "))
            k = int(input("Ingrese el valor de k: "))

            # Validación de los valores de entrada
            if n < 0 or k < 0 or k > n:
                print("Error: los valores deben cumplir 0 <= k <= n.")
                return

            operations_permu(n, k)



        elif option == 3:
            r = int(input("Ingrese el número de repeticiones: "))
            cadena = input("Ingrese la cadena a utilizar, sin espacios ni comas: ")

            # Validación de los valores de entrada
            if r <= 0 or not cadena:
                print("Error: la cadena y el número de repeticiones deben ser válidos.")
                return

            operations_permuPR(cadena, r)



        else:
            print("Error: la opción seleccionada no es válida.")

    except ValueError:
        print("Error: debe ingresar un valor numérico válido.")




# Formato de presentación para combinacoptiones
def final_format(n, m, result):
    print(f"""
        {n}!
    {n}C{m} = ------------------ = {result}
        {m}! ({n} - {m})!
    """)


# Formato de presentación para permutaciones sin repetición
def format_permut(n, k, result):
    print(f"""
        {n}!
    P = ------------------ = {result}
        ({n} - {k})!
    """)




# Cálculo de combinaciones ordinarias
def operations_comb(n, m):
    # Cálculo de factoriales utilizando la librería math
    n_factorial = math.factorial(n)
    m_factorial = math.factorial(m)
    n_m_factorial = math.factorial(n - m)

    # Aplicación de la fórmula de combinación
    result = n_factorial / (m_factorial * n_m_factorial)

    # Presentación del resultado
    final_format(n, m, result)


# Cálculo de permutaciones sin repetición
def operations_permu(n, k):
    # Aplicación de la fórmula de permutación
    result = math.factorial(n) // math.factorial(n - k)

    # Presentación del resultado
    format_permut(n, k, result)


# Generación de permutaciones con repetición
def operations_permuPR(cadena, r):
    caracteres = list(cadena)

    # Generación de todas las secuencias posibles
    permutations = list(product(caracteres, repeat=r))

    print(f"Cantidad de permutaciones: {len(permutations)}")
    print(permutations)


# Punto de entrada del programa
if __name__ == "__main__":
    main()
