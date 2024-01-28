from openpyxl import load_workbook
from openpyxl.worksheet.page import PrintPageSetup

if __name__ == "__main__":
    # Create a workbook and sheets
    filename = "Page_setup.xlsx"
    wb = load_workbook(filename)
    ws1 = wb["Sheet"]

    # openpyxl.worksheet.page module
    # Parameters from "Source code for openpyxl.worksheet.worksheet"
    ws1.page_setup.paperSize = ws1.PAPERSIZE_A4
    ws1.page_setup.orientation = ws1.ORIENTATION_LANDSCAPE
    ws1.page_setup.fitToHeight = 0
    ws1.page_setup.fitToWidth = 1

    ws1.page_setup = PrintPageSetup(worksheet=None, orientation=ws1.ORIENTATION_PORTRAIT, paperSize=ws1.PAPERSIZE_LETTER,\
                                    scale=None, fitToHeight=None, fitToWidth=None, firstPageNumber=None,\
                                    useFirstPageNumber=None, paperHeight=None, paperWidth=None, pageOrder=None,\
                                    usePrinterDefaults=None, blackAndWhite=None, draft=None, cellComments=None,\
                                    errors=None, horizontalDpi=None, verticalDpi=None, copies=None, id=None)


    wb.save(filename)
            

    
