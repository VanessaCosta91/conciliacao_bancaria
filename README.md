# Conciliação Automática de Transações

Este projeto simula a conciliação automática entre transações de vendas e extrato bancário, utilizando Python e pandas.


##  Objetivo

Comparar registros financeiros de duas fontes diferentes:
- Vendas realizadas (ex: cartão de debito, cartão de credito, Pix)
- Recebimentos no extrato bancário

A conciliação identifica se:
- Os valores foram corretamente recebidos
- Existem diferenças de valor
- Existem lançamentos que não constam em uma das fontes


## Tecnologias usadas
- Python
- pandas
- openpyxl


## Como usar

1. Clone o repositório

Abra o terminal e digite:
```
git clone https://github.com/VanessaCosta91/conciliacao_bancaria.git
cd conciliacao-transacoes
```

2. Instale as dependências
Crie (se quiser) e ative um ambiente virtual, e depois instale as bibliotecas necessárias:
```
pip install -r requirements.txt
```

3. Gere os dados fictícios
Execute o script para gerar os arquivos de entrada (vendas.csv e extrato_bancario.csv):
```
python src/gerar_dados.py
```

4. Execute a conciliação
Rode o script principal para realizar a conciliação e gerar o relatório:
```
python src/main.py
```

5. Verifique o resultado
Abra o arquivo Excel gerado para ver:
- Transações conciliadas
- Diferenças de valor
- Registros ausentes


## Autora
Vanessa Costa

Projeto de portfólio, com foco em aplicações financeiras e automações úteis no contexto bancário e cooperativista.








