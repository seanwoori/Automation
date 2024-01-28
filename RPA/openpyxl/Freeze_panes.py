from openpyxl import load_workbook

if __name__ == "__main__":
    # Create a workbook and sheets
    filename = "Freeze_panes.xlsx"
    wb = load_workbook(filename)
    ws1 = wb["Sheet1"]

    # Freeze the top row
    ws1.freeze_panes = "A1"

    """

    freeze_panes settings             Rows and columns frozen
    
    sheet.freeze_panes = 'A2'         Row 1

    sheet.freeze_panes = 'B1'         Column A

    sheet.freeze_panes = 'C1'         Columns A and B

    sheet.freeze_panes = 'C2'         Row 1 and columns A and B

    sheet.freeze_panes = 'A1' or      No Frozen panes
    sheet.freeze_panes = None
    """

    wb.save(filename)
            

    
