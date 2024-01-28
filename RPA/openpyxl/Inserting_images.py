from openpyxl import Workbook
from openpyxl.drawing.image import Image
# Remember to install Pillow; pip install Pillow

if __name__ == "__main__":
    # Create a workbook and sheets
    filename = "Images.xlsx"
    wb = Workbook()
    ws1 = wb["Sheet"]

    # create an image
    img = Image('logo.png')
    # add to worksheet and anchor next to cells
    ws1.add_image(img, 'A1')
    print("Image added to workbook")

    wb.save(filename)
            

    
