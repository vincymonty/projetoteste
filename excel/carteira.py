import pandas as pd
from openpyxl import load_workbook
dados = pd.read_excel("D:/FACULDADE/excel/teste_carteira.xlsx")
teste = dados.filter(items=["Nom Cliente", "Cód Item Cliente", "Den, Item", "Familia", "Liberado", "pedido", "Qtd Liberada"])
print(teste)
filtro_familia = teste[teste["Familia"].isin(["HIDROSSOLUVEIS", "LIQUIDOS", "P.A. LIQUIDOS"])]
#print(filtro_familia)
filtro_liberado = filtro_familia["Liberado"] == "LIBERADO"
filtrob = (filtro_familia[filtro_liberado])
#filtrob.to_excel("D:/FACULDADE/excel/teste_carteira_filtrada.xlsx")
print(filtrob)
df = pd.DataFrame(filtrob)
df.insert(7, "lote","")
df.insert(8, "Data Fab","")
df.insert(9, "Validade","")
df.insert(10, "Qtd Paletes","")
df.drop("Familia", axis=1, inplace=True)
df.drop("Liberado", axis=1, inplace=True)
print(df)
df.to_excel("D:/FACULDADE/excel/teste_carteira_filtrada.xlsx")
workbook = load_workbook ("D:/FACULDADE/excel/teste_carteira_filtrada.xlsx")
worksheet = workbook["Sheet1"]
worksheet.column_dimensions["A"].width = 5
worksheet.column_dimensions["B"].width = 50
worksheet.column_dimensions["C"].width = 15.5
worksheet.column_dimensions["D"].width = 23
worksheet.column_dimensions["E"].width = 9
worksheet.column_dimensions["F"].width = 12
worksheet.column_dimensions["G"].width = 14
worksheet.column_dimensions["H"].width = 11
worksheet.column_dimensions["I"].width = 10
worksheet.column_dimensions["J"].width = 11
worksheet.row_dimensions[1].width = 18
workbook.save("D:/FACULDADE/excel/teste_carteira_filtrada.xlsx")