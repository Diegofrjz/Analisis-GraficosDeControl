
from builtins import input

# Tiempo de la distribución del gráfico de control (La cantidad de columnas de los datos_desv)
while True:
    try:
        tiempo_gc = int(input("Ingrese la cantidad de puntos del Gráfico de control (Cantidad de columnas de los datos): "))
        break
    except ValueError:
        print("Tipo de valor incorrecto")
# El orden de la Array es el siguiente A2,A3,B3,B4
#Para el de rangos moviles falta E2
tab_tamaño_muestra_2 = [1.88, 2.659, 0, 3.267]
tab_tamaño_muestra_3 = [1.023, 1.954, 0, 2.568]
tab_tamaño_muestra_4 = [0.729, 1.628, 0, 2.266]
tab_tamaño_muestra_5 = [0.557, 1.427, 0, 2.089]
tab_tamaño_muestra_6 = [0.483, 1.287, 0.03, 1.97]
tab_tamaño_muestra_7 = [0.419, 1.182, 0.118, 1.882]
tab_tamaño_muestra_8 = [0.373, 1.099, 0.185, 1.815]
tab_tamaño_muestra_9 = [0.337, 1.032, 0.239, 1.761]
tab_tamaño_muestra_10 = [0.308, 0.975, 0.284, 1.716]
tab_tamaño_muestra_11 = [0.285, 0.927, 0.321, 1.679]
tab_tamaño_muestra_12 = [0.266, 0.886, 0.354, 1.646]
tab_tamaño_muestra_13 = [0.249, 0.85, 0.382, 1.618]
tab_tamaño_muestra_14 = [0.235, 0.817, 0.406, 1.594]
tab_tamaño_muestra_15 = [0.223, 0.789, 0.428, 1.572]
tab_tamaño_muestra_16 = [0.212, 0.763, 0.448, 1.552]
tab_tamaño_muestra_17 = [0.203, 0.739, 0.466, 1.534]
tab_tamaño_muestra_18 = [0.194, 0.718, 0.482, 1.518]
tab_tamaño_muestra_19 = [0.187, 0.698, 0.497, 1.503]
tab_tamaño_muestra_20 = [0.18, 0.68, 0.51, 1.49]
tab_tamaño_muestra_21 = [0.173, 0.663, 0.523, 1.477]
tab_tamaño_muestra_22 = [0.167, 0.647, 0.534, 1.466]
tab_tamaño_muestra_23 = [0.162, 0.633, 0.545, 1.455]
tab_tamaño_muestra_24 = [0.157, 0.619, 0.555, 1.445]
tab_tamaño_muestra_25 = [0.153, 0.606, 0.565, 1.435]

# Crea un diccionario que mapea el tamaño de muestra con el nombre de la array
diccionario_arrays = {
    2: tab_tamaño_muestra_2,
    3: tab_tamaño_muestra_3,
    4: tab_tamaño_muestra_4,
    5: tab_tamaño_muestra_5,
    6: tab_tamaño_muestra_6,
    7: tab_tamaño_muestra_7,
    8: tab_tamaño_muestra_8,
    9: tab_tamaño_muestra_9,
    10: tab_tamaño_muestra_10,
    11: tab_tamaño_muestra_11,
    12: tab_tamaño_muestra_12,
    13: tab_tamaño_muestra_13,
    14: tab_tamaño_muestra_14,
    15: tab_tamaño_muestra_15,
    16: tab_tamaño_muestra_16,
    17: tab_tamaño_muestra_17,
    18: tab_tamaño_muestra_18,
    19: tab_tamaño_muestra_19,
    20: tab_tamaño_muestra_20,
    21: tab_tamaño_muestra_21,
    22: tab_tamaño_muestra_22,
    23: tab_tamaño_muestra_23,
    24: tab_tamaño_muestra_24,
    25: tab_tamaño_muestra_25
}

# Solicita al usuario que ingrese el tamaño de muestra
while True:
    try:
        tamaño_muestra = int(input("Ingrese el tamaño de muestra (del 2 al 25): "))
        if 2 <= tamaño_muestra <= 25:
            break
        else:
            print("El tamaño de la muestra tiene que estar entre 2 y 25")
    except ValueError:
        print("El tamaño de la muestra tiene que estar entre 2 y 25")
