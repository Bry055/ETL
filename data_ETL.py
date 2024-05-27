import pandas as pd
from sqlalchemy import create_engine

# Leitura do CSV (Extração de Dados)
data_csv = pd.read_csv('ler_CSV.csv')

# Remover campos nulos (Transformação)
data_csv.dropna(inplace=True)

# Normalizar datas (Transformação)
data_csv['Data de Expiracao'] = pd.to_datetime(data_csv['Data de Expiracao'])
data_csv['Inicio da Liberacao'] = pd.to_datetime(data_csv['Inicio da Liberacao'])
data_csv['Nascimento'] = pd.to_datetime(data_csv['Nascimento'])
data_csv['Admissão'] = pd.to_datetime(data_csv['Admissão'])

# Normalizar strings (Transformação)
data_csv['Usuario'] = data_csv['Usuario'].str.title()

# Carregamento
engine = create_engine('sqlite:///meu_banco_de_dados.db')
data_csv.to_sql('Users', engine, index=False, if_exists='replace')
