import pandas as pd
from aux_class import csv_processor





#-----------
# Setando variaveis para teste
#----------- 
file = "data/cities_sales.csv"
columna = 'cidade'
atributo = 'Salvador'


#-----------
# Executando
#-----------    
# Instanciando com a classe; isso executa o "init"
csv_proc = csv_processor(file_path=file)

# Chamando a funcao de leitura de csv
csv_proc.load_csv()

# Chamando a funcao de filtrar
csv_proc.filter_df(column =  columna, attribute  = atributo) # filtro 1
df = csv_proc.filter_df("data_venda","2023-05-21") # filtro 2
print(df)
