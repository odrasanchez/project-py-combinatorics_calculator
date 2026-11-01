# Calculadora: Combinaciones y permutaciones

> Calculadora desarrollada en Python para realizar operaciones de análisis combinatorio. Implementa el cálculo de combinaciones ordinarias, permutaciones sin repetición y operaciones con repetición, mediante fórmulas matemáticas utilizadas en el ámbito académico.
> 
> El proyecto cuenta con dos versiones que permiten abordar diferentes problemas de análisis combinatorio mediante una interfaz de consola.
>
> Características:
> - Menú interactivo para seleccionar las operaciones.
> - Cálculo de combinaciones y permutaciones mediante fórmulas matemáticas.
> - Validación de datos de entrada.
> - Separación de operaciones mediante funciones.
> - Uso de librerías estándar de Python para operaciones factoriales.
> - Generación de secuencias con repetición en la versión que utiliza cadenas.


## Estado del repositorio 📊️
<div align="center" style="display: inline_block">
<img src="https://img.shields.io/badge/Dificultad-Principiante-071739?style=for-the-badge" />
<img src="https://img.shields.io/badge/Estado-Completado-071739?style=for-the-badge" />
<img src="https://img.shields.io/badge/Mantenimiento-Limitado%20a%20soporte-E3C39D?style=for-the-badge" />
</div>
<br>
<br>


## Tecnologías utilizadas 🔨
<div align="center" style="display: inline_block">
<img alt="Spyder Code" src="https://img.shields.io/badge/spyder-FF0000?style=for-the-badge" />
<img alt="Python" src="https://img.shields.io/badge/Python-14354C?style=for-the-badge" />
</div>
<br>


### Notas importantes ⚠
- Las operaciones cuentan con restricciones de datos basadas en las condiciones de sus respectivas fórmulas matemáticas.
- El idioma del contenido de los archivos y comentarios es Español (MX).
- No requiere instalaciones adicionales de librerías externas. Se utilizan módulos incluidos en la biblioteca estándar de Python.
- Los programas están desarrollados con fines académicos y de práctica.

<br>

## 1. 📙 Calculadora con uso de cadena

Esta versión permite realizar operaciones de análisis combinatorio mediante un menú interactivo en consola.

### Operaciones disponibles

**Caso 1. Combinación ordinaria**

Calcula las formas posibles de seleccionar una cantidad determinada de elementos de un conjunto, sin considerar el orden y sin permitir repeticiones.

\[
C(n,m)=\frac{n!}{m!(n-m)!}
\]

Requiere dos valores:
- `n`: cantidad total de elementos.
- `m`: cantidad de elementos seleccionados.

<br>

**Caso 2. Permutación sin repetición**

Calcula las formas posibles de ordenar una cantidad determinada de elementos, considerando el orden y sin permitir repeticiones.

\[
P(n,k)=\frac{n!}{(n-k)!}
\]

Requiere dos valores:
- `n`: cantidad total de elementos.
- `k`: cantidad de elementos seleccionados.

<br>

**Caso 3. Variaciones con repetición**

Genera todas las secuencias posibles a partir de una cadena de caracteres, permitiendo repetir sus elementos.

\[
VR(n,r)=n^r
\]

Requiere dos valores:
- `cadena`: conjunto de caracteres que se utilizarán.
- `r`: longitud de las secuencias generadas.

Ejemplo de ejecución:

```text
Bienvenido, seleccione la operación a trabajar:

1. Combinación ordinaria
2. Permutación sin repetición
3. Permutación con repetición

Seleccione una opción: 3

Ingrese el valor de repetición: 2
Ingrese la cadena a utilizar: abc

Cantidad de permutaciones: 9

[('a', 'a'), ('a', 'b'), ('a', 'c'),
 ('b', 'a'), ('b', 'b'), ('b', 'c'),
 ('c', 'a'), ('c', 'b'), ('c', 'c')]
```

<br>
<br>

## 2. 📗 Calculadora simple

Esta versión implementa las operaciones de análisis combinatorio mediante funciones independientes, utilizando fórmulas matemáticas y la librería `math` de Python.

### Operaciones disponibles

**Caso 1. Combinación ordinaria**

Calcula las formas posibles de seleccionar elementos de un conjunto sin considerar el orden y sin repetir elementos.

\[
C(n,m)=\frac{n!}{m!(n-m)!}
\]

Requiere:
- `n`: cantidad total de elementos.
- `m`: cantidad de elementos seleccionados.

<br>

**Caso 2. Permutación sin repetición**

Calcula las formas posibles de ordenar elementos de un conjunto sin repetirlos.

\[
P(n,k)=\frac{n!}{(n-k)!}
\]

Requiere:
- `n`: cantidad total de elementos.
- `k`: cantidad de elementos seleccionados.

<br>

**Caso 3. Permutación con repetición**

Calcula las formas posibles de ordenar un conjunto de elementos que contiene grupos de elementos repetidos.

\[
PR=\frac{n!}{n_1!\cdot n_2!\cdots n_r!}
\]

Requiere:
- `n`: cantidad total de elementos.
- `r`: cantidad de grupos de elementos repetidos.
- `n₁, n₂, ..., nᵣ`: cantidad de elementos pertenecientes a cada grupo.

Ejemplo de ejecución:

```text
Bienvenido, seleccione la operación a trabajar:

1. Combinación ordinaria
2. Permutación sin repetición
3. Permutación con repetición

Seleccione una opción: 3

Ingrese el valor total de elementos: 5
Ingrese el número de grupos: 3

Ingrese la cantidad de elementos del grupo 1: 2
Ingrese la cantidad de elementos del grupo 2: 2
Ingrese la cantidad de elementos del grupo 3: 1

5! / (2! * 2! * 1!) = 30
```
<br>

## Ejecución del proyecto 🚀

1. Clonar el repositorio:

```bash
git clone https://github.com/0draS0/PY-CalcuCombinaciones.git
```

2. Ingresar al directorio de la versión que se desea utilizar.

3. Ejecutar el archivo principal:

```bash
python main.py
```

Se requiere tener Python instalado en el equipo.

<br>

## Licencia ✅

Proyecto desarrollado con fines académicos como práctica de programación en Python y aplicación de conceptos matemáticos de análisis combinatorio.

El repositorio reúne diferentes implementaciones de una misma temática, permitiendo observar distintas formas de resolver problemas mediante funciones, ciclos, condicionales y librerías estándar.

Proyecto de carácter académico y educativo.

Copyright (c) 2026 at Odra Sanchez. Enlace del perfil:
<div align="center" style="display: inline_block">
  
<a href="https://github.com/odrasanchez">![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)</a>
</div>
<br>


## Contacto 🌐
Si tienes alguna pregunta o sugerencia, no dudes en contactarme:
<div align="center" style="display: inline_block;">
  
 <a href="https://www.linkedin.com/in/odrasanchez/">![LinkedIn](https://img.shields.io/badge/-LinkedIn-004e89?style=for-the-badge)</a>
 <a href="https://odrasanchezdev.netlify.app/links/index.html">![LinkTree](https://img.shields.io/badge/LinkTree-071739?style=for-the-badge)</a>
 <a href="https://www.instagram.com/odrasanchezdev/">![Instagram](https://img.shields.io/badge/-Instagram-9f175b?style=for-the-badge)</a>
 <a href="https://ko-fi.com/odrasanchez">![Ko-fi](https://img.shields.io/badge/-Ko--fi-f45b69?style=for-the-badge)</a>
 
</div>
