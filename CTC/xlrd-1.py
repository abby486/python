#-*-coding:gb2312-*-
import string
import re
from xlrd import open_workbook
from xlutils.copy import copy

rb = open_workbook("cq.xls")
numRS = 0
for s in rb.sheets():
	numRS = numRS + 1 
numWS = numRS

i = 0
w1 = "��Ե"
wb = copy(rb)
while i < numWS:
	ws = wb.get_sheet(i)
	print'Sheet:', ws.name
	if ws.name.encode("gb2312").find(w1) >= 0:
		print 'Sheet: Find edge in', ws.name
		ws = wb.get_sheet(i)
		ws.write(0,1,"changed")
		wb.save("cq1.xls")
	i = i+1

