# Optimizador de Producción con Django y Docker

Esta demo permite cargar un archivo .csv con parámetros de producción de dos productos para dos máquinas.
Se resuelve el problema de optimización lineal para maximizar los ingresos.

Se construyó utilizando Django como backend y para la resolución del problema se utiliza `PuLP`.

# Requisitos

1. Docker
2. Docker-compose

# Instalación

1. Clona el repositorio

```
git clone https://github.com/pablosbw/demo-opt-lineal.git
```

2. Ingresa a la carpeta

```
cd demo-opt-lineal
```

3. Levanta el entorno

```
docker-compose up --build
```

4. Accede a través de `http://localhost:8000/upload/`

# Estructura del archivo esperada

Archivo `.csv` con una sola fila, con las siguientes columnas:

- Product_A_Production_Time_Machine_1
- Product_A_Production_Time_Machine_2
- Product_B_Production_Time_Machine_1
- Product_B_Production_Time_Machine_2
- Machine_1_Available_Hours
- Machine_2_Available_Hours
- Price_Product_A
- Price_Product_B

Todos los valores del archivo deben ser numéricos positivos y no nulos.

## Otros inputs

También existen 2 parámetros opcionales, correspondientes a un máximo de capacidad a producir de cada tipo de unidad.
Este valor debe ser numérico no negativo en caso de existir.
