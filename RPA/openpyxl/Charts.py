from openpyxl import Workbook
from openpyxl.chart import BarChart, ScatterChart, PieChart, Reference, Series
from openpyxl.chart.series import DataPoint
from random import randint

def set_values(ws):
    counter = 2
    for column in ws1.iter_cols(min_row=2, min_col=1, max_col=1, max_row=11):
        for cell in column:
            cell.value = counter
            counter += 2
    for row in ws.iter_rows(min_row=2, min_col = 2, max_col=4, max_row=11):
        for cell in row:
            cell.value = randint(0,500)

def print_rows(ws):
    row_string = ""
    for row in ws.iter_rows(min_row=1, max_col=ws.max_column, max_row=ws.max_row):
        for cell in row:
            row_string += "{:<10}".format(str(cell.value) + " ")
        row_string += "\n"
    print(row_string)

if __name__ == "__main__":
    # Create a workbook and sheets
    filename = "Charts.xlsx"
    wb = Workbook()
    ws1 = wb["Sheet"]

    # Insert values from 1 to 100 into a grid of 10x10 cells
    headers = ["Number", "Torque", "Power", "Consumption"]
    ws1.append(headers)
    set_values(ws1)
    print_rows(ws1)

    series1 = Reference(ws1, min_col=1, min_row=1, max_col=1, max_row=11)
    series2 = Reference(ws1, min_col=2, min_row=1, max_col=2, max_row=11)
    series3 = Reference(ws1, min_col=3, min_row=1, max_col=3, max_row=11)
    series4 = Reference(ws1, min_col=4, min_row=1, max_col=4, max_row=11)
    series5 = Reference(ws1, min_col=2, min_row=2, max_col=2, max_row=6)

    # Add a Bar chart
    bar_chart = BarChart()
    bar_chart.add_data(series1, titles_from_data=True)
    bar_chart.add_data(series2, titles_from_data=True)
    bar_chart.title = "Bar Chart"
    bar_chart.style = 11
    bar_chart.x_axis.title = 'Size'
    bar_chart.y_axis.title = 'Percentage'
    ws1.add_chart(bar_chart, "A16")
    
    # Add a Scatter chart
    scatter_chart = ScatterChart()
    scatter_chart.title = "Scatter Chart"
    scatter_chart.style = 14
    scatter_chart.x_axis.title = 'Size'
    scatter_chart.y_axis.title = 'Percentage'
    series = Series(series1, series2, title_from_data=True)
    scatter_chart.series.append(series)
    ws1.add_chart(scatter_chart, "G1")
    
    # Add a Pie chart
    pie_chart = PieChart()
    labels = Reference(ws1, min_col=1, min_row=1, max_col=4, max_row=1)
    pie_chart.add_data(series5, titles_from_data=True)
    pie_chart.set_categories(labels)
    pie_chart.title = "Pie Chart"

    # Cut the first slice out of the pie
    pie_slice = DataPoint(idx=0, explosion=40)
    pie_chart.series[0].data_points = [pie_slice]
    ws1.add_chart(pie_chart, "K16")

    wb.save(filename)
            

    
