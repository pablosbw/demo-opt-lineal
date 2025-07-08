import pulp

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

class OptimizationModel:
    def __init__(self, df):
        self.df = df
        self.products = ["A", "B"]
        self.machines = ["1", "2"]
        
    def solve(self):
        prob = pulp.LpProblem("Maximize Revenue", pulp.LpMaximize)
        
        # Variables enteras positivas
        x = {f"Product_{v}": pulp.LpVariable(f"Product_{v}", lowBound=0, cat=pulp.LpInteger) for v in self.products}

        # FO
        # \sum{x_i * val_i}
        
        prob += pulp.lpSum( x[f"Product_{var}"] * self.df[f"Price_Product_{var}"].iloc[0] for var in self.products)
        
        # Restricciones
        # \sum{x_i * t_{ij}} <= m_j

        for m in self.machines:
            prob += pulp.lpSum( x[f"Product_{var}"] * self.df[f"Product_{var}_Production_Time_Machine_{m}"].iloc[0] for var in self.products)  <= self.df[f"Machine_{m}_Available_Hours"].iloc[0]
        
        prob.solve()
        
        result = {var_name: var.varValue for var_name, var in x.items()}
        total = pulp.value(prob.objective)
        
        return result, total
