# TODO add employee gui
import openpyxl


# Instantiate a Workbook object by excel file path
workbook = self.Workbook("Employee database.xls")

# Access the first worksheet in the Excel file
worksheet = workbook.getWorksheets().get(0)

# Insert a row into the worksheet at 3rd position
worksheet.getCells().insertRows(2,1)

# Save the modified Excel file in default (that is Excel 2003) format
workbook.save("Employee database.xls")