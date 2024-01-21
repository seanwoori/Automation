from openpyxl import Workbook

def create_sheets(wb, sheet_name_list):
    # Adds the sheets in the sheet_name_list to the workbook
    for sheet_name in sheet_name_list:
        wb.create_sheet(sheet_name)

if __name__ == "__main__":
    # Create a workbook and sheets
    filename = "Looping.xlsx"
    wb = Workbook()
    create_sheets(wb, ["Sheet2", "Sheet3", "Sheet4"])
    ws1 = wb["Sheet"]

    # Iterate over rows, then columns
    print("iter_rows:")
    for row in ws1.iter_rows(min_row=1, min_col= 1, max_col=4, max_row=3):
        #print(row)
        for cell in row:
            print(cell.coordinate, end = " ")
        print()
    print("-"*40)
    print("iter_cols:")
    for column in ws1.iter_cols(max_col=4, max_row=3):
        #print(column)
        for cell in column:
            print(cell.coordinate, end = " ")
        print()
    
    # Save the wb
    wb.save(filename)

    
