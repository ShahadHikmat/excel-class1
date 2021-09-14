# allows you to access openpyxl library and import work books
from openpyxl import workbook, load_workbook
# Loads the excel sheet from file source
workBookVariable = load_workbook('Grades.xlsx')
# workSheetVariable allows you to pick a specific sheet and we chose workBookVariable.active which is
# the current sheet we are on
workSheetVariable = workBookVariable.active
# prints Value of the cell you want
print(workSheetVariable["b3"].value)




