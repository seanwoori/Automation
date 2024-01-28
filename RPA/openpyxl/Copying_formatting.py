from openpyxl import Workbook
from copy import copy
from openpyxl.styles import Font


def set_values(ws):
    ws.delete_cols(1, 100)
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
    filename = "Moving_copying_ranges.xlsx"
    wb = Workbook()
    ws1 = wb["Sheet"]

    # Insert values from 1 to 100 into a grid of 10x10 cells
    set_values(ws1)
    print_rows(ws1)

    # move the whole range ten rows down
    ws1.move_range("A1:J10", rows=10, cols=0)

    print_rows(ws1)

    # reset values
    set_values(ws1)

    print_rows(ws1)

    # copy cell A1's value and formatting to cell A12
    old_cell = ws1.cell(row=1, column=1)
    old_cell.font = Font(name="Arial", size=18, color="FF0000")
    # old_cell.font = Font(name='Arial', size=18, color="FF0000")
    new_cell = ws1.cell(row=12, column=1, value=ws1.cell(row=1, column=1).value)
    new_cell.font = copy(old_cell.font)
    new_cell.border = copy(old_cell.border)
    new_cell.fill = copy(old_cell.fill)
    new_cell.number_format = copy(old_cell.number_format)
    new_cell.protection = copy(old_cell.protection)
    new_cell.alignment = copy(old_cell.alignment)

    wb.save(filename)
