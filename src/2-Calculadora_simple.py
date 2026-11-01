
# Librerías utilizadas
import math


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
            n = int(input("Ingrese el valor total de elementos: "))
            r = int(input("Ingrese el número de grupos: "))

            # Validación de los valores de entrada
            if n < 0 or r <= 0:
                print("Error: los valores deben ser válidos.")
                return

            operations_permuPR(n, r)

        else:
            print("Error: la opción seleccionada no es válida.")

    except ValueError:
        print("Error: debe ingresar un valor numérico válido.")






# Formato de presentación para combinaciones
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
    {n}P{k} = ------------------ = {result}
             ({n} - {k})!
    """)


# Formato de presentación para permutaciones con repetición
def format_permutR(n, denominator, result):
    print(f"""
             {n}!
    PR = ------------------ = {result}
             {denominator}
    """)





# Cálculo de combinaciones ordinarias
def operations_comb(n, m):
    # Cálculo de factoriales
    n_factorial = math.factorial(n)
    m_factorial = math.factorial(m)
    n_m_factorial = math.factorial(n - m)

    # Aplicación de la fórmula de combinación
    result = n_factorial // (m_factorial * n_m_factorial)

    # Presentación del resultado
    final_format(n, m, result)





# Cálculo de permutaciones sin repetición
def operations_permu(n, k):
    # Aplicación de la fórmula de permutación
    result = math.factorial(n) // math.factorial(n - k)

    # Presentación del resultado
    format_permut(n, k, result)





# Cálculo de permutaciones con repetición
def operations_permuPR(n, r):
    denominator = 1
    total_elements = 0

    # Solicitud y cálculo de los factoriales de cada grupo
    for i in range(r):
        num = int(input(f"Ingrese la cantidad de elementos del grupo {i + 1}: "))

        if num < 0:
            print("Error: la cantidad de elementos no puede ser negativa.")
            return

        total_elements += num
        denominator *= math.factorial(num)

    # Validación de la cantidad total de elementos
    if total_elements != n:
        print("Error: la suma de los grupos debe ser igual a n.")
        return

    # Aplicación de la fórmula de permutación con repetición
    result = math.factorial(n) // denominator

    # Presentación del resultado
    format_permutR(n, denominator, result)


# Punto de entrada del programa
if __name__ == "__main__":
    main()
