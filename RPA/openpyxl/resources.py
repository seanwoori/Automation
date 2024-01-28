import win32com.client
import os

xl = win32com.client.Dispatch("Excel.Application")

workbook_name = "sort_workbook.xlsx"
absolute_path = os.path.abspath(workbook_name)


wb = xl.Workbooks.open(absolute_path)


ws = wb.Worksheets('Sheet1')

ws.Range('A1:A10').Sort(Key1=ws.Range('A1'), Order1=1, Orientation=1)

wb.Save()
xl.Application.Quit()
