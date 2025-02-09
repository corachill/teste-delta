# PROJETO DE CARONAS DA UNB
import sys
import os
import pyarrow
import fastparquet

#Definir a variavel dim_user coom global para atualiza-la
global dim_user 

# Adiciona o diretório src ao caminho de busca
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))


from src.database import DataBase as db
from src.utils import *
from src.utils import gen_id, gen_privete_key

import pandas as pd


#Verificar se a base de dados existe, se não existe, criar.
path = '.\\data\\'
if db.exist_database(path)==True:
    pass
else:
    db.creat_database(path)
 
 
# Abrindo o banco de dados como DataFrame.
# Caminho do banco de dados dim_user.
path_dim_user = '.\\data\\' + 'dim_user.parquet'
# a biblioteca pandas lê o banco de dados com a função read_parquet.
dim_user = pd.read_parquet(path_dim_user)

# Caminho do banco de dados fact_ride.
path_fact_ride = '.\\data\\' + 'fact_ride.parquet'
# a biblioteca pandas lê o banco de dados com a função read_parquet.
fact_ride = pd.read_parquet(path_fact_ride)

