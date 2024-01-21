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
            row_string += "{:<6}".format(str(cell.value) + " ")
        row_string += "\n"
    print(row_string)

if __name__ == "__main__":
    # Create a workbook and sheets
    filename = "Moving_copying_ranges.xlsx"
    wb = Workbook()
    ws1 = wb["Sheet"]

    # Insert values from 1 to 100 into a grid of 10x10 cells
    set_values(ws1)
    print_rows(ws1)
    print("*"*30)

##    # move the whole range ten rows down
##    ws1.move_range("A1:J10", rows=10, cols=0)
##
##    print_rows(ws1)

##    #Move cell A1 30 rows down
##    #ws1._move_cell(row, column, row_offset, col_offset)
##    ws1._move_cell(1, 1, 30, 0)
##    print_rows(ws1)
##
##    # reset values
##    set_values(ws1)
##
##    print_rows(ws1)
##
##    # copy cell A1's value
##    old_cell = ws1.cell(row=1, column=1)
##    new_cell = ws1.cell(row=12, column=1, value= old_cell.value)
##
##    print_rows(ws1)
    
##     Copy the first row to row 15
    rows = ws1.iter_rows(min_row=0, max_row=1)

    for row in rows:
        for cell in row:
            new_cell = ws1.cell(row=15, column=cell.col_idx, value= cell.value)

    print_rows(ws1)

            

    
