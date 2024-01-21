from openpyxl import Workbook
from openpyxl.worksheet.table import Table, TableStyleInfo

def print_rows(ws):
    row_string = ""
    for row in ws.iter_rows(min_row=1, max_col=ws.max_column, max_row=ws.max_row):
        for cell in row:
            row_string += "{:<6}".format(str(cell.value) + " ")
        row_string += "\n"
    print(row_string)

if __name__ == "__main__":
    # Create a workbook and sheets
    filename = "Tables.xlsx"
    wb = Workbook()
    ws1 = wb["Sheet"]
    
    # Create Sales data, a list of lists
    # Using underscore for easier separation of thousands
    sales_data = [["North",  670_000, 230_000],\
                  ["South", 340_000, 550_000],\
                  ["West", 111_000, 95_000],
                  ["East", 456_000, 123_000]]

    # add column headings. String type only
    ws1.append(["Sales", "2018", "2019"])
    for row in sales_data:
        ws1.append(row)

    print_rows(ws1)

    # Create a table. Remember that all headers need to be of string type, None type is not acceptable
    sales_table = Table(displayName="SalesTable", ref="A1:C5")

    # Add a default style
    style = TableStyleInfo(name="TableStyleMedium8", showRowStripes=True)
    sales_table.tableStyleInfo = style
    # Add the table to the sheet
    ws1.add_table(sales_table)

    print_rows(ws1)

    wb.save(filename)
            

    
