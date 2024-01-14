import openpyxl

wb = openpyxl.load_workbook("added_sheet.xlsx")
for sheet in wb:
    print(sheet.title)

source = wb["New title"]
new_sheet = wb.copy_worksheet(source)
new_sheet.title = "Copied New title"
for sheet in wb:
    print(sheet.title)

wb.save("copied_sheets.xlsx")