# Verifica si el tamaño de muestra está en el diccionario
if tamaño_muestra in diccionario_arrays:
    # Accede a la array correspondiente usando el diccionario
    array_seleccionada = diccionario_arrays[tamaño_muestra]
# Ahora con la variable: "array_seleccionada" se pueden hacer operaciones

# CREAMOS LA ARRAY DATOS PARA LA DESVIACION ESTANDAR:
datos_desv = []

# El programa solicita los datos_desv de las desviaciones estandar al usuario
print("Introduce las desviaciones estandar, separados por espacios (Pega directo desde excel).")
datos_desv = input().split()

# Convierte los datos_desv en formato float
for i in range(len(datos_desv)):
    datos_desv[i] = float(datos_desv[i])

# CALCULAMOS EL sPROM:
sPromedio = sum(datos_desv) / len(datos_desv)

print("▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂")
# Imprimimos el promedio
print("El sProm es:", sPromedio)

# CÁLCULO DE LOS LIMITES DE CONTROL DE LAS DESVIACIONES ESTANDAR:
# usaremos "array_seleccionada" , para el calculo de los límites de control:
LCI_DESV = array_seleccionada[2]*sPromedio
if LCI_DESV < 0:
    LCI_DESV = 0

LCS_DESV = array_seleccionada[3]*sPromedio
if LCS_DESV < 0:
    LCS_DESV = 0

print("El límite de control superior para el G.C de Desv.Est es: ",LCS_DESV)
print("El límite de control inferior para el G.C de Desv.Est es: ",LCI_DESV)
print("▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂")

# 1.ÁLCULO DE RACHA POSITIVA:
print("ANALISIS DE RACHA:")
# Establecer la cantidad mínima de puntos consecutivos requeridos
min_puntos_consecutivos = 7

# Inicializar un contador para los puntos consecutivos
contador_consecutivo = 0
contador_consecutivin = 0

# Iterar sobre los datos_desv y contar los puntos consecutivos mayores que sProm
for punto in datos_desv:
    if punto > sPromedio:
        contador_consecutivo += 1
        if contador_consecutivo >= min_puntos_consecutivos:
            break
    else:
        contador_consecutivo = 0

# Verificar si se encontraron suficientes puntos consecutivos
if contador_consecutivo >= min_puntos_consecutivos:
    print(f"Se encontraron {min_puntos_consecutivos} o más puntos consecutivos mayores que sProm.")
else:
    print(f"No se encontraron {min_puntos_consecutivos} o más puntos consecutivos mayores que sProm.")

# 1.CÁLCULO DE RACHA NEGATIVA:
for puntito in datos_desv:
    if puntito < sPromedio:
        contador_consecutivin += 1
        if contador_consecutivin >= min_puntos_consecutivos:
            break
    else:
        contador_consecutivo = 0

# Verificar si se encontraron suficientes puntos consecutivos
if contador_consecutivo >= min_puntos_consecutivos:
    print(f"Se encontraron {min_puntos_consecutivos} o más puntos consecutivos menores que el sProm.")
else:
    print(f"No se encontraron {min_puntos_consecutivos} o más puntos consecutivos menores que sProm.")

print("▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂")
# 2.CÁLCULO DE LA TENDENCIA:
print("ANALISIS DE LA TENDENCIA:")
# Longitud de la secuencia que deseas encontrar (en este caso, 6 números consecutivos)
longitud_objetivo = 6

# Variables para contar la longitud de la secuencia actual
longitud_actual = 1

# Variable para almacenar el tipo de secuencia (ascendente, descendente o ninguna)
tipo_secuencia = None

# Recorremos la lista desde el segundo elemento en adelante
for i in range(1, len(datos_desv)):
    if datos_desv[i] > datos_desv[i - 1]:
        if tipo_secuencia == "ascendentes" or tipo_secuencia is None:
            longitud_actual += 1
            tipo_secuencia = "ascendentes"
        else:
            longitud_actual = 1
            tipo_secuencia = None
    elif datos_desv[i] < datos_desv[i - 1]:
        if tipo_secuencia == "descendentes" or tipo_secuencia is None:
            longitud_actual += 1
            tipo_secuencia = "descendentes"
        else:
            longitud_actual = 1
            tipo_secuencia = None
    else:
        longitud_actual = 1
        tipo_secuencia = None

    if longitud_actual == longitud_objetivo:
        break

