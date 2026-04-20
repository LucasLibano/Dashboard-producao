import pandas as pd

arquivo_excel = "Produção.xlsx"

df = pd.read_excel(arquivo_excel)

df.to_csv("arquivo_convertido.csv", index=False, encoding="utf-8-sig")

print("Arquivo convertido com sucesso!")