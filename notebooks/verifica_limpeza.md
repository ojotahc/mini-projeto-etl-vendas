# 🧹 Verificação da Limpeza de Dados

Abaixo está o script utilizado para validar se os espaços extras, valores únicos e padronizações de texto foram aplicados corretamente na base limpa (`limpo`) em comparação com a base original (`bruto`).

## 1. Inspeção Visual e Valores Únicos (Base Limpa)

Verifica o conteúdo das colunas de texto e lista todos os valores únicos após a padronização:

```python
# verificar limpeza
print(limpo[["cliente", "produto", "vendedor"]])
print(limpo["cliente"].unique())
print(limpo["produto"].unique())
print(limpo["vendedor"].unique())
print(limpo["categoria"].unique())
print(limpo["forma_pagamento"].unique())
```

## 2. Contagem de Valores Únicos: Antes vs. Depois

Compara a quantidade de registros distintos antes (`bruto`) e depois (`limpo`) da remoção de espaços extras e padronização de caixa (maiúsculas/minúsculas):

### Antes (`bruto`)

```python
print(bruto["cliente"].nunique())
print(bruto["produto"].nunique())
print(bruto["vendedor"].nunique())
print(bruto["categoria"].nunique())
print(bruto["forma_pagamento"].nunique())
```

### Depois (`limpo`)

```python
print(limpo["cliente"].nunique())
print(limpo["produto"].nunique())
print(limpo["vendedor"].nunique())
print(limpo["categoria"].nunique())
print(limpo["forma_pagamento"].nunique())
```

## 3. Etapa 3 - Removendo Duplicados

Valida o novo formato do DataFrame e confirma se ainda existem linhas inteiras repetidas ou IDs de venda duplicados:

```python
print(limpo)
print(limpo.shape)
print(limpo.duplicated().sum())
print(limpo["id_venda"].duplicated().sum())
```