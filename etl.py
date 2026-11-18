# %%
import pandas as pd
import os 
import sqlite3

# %%
def extrair() -> pd.DataFrame:
    df_bruto = pd.read_csv("data/raw/vendas_bruto.csv", encoding="utf-8")
    return df_bruto

# %%
bruto = extrair()
# %%
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
filtado = df[condicao]
print(filtado)