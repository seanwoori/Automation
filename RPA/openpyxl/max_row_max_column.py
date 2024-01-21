from openpyxl import load_workbook

if __name__ == "__main__":
    # Create a workbook and sheets
    filename = "max_row_max_col.xlsx"
    wb = load_workbook(filename)
    ws1 = wb["Sheet"]

    # Iterate over rows, then columns
    print(f"max_row is in row {ws1.max_row} and max_column is in column {ws1.max_column}")
    for row in ws1.iter_rows(min_row=1, max_col=ws1.max_column, max_row=ws1.max_row):
        for cell in row:
            print("{0: <3}".format(cell.coordinate), end = " ")
        print()
    print("-"*50)
    for row in ws1.iter_rows(min_row=1, max_col=ws1.max_column, max_row=ws1.max_row):
        for cell in row:
            print("{0: <5}".format(str(cell.value)), end = " ")
        print()

    
    # Save the wb
    #wb.save(filename)

    
