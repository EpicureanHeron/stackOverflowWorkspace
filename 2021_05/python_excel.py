import openpyxl

book=openpyxl.load_workbook("test.xlsx")

sheet = book.active


b2 = sheet['B2']
b3 = sheet['B3']
b4 = sheet['B4']
b5 = sheet['B5']
b6 = sheet['B6']
b8 = sheet['B8']
i7 = sheet['I7']
print (i7)

value_to_add = b2.value * 5

sheet.cell(row=7, column=9).value = value_to_add


book.save('test.xlsx')