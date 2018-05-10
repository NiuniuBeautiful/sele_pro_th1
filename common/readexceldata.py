import xlrd
data = xlrd.open_workbook("testdata.xlsx")

table = data.sheet_by_name("Sheet1")  # 通过名称获取
nrows = table.nrows  # 读取整行
ncols = table.ncols  # 读取整列

print(nrows)
print(ncols)

print(table.row_values(0))
print(table.col_values(0))