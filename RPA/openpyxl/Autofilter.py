from openpyxl import Workbook

def set_values(ws):
    data = [
    ["Fruit", "Quantity"],
    ["Kiwi", 1],
    ["Grape", 15],
    ["Apple", 3],
    ["Peach", 6],
    ["Pomegranate", 3],
    ["Pear", 7],
    ["Tangerine", 4],
    ["Blueberry", 58],
    ["Mango", 3],
    ["Watermelon", 19],
    ["Blackberry", 3],
    ["Orange", 25],
    ["Raspberry", 9],
    ["Banana", 7]
    ]
    for r in data:
        ws.append(r)

if __name__ == "__main__":
    # Create a workbook and sheets
    filename = "Filtering.xlsx"
    wb = Workbook()
    ws1 = wb["Sheet"]
    # Insert values from 1 to 100 into a grid of 10x10 cells
    set_values(ws1)

    # Set autofilter
    ws1.auto_filter.ref = "A1:B15"
    #ws1.auto_filter.add_filter_column(0, ["Kiwi", "Apple", "Mango"])
    ws1.auto_filter.add_sort_condition("B2:B15", descending=False)
    # OpenPyXL does not apply the filter, you have to do that manually.
    # This will add the relevant instructions to the file but will neither actually filter nor sort.

    wb.save(filename)
            

    
