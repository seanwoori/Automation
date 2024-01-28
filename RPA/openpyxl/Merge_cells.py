from openpyxl import Workbook

def set_values(ws):
    ws.delete_cols(1,100)
    counter = 1
    for row in ws.iter_rows(min_row=1, max_col=10, max_row=10):
        for cell in row:
            cell.value = counter
            counter += 1

def print_rows(ws):
    row_string = ""
    for row in ws.iter_rows(min_row=1, max_col=ws.max_column, max_row=ws.max_row):
        for cell in row:
            row_string += "{:<3}".format(str(cell.value) + " ")
        row_string += "\n"
    print(row_string)

if __name__ == "__main__":
    # Create a workbook and sheets
    filename = "Merge_cells.xlsx"
    wb = Workbook()
    ws1 = wb["Sheet"]

    # Insert values from 1 to 100 into a grid of 10x10 cells
    set_values(ws1)
    # Merge cells A1:B1
    ws1.merge_cells('A1:B1')
    wb.save(filename)
    #ws1.unmerge_cells('A2:D2')
    # Merge cells A4:C4
    #ws1.merge_cells(start_row=4, start_column=1, end_row=4, end_column=3)
    
    print_rows(ws1)

    wb.save(filename)
            

    
