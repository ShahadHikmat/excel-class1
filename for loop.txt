# Using openpyxl to import library workbook
# allows you to access openpyxl library and import work books
from openpyxl import workbook, load_workbook
# Loads the excel sheet from file source
# load file grades file into workbook
# create a variable so you use the file  Grades.xlsx from load_workbook
workBookVariable = load_workbook('Grades.xlsx')
# workSheetVariable allows you to pick a specific sheet and we chose workBookVariable.active which is
# the current sheet we are on
# set workSheetVariable to blank.active
# set workSheetVariable to active excel work sheet
# Create workSheetVariable and associate with active worksheet bu using wb variable
workSheetVariable = workBookVariable.active
# A for loop is used for iterating over a sequence
# loop through to print value of the calls in column  with the last cell   ; you can change the number to letter
# you can check row with number and column with letters
for cell in workSheetVariable['c']:
    print(cell.value)
    # use a " for loop" to print Value of the cells in Rows ; you can change the number to letter
    # you can check row with number and column with letters
for cell in workSheetVariable['3']:
    print(cell.value)