# Verificamos si encontramos una secuencia de la longitud deseada
if longitud_actual == longitud_objetivo:
    print(f"Se encontró una secuencia de {longitud_objetivo} o más números {tipo_secuencia}.")
else:
    print(f"No se encontró una secuencia de {longitud_objetivo} números consecutivos ascendentes o descendentes.")

print("▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂")

# 4.CÁLCULO DE LOS PUNTOS FUERA DE LOS LÍMITES DE CONTROL:
print("ANALISIS DE PUNTOS FUERA DE LOS LÍMITES DE CONTROL:")
# LCS_DESV:
# Inicializar un contador para los puntos mayores que LCS_DESV
contador_mayores = 0

# Iterar sobre los datos_desv y contar los puntos mayores que LCS_DESV
for dato in datos_desv:
    if dato > LCS_DESV:
        contador_mayores += 1
        if contador_mayores >= 2:
            break

# Verificar si se encontraron 2 o más puntos mayores que LCS_DESV
if contador_mayores >= 2:
    print(f"Se encontraron 2 o más puntos mayores que LCS_DESV.")
else:
    print(f"No se encontraron 2 o más puntos mayores que LCS_DESV.")

# LCI_DESV:
# Inicializar un contador para los datos_desv menores que LCI_DESV
contador_menores = 0

# Iterar sobre los datos_desv y contar los datos_desv menores que LCI_DESV
for dato in datos_desv:
    if dato < LCI_DESV:
        contador_menores += 1
        if contador_menores >= 2:
            break

# Verificar si se encontraron 2 o más puntos menores que LCI_DESV
if contador_menores >= 2:
    print(f"Se encontraron 2 o más puntos menores que LCI_DESV.")
else:
    print(f"No se encontraron 2 o más puntos menores que LCI_DESV.")

print("▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂")

# CREAMOS LA ARRAY DATOS PARA LAS MEDIAS:
datos_medias = []

# El programa solicita los datos de las medias al usuario
print("Introduce las medias, separados por espacios (Pega directo desde excel).")
datos_medias = input().split()

# Convierte los datos en formato float
for i in range(len(datos_medias)):
    datos_medias[i] = float(datos_medias[i])

print("▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂")
# CALCULAMOS EL xPROM:
xPromedio = sum(datos_medias) / len(datos_medias)

print("El xProm es: ",xPromedio)

# CÁLCULO DE LOS LIMITES DE CONTROL DE LAS MEDIAS:
LCI_MEDIAS = xPromedio-array_seleccionada[1]*sPromedio
if LCI_MEDIAS < 0:
    LCI_MEDIAS = 0

LCS_MEDIAS = xPromedio+array_seleccionada[1]*sPromedio
if LCS_MEDIAS < 0:
    LCS_MEDIAS = 0

# CÁLCULO DE LOS +-1 y +-2 Simgas:

MAS_1_SIGMA = xPromedio+(xPromedio-LCI_MEDIAS)/3
MENOS_1_SIGMA = xPromedio-(xPromedio-LCI_MEDIAS)/3
MAS_2_SIGMA = LCS_MEDIAS-(xPromedio-LCI_MEDIAS)/3
MENOS_2_SIGMA = LCI_MEDIAS+(xPromedio-LCI_MEDIAS)/3


print("El límite de control inferior para el G.C de medias es: ",LCI_MEDIAS)
print("El límite de control superior para el G.C de medias es: ",LCS_MEDIAS)

print("▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂")

print("El límite +2Sigma es: ", MAS_2_SIGMA)
print("El límite +1Sigma es: ", MAS_1_SIGMA)
print("El límite -1Sigma es: ", MENOS_1_SIGMA)
print("El límite -2Sigma es: ", MENOS_2_SIGMA)
print("▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂")

# 4.ACERCAMIENTO A LOS LIMITES DE CONTROL:

