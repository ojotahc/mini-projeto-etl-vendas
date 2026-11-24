# %%
import pandas as pd
import os 
import sqlite3

DB = "data/processed/vendas.db"

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
    # otimizar essa tratativa depois
    cliente_com_nulo = df_limpo["cliente"]
    cliente_sem_nulo = cliente_com_nulo.fillna("Não informado")
    df_limpo["cliente"] = cliente_sem_nulo

    vendedor_com_nulo = df_limpo["vendedor"]
    vendedor_sem_nulo = vendedor_com_nulo.fillna("Não informado")
    df_limpo["vendedor"] = vendedor_sem_nulo

    df_limpo = df_limpo.dropna(subset=["quantidade", "preco_unitario"])

    df_limpo["quantidade"] = df_limpo["quantidade"].astype(int)

    df_limpo = df_limpo.reset_index(drop=True)

    return df_limpo

def carregar(df_limpo: pd.DataFrame) -> None:
    os.makedirs("data/processed", exist_ok=True)

    df_para_gravar = df_limpo.copy()
    df_para_gravar["data_venda"] = df_para_gravar["data_venda"].dt.strftime("%Y-%m-%d")

    conexao = sqlite3.connect(DB)
    try:
        df_para_gravar.to_sql("vendas", conexao, if_exists="replace", index=False)
    finally:
        conexao.close()


if __name__ == "__main__":
    bruto = extrair()
    limpo = transformar(bruto)
    carregar(limpo)
# %%
"""
Teste rápido

con = sqlite3.connect(DB)
print(pd.read_sql("SELECT COUNT(*) AS linhas FROM vendas", con))
print(pd.read_sql("SELECT SUM(quantidade * preco_unitario) AS faturamento FROM vendas", con))
print(pd.read_sql("SELECT * FROM vendas LIMIT 5", con))
con.close()
"""
# %%
