import openpyxl
from openpyxl.styles import Font

wb = openpyxl.load_workbook('test1.xlsx')

sheet = wb.get_sheet_by_name('Sheet1')

# https://openpyxl.readthedocs.io/en/stable/styles.html
remove_strike = Font(strike=False)


for value in sheet:
    for cell in value:
       if cell.font.strike!=None:
            print(cell.value)

# wb.save(filename='test2.xlsx')