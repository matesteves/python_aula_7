from ETL import read_csv
import analytics_functions as af

file_path: str = "data/sales.csv"

sales = read_csv(file_path)

nao_entregues = af.produtos_nao_entregues(sales)
print(nao_entregues)

total_revenue = af.total_revenue(sales)
print(total_revenue)