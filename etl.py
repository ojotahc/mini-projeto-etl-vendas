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
print(bruto.duplicated().sum())
# %%
