from openpyxl import Workbook


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
    filename = "Deleting_inserting_rows_cols.xlsx"
    wb = Workbook()
    ws1 = wb["Sheet"]

    # Insert values from 1 to 100 into a grid of 10x10 cells
    set_values(ws1)

    print_rows(ws1)

    # Insert a row at the top
    ws1.insert_rows(1)
    # Insert a row above the second row (which is now the former first row)
    ws1.insert_rows(2)

    print_rows(ws1)

    # Delete the top row
    ws1.delete_rows(1)  # zeroeth index for rows

    print_rows(ws1)

    # insert a blank column at the fourth column and delete the first column
    ws1.insert_cols(4)
    print_rows(ws1)
    ws1.delete_cols(1)  # first index for columns

    print_rows(ws1)

    # reset values
    set_values(ws1)
    print_rows(ws1)
    # delete 5 columns, starting from column 1
    ws1.delete_cols(1, 5)
    print_rows(ws1)
    # delete four rows, starting from row 1
    ws1.delete_rows(1, 4)
    print_rows(ws1)

    # Save the wb
    wb.save(filename)
