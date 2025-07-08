import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Cria dados para serem usados nos testes

# Inicia geração de números aleatórios
np.random.seed(42)
random.seed(42)

# Define os meios de pagamentos e nomes cliente que vão ser usado para gerar arquivos
meios_pagamento = ['Pix', 'Cartão de Crédito', 'Cartão de Débito', 'Boleto']
clientes = ['Roberto', 'Maiara','Cleide','José','João', 'Maria', 'Carlos', 'Ana', 'Luciana', 'Pedro', 'Fernanda']

# Cria arquivo de vendas

# Cria lista com valores a serem utilizados
vendas = []
for i in range(100):

    data = datetime.today() - timedelta(days=random.randint(0,30))
    valor = round(random.uniform(20,300),2)
    cliente = random.choice(clientes)
    meio = random.choice(meios_pagamento)
    nsu = f'{i:03}'
    vendas.append([data.date(), valor, cliente, meio, nsu])

# Converte lista para Dataframe
df_vendas = pd.DataFrame(vendas, columns=['Data', 'Valor', 'Cliente', 'Meio_de_Pagamento', 'NSU'])
# Salva arquivo .CSV
df_vendas.to_csv("data/vendas.csv", index=False)


# Cria arquivo de extrato bancário

# Cria listas que serão usadas para gerar arquivo do extrato bancário
extrato = []

# escolhe amostra de valor das vendas para simular valor que cai na conta
indices_conciliados = random.sample(range(100), 70)
for i in indices_conciliados:
    venda = df_vendas.iloc[i]
    descricao = f'Recebimento {venda['Meio_de_Pagamento']} - {venda['NSU']}'
    extrato.append([venda['Data'], descricao, venda['Valor'], 'C', venda['NSU']])

# Adiciona lançamentos de operações bancários comuns em extratos
for i in range(5):
    data = datetime.today() - timedelta(days=random.randint(0,10))
    valor = round(random.uniform(9,35),2)
    descricao = random.choice(['Tarifa bancária', 'TED', 'Juros', 'IOF'])
    identificador = f'{i:03}'
    extrato.append([data.date(), descricao, valor, 'D', identificador])

# Converte lista para Dataframe
df_extrato = pd.DataFrame(extrato, columns=['Data', 'Descricao', 'Valor', 'Tipo', 'Identificador'])

#Salva em arquivo do extrato com .csv
df_extrato.to_csv('data/extrato_bancario.csv', index=False)

