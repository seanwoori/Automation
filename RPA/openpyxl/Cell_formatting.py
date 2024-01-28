from openpyxl import load_workbook, Workbook
from copy import copy
from openpyxl.styles import colors, Font
from openpyxl.styles.fills import PatternFill
from openpyxl.styles.borders import Border, Side, BORDER_THIN, BORDER_THICK, BORDER_DASHDOT, BORDER_DOUBLE
from openpyxl.styles.numbers import FORMAT_PERCENTAGE_00
from openpyxl.styles.protection import Protection
from openpyxl.styles.alignment import Alignment

def print_rows(ws):
    row_string = ""
    for row in ws.iter_rows(min_row=1, max_col=ws.max_column, max_row=ws.max_row):
        for cell in row:
            row_string += "{:<3}".format(str(cell.value) + " ")
        row_string += "\n"
    print(row_string)

if __name__ == "__main__":
    # Create a workbook and sheets
    filename = "Cell formatting.xlsx"
    wb = load_workbook("Cell formatting_original.xlsx")
    ws1 = wb["Sheet"]

    # Insert values from 1 to 100 into a grid of 10x10 cells
    print_rows(ws1)    

    font_cell = ws1.cell(row=2, column=2)           #B2
    border_cell = ws1.cell(row=3, column=4)         #D3
    fill_cell = ws1.cell(row=4, column=6)           #F4
    number_format_cell = ws1.cell(row=5, column=8)  #H5
    alignment_cell = ws1.cell(row=8,column=9)       #I8
    # See openpyxl.styles.colors for a list of colors
    # See openpyxl.styles.fonts for all elements of Font
    font_cell.font = Font(name='Arial', size=18, b=True, i=True, color=colors.COLOR_INDEX[12])
    
    # openpyxl.styles.borders
    borders = Border(left=Side(border_style=BORDER_THIN, color='00000000'),\
                         right=Side(border_style=BORDER_THICK, color='00000000'),\
                         top=Side(border_style=BORDER_DASHDOT, color='00000000'),\
                         bottom=Side(border_style=BORDER_DOUBLE, color='00000000'))
    border_cell.border = borders
    

    # openpyxl.styles.fills
    red_color = colors.Color(rgb='00FF0000')
    solid_red_fill = PatternFill(patternType='solid', fgColor=red_color)
    fill_cell.fill = solid_red_fill
    

    # openpyxl.styles.numbers
    number_format_cell.number_format = FORMAT_PERCENTAGE_00
    
    # Create a Workbook password and lock the structure
    wb2 = Workbook()
    wb2.security.workbookPassword = '1234'
    wb2.security.lockStructure = True
    wb2.save("Cell formatting2.xlsx")

    # Protect the sheet
    ws1.protection.sheet = True
    ws1.protection.password = '1234'
    ws1.protection.enable()

    
    # Unlock cell A1
    ws1.cell(row=1,column=1).protection = Protection(locked=False, hidden=False)
    wb.save(filename)

    # openpyxl.styles.alignment
    
##    alignment_cell.alignment = Alignment(horizontal="center", vertical=None, textRotation=0,\
##                                         wrapText=None, shrinkToFit=None, indent=0,\
##                                         relativeIndent=0, justifyLastLine=None,\
##                                         readingOrder=0, text_rotation=None,\
##                                         wrap_text=None, shrink_to_fit=None, mergeCell=None)
##
##    wb.save(filename)
##            
##
##    
