# %%
import pandas as pd
import os 
import sqlite3

# %%
def extrair() -> pd.DataFrame:
    df_bruto = pd.read_csv("data/raw/vendas_bruto.csv", encoding="utf-8")
    return df_bruto
# %%
def transformar(df_bruto: pd.DataFrame) -> pd.DataFrame:
    df_limpo =  df_bruto.copy()
    df_limpo["cliente"] = df_limpo["cliente"].str.strip()
    df_limpo["produto"] = df_limpo["produto"].str.strip()
    df_limpo["vendedor"] = df_limpo["vendedor"].str.strip()
    df_limpo["vendedor"] = df_limpo["vendedor"].str.capitalize()
    df_limpo["categoria"] = df_limpo["categoria"].str.capitalize()
    df_limpo["forma_pagamento"] = df_limpo["forma_pagamento"].str.capitalize()
    return df_limpo
# %%
if __name__ == "__main__":
    bruto = extrair()
    limpo = transformar(bruto)
# %%
print(limpo)
# %%
# verificar espaços
print(limpo[["cliente", "produto", "vendedor"]])
print(limpo["cliente"].unique())
print(limpo["produto"].unique())
print(limpo["vendedor"].unique())
print(limpo["categoria"].unique())
print(limpo["forma_pagamento"].unique())
# %%
print(bruto["cliente"].nunique())
print(bruto["produto"].nunique())
print(bruto["vendedor"].nunique())
print(bruto["categoria"].nunique())
print(bruto["forma_pagamento"].nunique())
# %%
print(limpo["cliente"].nunique())
print(limpo["produto"].nunique())
print(limpo["vendedor"].nunique())
print(limpo["categoria"].nunique())
print(limpo["forma_pagamento"].nunique())
