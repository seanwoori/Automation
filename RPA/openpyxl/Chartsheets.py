from openpyxl import Workbook
from openpyxl.chart import AreaChart, Reference

if __name__ == "__main__":
    # Create a workbook and sheets
    filename = "Chartsheets.xlsx"
    wb = Workbook()
    ws1 = wb["Sheet"]
    # Create a chartsheet
    cs = wb.create_chartsheet()

    rows = [
        ["Bricks", 3],
        ["Tiles", 2],
        ["Blocks", 4],
        ["Grass", 8],
        ["Plates", 8],
        ["Soil", 1],
    ]

    for row in rows:
        ws1.append(row)

    # Titles
    chart = AreaChart()
    chart.title = "Area Chart"
    chart.style = 13
    chart.x_axis.title = 'Item'
    chart.y_axis.title = 'Share of area'

    # Add the data to the chart
    data = Reference(ws1, min_col=2, min_row=1, max_row=6)
    categories = Reference(ws1, min_col=1, min_row=1, max_row=6)
    chart.add_data(data, titles_from_data=False)
    chart.set_categories(categories)
    # Add the chart to the chartsheet
    #cs.add_chart(chart)

    wb.save(filename)
            

    
