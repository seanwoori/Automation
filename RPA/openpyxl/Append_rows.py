#!/usr/bin/env python3

"""
Inserting rows with the append method
"""

from openpyxl import Workbook

def print_rows(ws):
    row_string = ""
    for row in ws.iter_rows(min_row=1, max_col=ws.max_column, max_row=ws.max_row):
        for cell in row:
            row_string += "{:<8}".format(str(cell.value) + " ")
        row_string += "\n"
    print(row_string)

if __name__ == "__main__":
    # Create a workbook and sheets
    filename = "Append.xlsx"
    wb = Workbook()
    ws1 = wb["Sheet"]

    #print_rows(ws1)

    # Create Sales data, a list of lists
    # Using underscore for easier separation of thousands
    sales_data = [ ["North",  670_000, 230_000],\
                  ["South", 340_000, 550_000],\
                  ["West", 111_000, 95_000],
                  ["East", 456_000, 123_000] ]

    # add column headings
    ws1.append( ["Sales", 2018, 2019] )
    #print_rows(ws1)
    for row in sales_data:
        ws1.append(row)

    print_rows(ws1)
   
    wb.save(filename)


    
