import pandas as pd

vendas = pd.read_csv('data/vendas.csv')
extrato = pd.read_csv('data/extrato_bancario.csv')

'''
print('Vendas: \n', vendas.head().to_string())
print('\nExtrato: \n', extrato.head().to_string())
'''

# Juntas os dois dataframes
df = pd.merge(vendas, extrato, left_on='NSU', right_on='Identificador', how="outer", suffixes=('_venda', '_extrato'))

# Cria coluna situação
def comparar(linha):
    if pd.isna(linha['Valor_venda']):
        return 'Somente no relatório de vendas'
    elif pd.isna(linha['Valor_extrato']):
        return 'Somente no extrato bancário'
    elif abs(linha['Valor_venda'] - linha['Valor_extrato']) == 0:
        return 'Conciliado'
    else:
        return 'Diferença de valor'

df['Situacao'] = df.apply(comparar, axis=1)

# Exporta conciliação para excel
df.to_excel('outputs/Relatorio_conciliacao.xlsx', index=False)
print('Relatório gerado com sucesso!')

