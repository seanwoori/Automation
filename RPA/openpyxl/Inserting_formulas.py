from openpyxl import Workbook

def print_rows(ws):
    row_string = ""
    for row in ws.iter_rows(min_row=1, max_col=ws.max_column, max_row=ws.max_row):
        for cell in row:
            row_string += "{:<16}".format(str(cell.value) + " ")
        row_string += "\n"
    print(row_string)

if __name__ == "__main__":
    # Create a workbook and sheets
    filename = "Formulae.xlsx"
    wb = Workbook()
    ws1 = wb["Sheet"]

    """
    NB you must use the English name for a function
    and function arguments must be separated by commas
    and not other punctuation such as semi-colons.
    """

    # Insert values
    for i in range(1,11):
        ws1.cell(row=i, column=1).value = i*i
        ws1.cell(row=i,column=2).value = i/2

    print_rows(ws1)
    #=SUM(A1:A10)

    # Define the first and last cell used in the formula
    first_cell = ws1.cell(row=1, column=1) #A1
    last_cell = ws1.cell(row=10,column=1) #A10

    # Create the formula =SUM(A1:A10)
    ws1.cell(row=11, column=1).value = "=SUM(" +str(first_cell.coordinate) + ":" + str(last_cell.coordinate) +")"
    print_rows(ws1)

    

    # Move the formula one step to the right, and transpose the formula
    ws1._move_cell(row=11,column=1,row_offset=0,col_offset=1,translate=True)
    print_rows(ws1)
    
    wb.save(filename)
            

    
