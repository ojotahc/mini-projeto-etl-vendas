# 📋 Diagnóstico final da Etapa 1

| Coluna | Problema |
| :--- | :--- |
| **Linhas** | 4 vendas duplicadas, registradas duas vezes (infla o faturamento) |
| **`data_venda`** | Tipo texto e 3 formatos misturados |
| **`cliente`** | 3 nulos e espaços extras |
| **`produto`** | Espaços extras |
| **`categoria`** | Caixa misturada (papelaria, eletrônicos) |
| **`quantidade`** | 4 nulos, e o tipo float é consequência deles |
| **`preco_unitario`** | 3 nulos |
| **`vendedor`** | 5 nulos, espaços extras e caixa misturada |
| **`forma_pagamento`** | Caixa misturada (dinheiro, cartão) |

---

## 💻 Código de Análise Exploratória

```python
print(bruto.shape)
# %%
print(bruto.head(10))
# %%
print(bruto["data_venda"])
# %%
print(bruto.info())
# %%
print(bruto.isnull().sum())
# %%
print(bruto["categoria"].unique())
# %%
print(bruto["categoria"].value_counts())
# %%
print(bruto["vendedor"].unique())
# %%
print(bruto["forma_pagamento"].unique())
# %%
print(bruto["data_venda"].head(10))
# %%
print(bruto.duplicated().sum())
# %%
condicao = bruto["id_venda"].duplicated(keep=False)
print(condicao)

# %%
filtado = bruto[condicao]
print(filtado)
# %%
print(bruto["cliente"].unique())
# %%
print(bruto["produto"].unique())
# %%
```