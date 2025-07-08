import pandas as pd
import numpy as np

# Esto podría estar en un archivo de config
REQUIRED_COLUMNS = [
    "Product_A_Production_Time_Machine_1",
    "Product_A_Production_Time_Machine_2",
    "Product_B_Production_Time_Machine_1",
    "Product_B_Production_Time_Machine_2",
    "Machine_1_Available_Hours",
    "Machine_2_Available_Hours",
    "Price_Product_A",
    "Price_Product_B",
]

class DataLoader:
    def __init__(self, file, max_prod_a, max_prod_b):
        self.df = pd.read_csv(file)
        self.max_prod_a = max_prod_a
        self.max_prod_b = max_prod_b
        self.validate()

    def validate(self):
        # Validación df
        missing = [col for col in REQUIRED_COLUMNS if col not in self.df.columns]
        
        # Chequeos básicos
        if missing:
            raise ValueError(f"Columnas faltantes: {missing}")
        
        if self.df.isnull().any().any():
            raise ValueError("Datos faltantes en el archivo.")
        
        # Tipo esperado int/float
        non_numeric_cols = []
        for col in REQUIRED_COLUMNS:
            if not np.issubdtype(self.df[col].dtype, np.number):
                non_numeric_cols.append(col)
        if non_numeric_cols:        
            raise ValueError(f"La(s) columna(s) '{', '.join(non_numeric_cols)}' contiene datos no numéricos.")
        
        # Por naturaleza del problema los valores deben ser no negativos
        negative_columns = []
        for col in REQUIRED_COLUMNS:
            if (self.df[col] < 0).any():
                negative_columns.append(col)       
        if negative_columns:
            raise ValueError(f"La(s) columna(s) '{', '.join(negative_columns)}' contiene datos negativos.")
        
        # Validación máximos de producción (en caso de existir)
        if self.max_prod_a is not None:
            assert isinstance(self.max_prod_a, int), "La capacidad máxima de producción de B debe un número entero (no negativo)"
            assert self.max_prod_a >= 0, "La capacidad máxima de producción de A debe ser no negativo"
            
        if self.max_prod_b is not None:    
            assert isinstance(self.max_prod_b, int), "La capacidad máxima de producción de B debe un número entero (no negativo)"
            assert self.max_prod_b >= 0, "La capacidad máxima de producción de B debe ser no negativo"

