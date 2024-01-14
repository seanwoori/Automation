from openpyxl import load_workbook
from openpyxl import Workbook

def save_wb(wb, filename):
    # Save a workbook
    wb.save(filename)

def open_wb(filename):
    # Returns an opened workbook
    return load_workbook(filename)

def create_sheets(wb, sheet_name_list):
    # Adds the sheets in the sheet_name_list to the workbook
    for sheet_name in sheet_name_list:
        wb.create_sheet(sheet_name)

def delete_sheet_by_name(wb, sheet_name):
    wb.remove(wb[sheet_name])

def copy_sheet(wb, source_sheet_name, new_sheet_name=""):
    new_sheet_name = "Copy of " + source_sheet_name if new_sheet_name == "" else new_sheet_name
    #Copy sheets
    source = wb[source_sheet_name]
    new_sheet = wb.copy_worksheet(source)
    new_sheet.title = new_sheet_name

def get_sheet_name_and_index_from_wb(wb):
    # Return a dictionary holding the indexes and names of the sheets
    sheet_name_index_dict = {}
    for index, sheet in enumerate(wb):
        sheet_name_index_dict[index] = sheet.title
    return sheet_name_index_dict

def get_sheet_by_index(wb, index):
    # Returns a sheet at the provided index
    try:
        return wb.worksheets[index]
    except IndexError:
        print("No sheet exists with index", index)

if __name__ == "__main__":
    wb = Workbook()
    create_sheets(wb, ["A sheet", "Another sheet", "Yet another sheet"])
    delete_sheet_by_name(wb, "Yet another sheet")
    copy_sheet(wb, "A sheet")
    copy_sheet(wb, "A sheet", "Fresh copy")
    print(get_sheet_by_index(wb, 3).title)
    #print(get_sheet_by_index(wb, 56).title)
    print("-"*60)
    print(get_sheet_name_and_index_from_wb(wb))