print("ANALISIS DEL ACERCAMIENTO A LOS LÍMITES DE CONTROL")
# Longitud mínima de la secuencia consecutiva que deseas (2 o 3)
longitud_minima = 2

# Variable para contar el número de valores consecutivos que cumplen con las condiciones
conteo_consecutivo = 0
conteo_consecutivo2 = 0
# para arriba de la media
for val1 in datos_medias:
    if MAS_2_SIGMA < val1 < LCS_MEDIAS:
        conteo_consecutivo += 1
        if conteo_consecutivo >= longitud_minima:
            print(f"Se encontraron {longitud_minima} o más datos consecutivos que cumplen con las condiciones.")
            break
    else:
        conteo_consecutivo = 0  # Reiniciamos el conteo si no se cumple la condición

# Si llegamos aquí y no se encontraron suficientes datos consecutivos, puedes mostrar un mensaje
if conteo_consecutivo < longitud_minima:
    print(f"No se encontraron {longitud_minima} o más datos consecutivos que cumplan con las condiciones.")

# para abajo de la media
for val2 in datos_medias:
    if LCI_MEDIAS < val2 < MENOS_2_SIGMA:
        conteo_consecutivo2 += 1
        if conteo_consecutivo2 >= longitud_minima:
            print(f"Se encontraron {longitud_minima} o más datos consecutivos que cumplen con las condiciones.")
            break
    else:
        conteo_consecutivo2 = 0  # Reiniciamos el conteo si no se cumple la condición

if conteo_consecutivo2 < longitud_minima:
    print(f"No se encontraron {longitud_minima} o más datos consecutivos que cumplan con las condiciones.")

print("▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂")

# 5.ACERCAMIENTO A LA LÍNEA CENTRAL:

print("ANALISIS DEL ACERCAMIENTO A LA LINEA CENTRAL (xProm)")
tolerancia_media = round(0.68*tiempo_gc)

# Inicializar un contador para contar los valores que cumplen la condición
contador = 0

# Iterar sobre los datos y verificar si cada valor cumple la condición
for val3 in datos_medias:
    if MENOS_1_SIGMA < val3 < MAS_1_SIGMA:
        contador += 1

# Verificar si hay más de 18 datos que cumplen la condición y mostrar un mensaje
if contador > tolerancia_media:
    print("El 68% de los puntos o más, están entre +1sigma y -1sigma.")
else:
    print("La cantidad de puntos entre +1sigma y -1sigma es normal.")

print("▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂")

# 6.PERIODICIDAD
print("ANALISIS DE PERIODICIDAD:")
# Inicializamos variables para llevar el conteo
conteo_arriba = 0
conteo_abajo = 0
conteo_igual = 0
condicion_anterior = None  # Para mantener un seguimiento de la condición anterior

# Iteramos a través de los elementos del array
for val4 in datos_medias:
    if val4 > xPromedio:
        if condicion_anterior != "arriba":
            print(f"Hubo un cambio: Ahora hay {conteo_arriba} valores consecutivos arriba de xPromedio.")
            conteo_arriba = 1
            condicion_anterior = "arriba"
        else:
            conteo_arriba += 1
    elif val4 < xPromedio:
        if condicion_anterior != "abajo":
            print(f"Hubo un cambio: Ahora hay {conteo_abajo} valores consecutivos abajo de xPromedio.")
            conteo_abajo = 1
            condicion_anterior = "abajo"
        else:
            conteo_abajo += 1
    else:
        if condicion_anterior != "igual":
            print(f"Hubo un cambio: Ahora hay {conteo_igual} valores consecutivos iguales a xPromedio.")
            conteo_igual = 1
            condicion_anterior = "igual"
        else:
            conteo_igual += 1

# Imprimimos los resultados finales
if condicion_anterior == "arriba":
    print(f"Hubo un cambio: Ahora hay {conteo_arriba} valores consecutivos arriba de xPromedio.")
elif condicion_anterior == "abajo":
    print(f"Hubo un cambio: Ahora hay {conteo_abajo} valores consecutivos abajo de xPromedio.")
elif condicion_anterior == "igual":
    print(f"Hubo un cambio: Ahora hay {conteo_igual} valores consecutivos iguales a xPromedio.")

print("▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂")
