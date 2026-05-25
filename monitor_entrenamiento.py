"""
Nombre del Alumno: Jetro Garcia
Matrícula: ux25ii347
Fecha: 25/05/2026
Examen Segundo Parcial - Programación Estructurada
"""

# ==========================================
# 1. IMPORTACIÓN DE BIBLIOTECAS ESTÁNDAR
# ==========================================

import datetime
import math
import random
import statistics
import sys

# ==========================================
# 2. DEFINICIÓN DE CONSTANTES
# ==========================================

MAX_EPOCHS = 10
UMBRAL_ERROR_CRITICO = 0.95


# ==========================================
# 3. FUNCIONES DEFINIDAS POR EL USUARIO
# ==========================================

def obtener_info_sistema():
    """
    Usa la biblioteca 'sys' para validar el entorno de ejecución.
    """

    print("\n--- INFORMACIÓN DEL SISTEMA ---")

    # Llamada 1 a sys
    print("Plataforma:", sys.platform)

    # Llamada 2 a sys
    print("Versión de Python:")
    print(sys.version)

    # Llamada 3 a sys
    print("Argumentos del sistema:", sys.argv)


def simular_metricas_entrenamiento(cantidad_epochs):
    """
    Usa las bibliotecas 'random' y 'datetime'
    para simular datos de entrenamiento.
    """

    print("\n--- SIMULANDO ENTRENAMIENTO IA ---")

    lista_loss = []
    lista_latencias = []

    # Llamada 1 datetime
    inicio = datetime.datetime.now()

    # Llamada 2 datetime
    fecha_formateada = inicio.strftime("%d/%m/%Y %H:%M:%S")

    print("Inicio del entrenamiento:", fecha_formateada)

    eventos = [
        "Epoch exitoso",
        "Gradiente inestable",
        "Actualización de pesos",
        "Sincronización de GPU"
    ]

    for epoch in range(1, cantidad_epochs + 1):

        # Llamada 1 random
        loss = random.uniform(0.10, 1.00)

        # Llamada 2 random
        probabilidad = random.randint(1, 100)

        # Llamada 3 random
        evento = random.choice(eventos)

        latencia = random.uniform(10.0, 40.0)

        lista_loss.append(loss)
        lista_latencias.append(latencia)

        print("\nEpoch:", epoch)
        print("Loss:", round(loss, 4))
        print("Probabilidad de éxito:", probabilidad, "%")
        print("Evento:", evento)
        print("Latencia:", round(latencia, 2), "ms")

        if loss > UMBRAL_ERROR_CRITICO:
            print("\n¡ERROR CRÍTICO DETECTADO!")
            print("Finalizando entrenamiento...")

            # Llamada importante de sys
            sys.exit()

    # Llamada 3 datetime
    fin = datetime.datetime.now()

    diferencia = fin - inicio

    print("\nTiempo total de entrenamiento:", diferencia)

    return lista_loss, lista_latencias


def analizar_rendimiento(lista_loss, lista_latencias):
    """
    Usa la biblioteca statistics para analizar datos.
    """

    print("\n--- ANÁLISIS DE RENDIMIENTO ---")

    # Llamada 1 statistics
    promedio = statistics.mean(lista_loss)

    # Llamada 2 statistics
    desviacion = statistics.stdev(lista_loss)

    # Llamada 3 statistics
    mediana = statistics.median(lista_latencias)

    print("Media de Loss:", round(promedio, 4))
    print("Desviación Estándar:", round(desviacion, 4))
    print("Mediana de Latencia:", round(mediana, 2))


def calcular_rmse(predicciones, reales):
    """
    Usa la biblioteca math para calcular RMSE.
    """

    print("\n--- CÁLCULO RMSE ---")

    suma = 0

    for i in range(len(predicciones)):

        diferencia = reales[i] - predicciones[i]

        # Llamada 1 math
        valor_absoluto = math.fabs(diferencia)

        # Llamada 2 math
        cuadrado = math.pow(valor_absoluto, 2)

        suma += cuadrado

    promedio = suma / len(predicciones)

    # Llamada 3 math
    rmse = math.sqrt(promedio)

    epochs_redondeados = math.ceil(rmse)

    print("RMSE:", round(rmse, 4))
    print("Epochs redondeados:", epochs_redondeados)

# ==========================================
# 4. PROGRAMA PRINCIPAL (PUNTO DE ENTRADA)
# ==========================================

def main():

    print("=== INICIANDO SIMULADOR DE AGENTES DE IA ===")

    obtener_info_sistema()

    lista_loss, lista_latencias = simular_metricas_entrenamiento(MAX_EPOCHS)

    analizar_rendimiento(lista_loss, lista_latencias)

    predicciones = [0.8, 0.6, 0.7, 0.9]
    reales = [1.0, 0.5, 0.8, 1.0]

    calcular_rmse(predicciones, reales)

    print("\n=== ENTRENAMIENTO FINALIZADO ===")


if __name__ == "__main__":
    main()