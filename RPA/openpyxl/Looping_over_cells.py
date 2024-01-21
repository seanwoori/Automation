from openpyxl import Workbook

if __name__ == "__main__":
    # Create a workbook and sheets
    filename = "Looping.xlsx"
    wb = Workbook()
    ws1 = wb["Sheet"]

    # Iterate over rows
    for row in range(1, 4):
        for col in range(1, 4):
            cell = ws1.cell(row=col, column=row)
            print(cell.coordinate, end=" ")
        print()
            

    # Save the wb
    wb.save(filename)

    
