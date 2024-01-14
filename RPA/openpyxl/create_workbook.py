import openpyxl

wb = openpyxl.Workbook()
ws = wb.create_sheet("A sheet", 0)
ws2 = wb.create_sheet("Sheet nr 2")

for sheet in wb:
    print(sheet.title)


del wb["A sheet"] # delete the sheet
for sheet in wb:
    print(sheet.title)

ws2.title = "New title"

wb.save("added_sheet.xlsx")