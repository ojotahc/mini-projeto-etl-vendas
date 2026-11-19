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
    df_limpo = df_limpo.drop_duplicates(subset=["id_venda"], keep="first")
    texto = df_limpo["data_venda"]
    ano_primeiro = pd.to_datetime(texto, format="%Y-%m-%d", errors="coerce")
    dia_barra    = pd.to_datetime(texto, format="%d/%m/%Y", errors="coerce")
    dia_hifen    = pd.to_datetime(texto, format="%d-%m-%Y", errors="coerce")
    df_limpo["data_venda"] = ano_primeiro.fillna(dia_barra).fillna(dia_hifen)
    return df_limpo
# %%
if __name__ == "__main__":
    bruto = extrair()
    limpo = transformar(bruto)
# %%

# %%
# %%
