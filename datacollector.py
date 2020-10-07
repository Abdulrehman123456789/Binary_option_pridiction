import time
import pyscreenshot as ImageGrab
import pytesseract       
from PIL import Image  
import pyautogui
import datetime


f=open('tradedata.txt','w')
f.write("")
f.close()



pasttime=-1

datarow=""

prevalue='1' 

currentrow=1



#inter the number of rows in dataset
number_of_row_for_training=15


while True:

	time.sleep(5)

	currenttime=datetime.datetime.now().time()
	datearr=str(currenttime).split(':')
	presenttime=datearr[1]
	print(presenttime)


	f1=open("sync.txt",'w')
	f1.write("0")
	f1.close()


	im=ImageGrab.grab(bbox=(367,530,569,604))
	im.save('mydata.png')
	print("screenshort taken")


	  
	try:         
 		
		img = Image.open('mydata.png')
		result = pytesseract.image_to_string(img)  
		print(result)
		cheakfloat=float(result)
		datarow=datarow+result+"/"
		prevalue=result



	except:
		print("unable to extract the information") 
		datarow=datarow+prevalue+"/"


		#GUI disturbance handalor
		pyautogui.click(x=1003, y=571)



	if pasttime!=presenttime:

		if currentrow>number_of_row_for_training:
			remstring=""
			f=open('tradedata.txt','r')
			data=f.read()
			f.close()
			dataarr=data.split('\n')
			print("dataarr")
			print(dataarr)
			remainingdataarr=dataarr[1:]
			print("remainingdataarr")
			print(remainingdataarr)
			for i in range(0,len(remainingdataarr)-1):
				remstring=remstring+remainingdataarr[i]+"\n"
			print("remainingdata")
			print(remstring)
			print("present_tuple")
			print(datarow) 
			fianlstring=remstring+datarow
			print("finaldataset")
			print(fianlstring)
			f=open('tradedata.txt','w')
			f.write("")
			f.write(fianlstring)
			f.write("\n")
			f.close()
			pasttime=presenttime
			datarow=""
			print("DATASET READY")


			f1=open("sync.txt",'w')
			f1.write("1")
			f1.close()

		else:


			f=open('tradedata.txt','a')


			print(datarow) 


			f.write(datarow)

			f.write("\n")

			pasttime=presenttime
			datarow=""

			currentrow=currentrow+1

			f.close()





