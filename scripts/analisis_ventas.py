
import pandas as pd
import matplotlib.pyplot as plt

# Leer dataset
df = pd.read_csv("../datos/sales_sample_2024.csv")

# Mostrar primeras filas
print(df.head())

# Calcular ventas totales
ventas_totales = df["sales_amount"].sum()

print("Ventas totales:", ventas_totales)

# Agrupar ventas por fecha
ventas_por_fecha = df.groupby("sales_date")["sales_amount"].sum()

# Crear gráfico
plt.figure(figsize=(10,5))
ventas_por_fecha.plot()

plt.title("Ventas por Fecha")
plt.xlabel("Fecha")
plt.ylabel("Ventas")

# Guardar gráfico
plt.savefig("../resultados/grafico_ventas.png")

print("Gráfico generado correctamente")
