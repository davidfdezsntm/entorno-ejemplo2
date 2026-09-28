import pandas as pd

ventas_enero = pd.DataFrame({
    "producto": ["A", "B", "C"],
    "ventas": [100, 150, 200]
})

ventas_febrero = pd.DataFrame({
    "producto": ["A", "B", "C"],
    "ventas": [120, 130, 210]
})

ventas_totales = pd.concat([ventas_enero, ventas_febrero], ignore_index=True)

print(ventas_totales)