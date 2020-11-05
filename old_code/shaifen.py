import xlrd
dz = r'C:\Users\WOOO\Desktop\1.xlsx'
book = xlrd.open_workbook(dz)
sheet1=book.sheet_by_index(0)
for i in range(sheet1.nrows):
    print(sheet1.cell_value(i,0),'  \t',sheet1.cell_value(i,1))