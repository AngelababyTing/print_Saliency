import os
import sys
import math
import _thread

input = sys.argv[1]
output = sys.argv[2]
filecount = 0
start = 1
end = 50
threadNum = 0
threadfile = 0

#列出輸入參數位置底下的文件
def print_Saliency(thr_name, start, end):
	global input
	global output

	for work in range(start, end+1):
		work_string = str(work)
		print(str(thr_name) + " ---")
		os.system("E:\hsaliencyexe\HSaliency.exe " + input + "\\" + work_string + ".jpg " + output)

#計算文件數量
for filename in os.listdir(input): 
	filecount += 1

#計算要開啟的多線程(Thread)個數
threadNum = int(math.floor(filecount / 50))
threadfile = filecount % 50

try:
	for threadNum in range(threadNum):
		_thread.start_new_thread( print_Saliency, (threadNum+1, start, end))
		start += 50
		end += 50

	if threadfile != 0:
		_thread.start_new_thread( print_Saliency, ("thr_name", ((threadNum+1)*50)+1, filecount))
except:
	pass
	
while 1:
	pass