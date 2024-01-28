from openpyxl import Workbook

if __name__ == "__main__":
    # Create a workbook and sheets
    filename = "Fold.xlsx"
    wb = Workbook()
    ws1 = wb["Sheet"]

    ws1.column_dimensions.group('A','D', hidden=True)
    ws1.row_dimensions.group(1,10, hidden=True)

    wb.save(filename)
            

    
